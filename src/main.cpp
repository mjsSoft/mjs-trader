#include <iostream>
#include <fmt/core.h>

#include "core_lib/trader_core_lib.hpp"

int main()
{
    std::cout << "Hello:)) " << std::endl;
    std::cout << add(2) << std::endl;
    fmt::print("Hello, {}!\n", "Conan & fmt");
    return 0;
}
