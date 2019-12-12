cmake_minimum_required(VERSION 3.15)
project(advent_of_code_2019)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(day_1)

### conan setup
if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()

add_executable(advent_of_code_2019
        #        day_1/d1_sol1.cpp
#        day_1/d1_sol2.cpp
        day_1/module_mass.txt
        README.md
        day_2/d2_sol1.cpp)
