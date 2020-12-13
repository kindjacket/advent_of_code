from utils import get_input


class Command:
    def __init__(self, idx, raw_input):
        self.idx = idx
        self.command = self.parse_command(raw_input)[0]
        self.action = self.parse_command(raw_input)[1]

    def increase_accumulator(self, accumulator):
        if self.command == 'acc':
            accumulator += self.action
        return accumulator

    def next_idx(self):
        if self.command in {'acc', 'nop'}:
            return self.idx + 1
        else:
            return self.idx + self.action

    def possible_jump_to(self):
        if self.command in {"jmp", "nop"}:
            return self.idx + self.action
        else:
            return None

    @staticmethod
    def parse_command(input_command_raw: str) -> tuple:
        split_command = input_command_raw.split(" ")
        return split_command[0], int(split_command[1])


def run_program(input_data):
    accumulator = 0
    current_idx = 0
    previously_visited_idxs = set()
    while current_idx not in previously_visited_idxs:
        previous_idx = current_idx
        command = Command(current_idx, input_data[current_idx])
        accumulator = command.increase_accumulator(accumulator)
        current_idx = command.next_idx()
        previously_visited_idxs.add(previous_idx)
    return accumulator, previously_visited_idxs


def get_smooth_finish_idxs(input_data):
    last_idx = len(input_data) - 1  ### last element in list
    smooth_finish_idxs = {last_idx}
    steps_back = 1
    previous_command = Command(last_idx - steps_back, input_data[last_idx - steps_back])
    while previous_command.command in {"acc", "nop"}:
        smooth_finish_idxs.add(last_idx - steps_back)
        steps_back += 1
        previous_command = Command(
            last_idx - steps_back, input_data[last_idx - steps_back]
        )
    return smooth_finish_idxs

def test_for_possible_change(bad_program_loop, smooth_finish_idxs, input_data):
    possible_routes_to_smooth_finish = {
        idx
        for idx, i in enumerate(input_data)
        if Command(idx, i).possible_jump_to() in smooth_finish_idxs
    }
    if possible_routes_to_smooth_finish == ''


def main():
    input_data = get_input()
    ### to get the routes to the smooth finish we need to get all nop and jmp
    accumulator, bad_program_loop =  run_program(input_data)
    ### then we need to filter them on ones that idx + command in the set
    ### we then need to see if any of those are in the loop idx set
    smooth_finish_idxs = get_smooth_finish_idxs(input_data)
    count = 0


if __name__ == "__main__":
    main()
