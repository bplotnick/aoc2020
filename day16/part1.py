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


def main():
    constraints, your_ticket, nearby_tickets = read_input("input.txt")

    failed_vals = []
    for idx, tick in enumerate(nearby_tickets):
        #        failed_ticket = False
        for field in tick:
            for constraint in constraints.values():
                failed_constraint = True
                if not (
                    field < constraint[0][0]
                    or (constraint[0][1] < field < constraint[1][0])
                    or field > constraint[1][1]
                ):
                    failed_constraint = False
                    break
            if failed_constraint:
                #                failed_ticket = True
                failed_vals.append((idx, field))

    print(failed_vals)
    total = 0
    for v in failed_vals:
        total += v[1]
    print(total)


main()
