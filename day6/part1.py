filename = "input.txt"


def main():
    with open(filename) as f:
        answers_per_group = f.read().split("\n\n")
    count = 0
    for group in answers_per_group:
        answers = set()
        for answer in group.split("\n"):
            answers = answers.union(set(answer))
        count += len(answers)
    print(count)


main()
