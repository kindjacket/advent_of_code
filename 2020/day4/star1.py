from utils import get_input

REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def clean_passport_inputs(input_data: list[str]):
    passport_inputs = []
    passport_input = ""
    ### add blank list to the end of the list so logic works smoomthly. A bit of hack
    input_data.append([])
    for idx, i in enumerate(input_data):
        if len(i) > 0:
            if len(passport_input) > 0:
                ### we add a space to the input to make it easier to parse
                passport_input += f" {i}"
            else:
                passport_input += i
        else:
            ### line break and therefore end of input data
            passport_inputs.append(passport_input)
            passport_input = ""
    return passport_inputs


def raw_passport_input_to_key_values(passport_input: str):
    fields = passport_input.split(" ")
    key_values = {i.split(":")[0]: i.split(":")[1] for i in fields}
    return key_values


def passport_validator(structured_passport: dict[str:str]):
    if (set(structured_passport.keys()) & REQUIRED_KEYS) == REQUIRED_KEYS:
        return True
    else:
        return False


def main():
    input_data = [i for i in get_input()]
    passport_inputs = clean_passport_inputs(input_data)
    structured_passport_data = [
        raw_passport_input_to_key_values(i) for i in passport_inputs
    ]
    valid_passport_count = len(
        [i for i in structured_passport_data if passport_validator(i)]
    )
    print(valid_passport_count)


if __name__ == "__main__":
    main()
