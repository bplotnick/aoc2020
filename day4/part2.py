import re
from typing import Dict
from typing import Callable

filename = "input.txt"


def range_validator_factory(left_bound: int, right_bound: int) -> Callable[[str], bool]:
    def func(val: str) -> bool:
        ival = int(val)
        if ival >= left_bound and ival <= right_bound:
            return True
        else:
            return False

    return func


byr_fn = range_validator_factory(1920, 2002)
iyr_fn = range_validator_factory(2010, 2020)
eyr_fn = range_validator_factory(2020, 2030)


def hgt_fn(val: str) -> bool:
    if val.endswith("cm"):
        return range_validator_factory(150, 193)(val[:-2])
    elif val.endswith("in"):
        return range_validator_factory(59, 76)(val[:-2])
    else:
        return False


def hcl_fn(val: str) -> bool:
    if re.match(r"^#[0-9a-f]{6}$", val) is not None:
        return True
    else:
        return False


def ecl_fn(val: str) -> bool:
    valid_ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if val in valid_ecls:
        return True
    else:
        return False


def pid_fn(val: str) -> bool:
    if re.match(r"^[0-9]{9}$", val) is not None:
        return True
    else:
        return False


validate_fns = {
    "byr": byr_fn,
    "iyr": iyr_fn,
    "eyr": eyr_fn,
    "hgt": hgt_fn,
    "hcl": hcl_fn,
    "ecl": ecl_fn,
    "pid": pid_fn,
}


def check_pass(passport: Dict[str, str]) -> bool:
    for key in validate_fns.keys():
        if key not in passport or not validate_fns[key](passport[key]):
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
