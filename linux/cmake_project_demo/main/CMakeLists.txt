message(STATUS "Build in main folder")
set (MODULE_MAIN demo)

#include_directories("{CMAKE_SOUCE_DIR}/math" "${CMAKE_SOURCE_DIR}/utility")

add_executable(${MODULE_MAIN} main.cpp)

target_link_libraries(${MODULE_MAIN}
					${CMAKE_BINARY_DIR}/utility/libutility.so
					${CMAKE_BINARY_DIR}/math/libmath.so)