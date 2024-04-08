cmake_minimum_required(VERSION 3.10)

project(pr_backend)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(fmt CONFIG REQUIRED)

add_executable(pr_backend src/main.cxx)

target_link_libraries(pr_backend PRIVATE fmt::fmt)
