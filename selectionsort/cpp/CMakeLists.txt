cmake_minimum_required(VERSION 3.20)
project(selectionsort 
		VERSION 1.0
		DESCRIPTION "Implementation of Selection Sort"
		LANGUAGES CXX)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

configure_file(selectionsort.h.in selectionsort.h)

add_executable(
  main
  main.cpp
)

target_include_directories(main PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )
