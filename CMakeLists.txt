cmake_minimum_required(VERSION 3.15)
project(mjs_trader VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(SOURCES
    src/core_lib/trader_core_lib.cpp
)

add_library(core_lib ${SOURCES})
target_include_directories(core_lib PUBLIC include)

find_package(fmt REQUIRED)

add_executable(mjs_trader src/main.cpp)
target_link_libraries(mjs_trader PRIVATE core_lib fmt::fmt)