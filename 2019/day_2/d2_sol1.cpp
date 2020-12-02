#include <vector>
#include <set>

static void opcode_validator(int opcode) {
    std::set<int> opcodes = {1, 2, 99};
    // will return true if in the set, false if not
    const bool valid = opcodes.find(opcode) != opcodes.end();
    if (!valid) {
        printf("bad data");
    }
}

// we &vec if we want to mutate the vector https://www.geeksforgeeks.org/passing-vector-function-cpp/
static int opcode_operator(int opcode_index, std::vector<int> &vec) {
    int opcode = vec.at(opcode_index);
    opcode_validator(opcode);
    int position_1 = vec.at(opcode_index + 1);
    int position_2 = vec.at(opcode_index + 2);
    int storage_position = vec.at(opcode_index + 3);
    int next_index = opcode_index + 4;
    if (opcode == 1) {
        //Opcode 1 adds together numbers read from two positions and stores the result in a third position.
        //The three integers immediately after the opcode tell you these three positions - the first two indicate
        //the positions from which you should read the input values, and the third indicates the position
        //at which the output should be stored.

        //For example, if your Intcode computer encounters 1,10,20,30,
        //it should read the values at positions 10 and 20, add those values,
        //and then overwrite the value at position 30 with their sum.
        vec.at(storage_position) = vec.at(position_1) + vec.at(position_2);
    } else if (opcode == 2) {
//        Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead
//        of adding them. Again, the three integers after the opcode indicate where the inputs
//        and outputs are, not their values.
        vec.at(storage_position) = vec.at(position_1) * vec.at(position_2);
    }
    return next_index;
}


int main() {
    std::vector<int> vec{1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 10, 19, 23, 1, 6, 23, 27,
                         1, 5, 27, 31, 1, 10, 31, 35, 2, 10, 35, 39, 1, 39, 5, 43, 2, 43, 6, 47, 2, 9, 47, 51, 1,
                         51, 5, 55, 1, 5, 55, 59, 2, 10, 59, 63, 1, 5, 63, 67, 1, 67, 10, 71, 2, 6, 71, 75, 2, 6,
                         75, 79, 1, 5, 79, 83, 2, 6, 83, 87, 2, 13, 87, 91, 1, 91, 6, 95, 2, 13, 95, 99, 1, 99, 5,
                         103, 2, 103, 10, 107, 1, 9, 107, 111, 1, 111, 6, 115, 1, 115, 2, 119, 1, 119, 10, 0, 99, 2,
                         14, 0, 0};
    // add adjustments based on specs
    // replace position 1 with the value 12 and replace position 2 with the value 2.
    vec.at(1) = 12;
    vec.at(2) = 2;
    int current_opcode_index = 0;
    int current_opcode = vec.at(current_opcode_index);
    while (current_opcode != 99) {
        current_opcode_index = opcode_operator(current_opcode_index, vec);
        current_opcode = vec.at(current_opcode_index);
    }
    int output = vec.at(0);
    printf("%i", output);
}



