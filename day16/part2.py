def read_input(filename):
    constraints = {}
    with open(filename) as f:
        lines = f.read().splitlines()

    idx = 0
    l = lines[idx]
    while l:
        k, v = l.strip().split(": ")
        lrange, rrange = v.split(" or ")
        val = [[int(x) for x in lrange.split("-")], [int(x) for x in rrange.split("-")]]
        constraints[k] = val
        idx += 1
        l = lines[idx]

    idx += 1
    assert "your ticket" in lines[idx]
    idx += 1
    your_ticket = lines[idx].split(",")
    your_ticket = [int(x) for x in your_ticket]

    idx += 2
    assert "nearby tickets" in lines[idx]
    idx += 1
    nearby_tickets = [l.split(",") for l in lines[idx:]]
    nearby_tickets = [[int(num) for num in tick] for tick in nearby_tickets]

    return constraints, your_ticket, nearby_tickets


def is_valid_for_constraint(constraint, field):
    return not (
        field < constraint[0][0]
        or (constraint[0][1] < field < constraint[1][0])
        or field > constraint[1][1]
    )


def remove_bad_ticks(constraints, nearby_tickets):
    failed_ticks = []
    for idx, tick in enumerate(nearby_tickets):
        #        failed_ticket = False
        for field in tick:
            for constraint in constraints.values():
                failed_constraint = True
                if is_valid_for_constraint(constraint, field):
                    failed_constraint = False
                    break
            if failed_constraint:
                #                failed_ticket = True
                failed_ticks.append(tick)
                break

    for f in failed_ticks:
        nearby_tickets.remove(f)
    return nearby_tickets


def main():
    constraints, your_ticket, nearby_tickets = read_input("input.txt")

    nearby_tickets = remove_bad_ticks(constraints, nearby_tickets)

    all_ticks = [your_ticket] + nearby_tickets

    # list of sets of valid constraints. each element is a separate field
    fields_valid_constraints = [set(constraints.keys()) for _ in all_ticks[0]]
    for field_name, constraint in constraints.items():
        for field_idx in range(len(all_ticks[0])):
            for tick in all_ticks:
                if not is_valid_for_constraint(constraint, tick[field_idx]):
                    fields_valid_constraints[field_idx].remove(field_name)
                    break

    solutions = [None] * len(all_ticks[0])
    found_one_solution = True
    while found_one_solution:
        found_one_solution = False
        for idx, c in enumerate(fields_valid_constraints):
            if len(c) == 1:
                found_one_solution = True
                cur_solution = c.pop()
                solutions[idx] = cur_solution
                break
        if found_one_solution:
            for field in fields_valid_constraints:
                field.discard(cur_solution)

    total = 1
    for idx, s in enumerate(solutions):
        if "departure" in s:
            total *= your_ticket[idx]

    print(total)


main()
