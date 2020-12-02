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
static int opcode_operator(int instruction_pointer, std::vector<int> &vec) {
    int opcode = vec.at(instruction_pointer);
    opcode_validator(opcode);
    // parameters
    int position_1 = vec.at(instruction_pointer + 1);
    int position_2 = vec.at(instruction_pointer + 2);
    int storage_position = vec.at(instruction_pointer + 3);
    int next_instruction_pointer = instruction_pointer + 4;
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
    return next_instruction_pointer;
}

// this time we want to copy the input vector
static int test_inputs(int noun, int verb, std::vector<int> memory) {
    memory.at(1) = noun;
    memory.at(2) = verb;
    int current_address = 0;
    int current_opcode = memory.at(current_address);
    while (current_opcode != 99) {
        current_address = opcode_operator(current_address, memory);
        current_opcode = memory.at(current_address);
    }
    return memory.at(0);
}


int main() {
    std::vector<int> memory{1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 10, 19, 23, 1, 6, 23, 27,
                            1, 5, 27, 31, 1, 10, 31, 35, 2, 10, 35, 39, 1, 39, 5, 43, 2, 43, 6, 47, 2, 9, 47, 51, 1,
                            51, 5, 55, 1, 5, 55, 59, 2, 10, 59, 63, 1, 5, 63, 67, 1, 67, 10, 71, 2, 6, 71, 75, 2, 6,
                            75, 79, 1, 5, 79, 83, 2, 6, 83, 87, 2, 13, 87, 91, 1, 91, 6, 95, 2, 13, 95, 99, 1, 99, 5,
                            103, 2, 103, 10, 107, 1, 9, 107, 111, 1, 111, 6, 115, 1, 115, 2, 119, 1, 119, 10, 0, 99, 2,
                            14, 0, 0};
    int target_value = 19690720;
    // I will brute force to see what values give me the number we are aiming for
    for (int i = 0; i <= 99; i++) {
        for (int j = 0; j <= 99; j++) {
            int output = test_inputs(i, j, memory);
            if (output == target_value) {
                int noun = i;
                int verb = j;
                int result = (100 * noun) + verb;
                printf("%i", result);
                break;
            }
        }
    }
}
