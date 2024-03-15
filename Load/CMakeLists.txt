cmake_minimum_required(VERSION 3.25)

project(gpiod LANGUAGES C)

add_executable(Load Load.c)

target_link_libraries(Load gpiod)
