from utils import get_input


def clean_group_forms(input_data: list[str]):
    group_inputs = []
    group_input = set()
    ### add blank list to the end of the list so logic works smoomthly. A bit of hack
    input_data.append([])
    for i in input_data:
        if len(i) > 0:
            group_input.update(set(list(i)))
        else:
            ### line break and therefore end of input data
            group_inputs.append(group_input)
            group_input = set()
    return group_inputs


def main():
    input_data = [i for i in get_input()]
    group_inputs = clean_group_forms([i for i in input_data])
    print(sum([len(i) for i in group_inputs]))


if __name__ == "__main__":
    main()
