cmake_minimum_required(VERSION 3.27)

project(main LANGUAGES CXX)
set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g") # debug flag

include_directories(src)
set(SOURCES class.cpp)

add_library(class SHARED ${SOURCES})