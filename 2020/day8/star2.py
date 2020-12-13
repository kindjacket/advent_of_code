from utils import get_input


class Command:
    def __init__(self, idx, raw_input):
        self.idx = idx
        self.command = self.parse_command(raw_input)[0]
        self.action = self.parse_command(raw_input)[1]

    def increase_accumulator(self, accumulator):
        self.acc_command_input = accumulator
        if self.command == "acc":
            accumulator += self.action
        return accumulator

    def next_idx(self):
        if self.command in {"acc", "nop"}:
            return self.idx + 1
        else:
            return self.idx + self.action

    @staticmethod
    def parse_command(input_command_raw: str) -> tuple:
        split_command = input_command_raw.split(" ")
        return split_command[0], int(split_command[1])


def run_program(input_data, accumulator=0, current_idx=0):
    accumulator = accumulator
    current_idx = current_idx
    starting_command = Command(current_idx, input_data[current_idx])
    if starting_command.command == "nop":
        starting_command.command = "jmp"
    elif starting_command.command == "jmp":
        starting_command.command = "nop"
    previously_visited_idxs = set()
    all_commands = []
    while current_idx not in previously_visited_idxs and current_idx < len(input_data):
        previous_idx = current_idx
        if current_idx == starting_command.idx:
            command = starting_command
        else:
            command = Command(current_idx, input_data[current_idx])
        accumulator = command.increase_accumulator(accumulator)
        current_idx = command.next_idx()
        previously_visited_idxs.add(previous_idx)
        all_commands.append(command)
    return starting_command, accumulator, all_commands


def main():
    input_data = get_input()
    ### to get the routes to the smooth finish we need to get all nop and jmp
    starting_command, accumulator, bad_program_commands = run_program(input_data)
    tested_routes = [
        run_program(input_data, i.acc_command_input, i.idx)
        for i in bad_program_commands
        if i.command in {"jmp", "nop"}
    ]
    fixed_routes = [
        i for i in tested_routes if max([j.idx for j in i[2]]) == (len(input_data) - 1)
    ]
    print(fixed_routes[0][1])


if __name__ == "__main__":
    main()
