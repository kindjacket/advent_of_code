from utils import get_input


def parse_and_follow_commands(input_data):
    accumulator = 0
    current_idx = 0
    previously_visited_idxs = set()
    while current_idx not in previously_visited_idxs:
        ready_input = input_data[current_idx].split(" ")
        previous_idx = current_idx
        input_code = ready_input[0]
        input_operation = int(ready_input[1])
        if input_code == "acc":
            accumulator += input_operation
            current_idx += 1
        elif input_code == "jmp":
            current_idx += input_operation
        else:
            current_idx += 1
        previously_visited_idxs.add(previous_idx)
    return accumulator


def main():
    input_data = get_input()
    print(parse_and_follow_commands(input_data))


if __name__ == "__main__":
    main()
