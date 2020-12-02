#include <cmath>
#include <fstream>

static int fuel_for_weight(int a) {
    // this is the calculation for the fuel required for a given
    int r;
    r = (int) floor(a / 3) - 2;
    // if the result is less than 0 we return 0
    return std::max(r, 0);
}

static int fuel_for_module(int a) {
    // this compute the fuel for a module and then the fuel for the fuel weight
    int total_module_fuel = 0;
    int fuel_req = a;
    while (fuel_req > 0) {
        fuel_req = fuel_for_weight(fuel_req);
        total_module_fuel = total_module_fuel + fuel_req;
    }
    return total_module_fuel;
}

int main() {
    std::ifstream infile("day_1/module_mass.txt");
    std::string line;
    double tf = 0;
    while (std::getline(infile, line)) {
        int i = std::stoi(line);
        tf = tf + fuel_for_module(i);
    }
    printf("%f", tf);
}

