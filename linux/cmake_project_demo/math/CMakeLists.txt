message(STATUS "Enter math folder")
set(MODULE_MATH math)

aux_source_directory(. MATH_SOURCE)

add_library(${MODULE_MATH} SHARED ${MATH_SOURCE})