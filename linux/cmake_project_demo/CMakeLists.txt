cmake_minimum_required (VERSION 2.8.0)
#set(PROJECT_NAME "test")
project (mytest)
SET(VERSION "2.0.0")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}")   # 设置可执行文件的输出目录

add_subdirectory(math)       # 包含下级子目录math
add_subdirectory(utility)
add_subdirectory(main)