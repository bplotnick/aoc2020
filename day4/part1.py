from typing import Dict

filename = "input.txt"

req_keys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #    'cid',
]


def check_pass(passport: Dict[str, str]) -> bool:
    for key in req_keys:
        if passport.get(key) is None:
            return False
    return True


def main():
    count = 0
    with open(filename) as f:
        passports = f.read().split("\n\n")
    for i in range(len(passports)):
        passports[i] = passports[i].replace("\n", " ")
    for p in passports:
        parsed_pass = dict([val.split(":") for val in p.strip().split(" ")])
        if check_pass(parsed_pass):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
