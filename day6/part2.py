import string

filename = "input.txt"


def main():
    with open(filename) as f:
        answers_per_group = f.read().split("\n\n")
    count = 0
    for group in answers_per_group:
        answers = set(string.ascii_lowercase)
        print("----")
        for answer in group.strip().split("\n"):
            answers = answers.intersection(set(answer))
            print("{} - {}".format(answer, answers))
        count += len(answers)
    print(count)


main()
