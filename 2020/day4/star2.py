import re

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
        if (
            (1920 <= int(structured_passport["byr"]) <= 2002)
            and (2010 <= int(structured_passport["iyr"]) <= 2020)
            and (2020 <= int(structured_passport["eyr"]) <= 2030)
            and (
                structured_passport["hcl"][0] == "#"
                and len(structured_passport["hcl"][1:]) == 6
                and structured_passport["hcl"][1:].isalnum()
            )
            and (
                structured_passport["ecl"]
                in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
            )
            and (
                structured_passport["pid"].isdigit()
                and len(structured_passport["pid"]) == 9
            )
        ):
            if (
                "in" in structured_passport["hgt"]
                and "cm" in structured_passport["hgt"]
            ):
                ### we can't have both in the string
                return False
            elif "in" in structured_passport["hgt"]:
                if 59 <= int(structured_passport["hgt"][:-2]) <= 76:
                    return True
                else:
                    return False
            elif "cm" in structured_passport["hgt"]:
                if 150 <= int(structured_passport["hgt"][:-2]) <= 193:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
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
