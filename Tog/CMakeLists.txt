cmake_minimum_required(VERSION 3.25)

project(gpiod LANGUAGES C)

add_executable(toggle toggle1.c)

target_link_libraries(toggle gpiod)
