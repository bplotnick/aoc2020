from typing import Tuple

filename = "input.txt"
NUM_ROWS = 128
NUM_COLS = 8


def bin_part(letters: str, num_total: int) -> int:
    cur = list(range(num_total))
    for letter in letters:
        if letter in ("F", "L"):
            cur = cur[: len(cur) // 2]
        elif letter in ("B", "R"):
            cur = cur[len(cur) // 2 :]
        else:
            raise
    assert len(cur) == 1
    return cur[0]


def parse_seat(seat: str) -> Tuple[int, int]:
    row_strs = seat[:7]
    col_strs = seat[7:]

    row = bin_part(row_strs, NUM_ROWS)
    col = bin_part(col_strs, NUM_COLS)
    return row, col


def main():
    theo_seats = set(range(NUM_ROWS * 8 + NUM_COLS))
    seats_taken = set()
    with open(filename) as f:
        seats = f.read().splitlines()
        max_seat = 0
    for s in seats:
        row, col = parse_seat(s)
        seat_id = row * 8 + col
        max_seat = max(max_seat, seat_id)
        seats_taken.add(seat_id)
    theo_seats -= seats_taken
    for seat in theo_seats:
        if seat - 1 in seats_taken and seat + 1 in seats_taken:
            print(seat)


if __name__ == "__main__":
    main()
