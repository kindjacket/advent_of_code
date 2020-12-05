import re

from utils import get_input_for_day

DAY = 2

input_data = get_input_for_day(DAY)
valid_pw_count = 0
for i in input_data:
    data_as_list = re.split("-|: | ", i)
    assert len(data_as_list) == 4, "regex has failed"
    positions_to_read = [int(i) - 1 for i in data_as_list[:2]]
    letter = data_as_list[2]
    password = data_as_list[3]
    if [password[positions_to_read[0]], password[positions_to_read[1]]].count(
        letter
    ) == 1:
        valid_pw_count += 1
print(valid_pw_count)
