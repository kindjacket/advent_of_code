from utils import get_input

ROW_TOTAL = 127
COL_TOTAL = 7
MAPPING = {"F": 0, "B": 1, "R": 1, "L": 0}


def decode_seat_code(seat_code):
    row_code = seat_code[0:7]
    col_code = seat_code[7:10]
    row = sum(
        [
            ((ROW_TOTAL + 1) / (2 ** (idx + 1))) * MAPPING[i]
            for idx, i in enumerate(row_code)
        ]
    )
    col = sum(
        [
            ((COL_TOTAL + 1) / (2 ** (idx + 1))) * MAPPING[i]
            for idx, i in enumerate(col_code)
        ]
    )
    seat_id = (row * 8) + col
    return seat_id


def main():
    input_data = [i for i in get_input()]
    print(max([decode_seat_code(i) for i in input_data]))


if __name__ == "__main__":
    main()
