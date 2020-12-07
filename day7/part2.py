from typing import List, Tuple, Set, Dict, DefaultDict
from collections import defaultdict
import re

filename = "input.txt"


class Bag:
    def __init__(self, color: str, contents: Dict[str, int]):
        self.color = color
        self.contents = contents
        self.parents: Set[Bag] = set()

    def __hash__(self):
        return hash(self.color)

    def __eq__(self, other):
        return self.color == other.color

    def __repr__(self):
        return "<Bag {}>".format(self.color)


def construct_inventory(rules: List[str]) -> Dict[str, Bag]:
    first_match_re = r"^(?P<color>.*) bags contain (?P<contents>.*)\.\n$"
    bag_re = r"^(?P<number>[0-9]+) (?P<color>.*) bag[s]?"
    bags = {}
    for rule in rules:
        m = re.match(first_match_re, rule)
        if m is None:
            raise ValueError(
                f"Regex is wrong or input is invalid: {first_match_re},{rule}"
            )
        match = m.groupdict()
        color = match["color"]
        contents = match["contents"].split(", ")
        if contents[0] == "no other bags":
            contents = []
        contents_dict = {}
        for c in contents:
            m = re.match(bag_re, c)
            if m is None:
                raise ValueError(f"Regex is wrong or input is invalid: {bag_re},{c}")
            match = m.groupdict()
            contents_dict[match["color"]] = int(match["number"])
        bags[color] = Bag(color, contents_dict)
    return bags


def dfs_bags(bags: Dict[str, Bag], bag: Bag) -> int:
    total = 1
    for child, count in bag.contents.items():
        total += count * dfs_bags(bags, bags[child])
    return total


def main():
    with open(filename) as f:
        rules = f.readlines()

    bags = construct_inventory(rules)

    # Then create the parent links
    for bag in bags.values():
        for k in bag.contents:
            bags[k].parents.add(bag)

    # Replace contents with bag objects so that we don't need the big bag dict
    starting_bag = bags["shiny gold"]

    total = dfs_bags(bags, starting_bag) - 1  # Don't include self

    print(len(bags))
    print(total)


main()
