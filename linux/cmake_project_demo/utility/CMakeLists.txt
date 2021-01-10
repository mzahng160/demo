message(STATUS "Enter utility folder")
set(MODULE_UTILITY utility)

set (UTILITY_SOURCE utils.cpp)

add_library(${MODULE_UTILITY} SHARED ${UTILITY_SOURCE})