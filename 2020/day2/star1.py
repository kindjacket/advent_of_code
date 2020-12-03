import re
from utils import get_input

DAY = 2

input_data = get_input(DAY)
valid_pw_count = 0
for i in input_data:
    data_as_list = re.split('-|: | ', i)
    assert len(data_as_list) == 4, "regex has failed"
    min_count = int(data_as_list[0])
    max_count = int(data_as_list[1])
    letter = data_as_list[2]
    password = data_as_list[3]
    if min_count <= password.count(letter) <= max_count:
        valid_pw_count += 1
print(valid_pw_count)
