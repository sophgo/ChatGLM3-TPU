cmake_minimum_required(VERSION 2.8)
project(ChatGLM)


set(LIBSOPHON /opt/sophon/libsophon-current)
include_directories(${LIBSOPHON}/include)
include_directories(${PROJECT_SOURCE_DIR}/include)
link_directories(${LIBSOPHON}/lib)
link_directories(${PROJECT_SOURCE_DIR}/lib)

add_definitions(-DDEBUG --std=c++17 -fPIC -Wall -Werror)
set(CMAKE_BUILD_TYPE "Debug")

find_package(pybind11 REQUIRED CONFIG)
pybind11_add_module(ChatGLM ChatGLM.cpp)


target_link_libraries(ChatGLM bmrt bmlib sentencepiece)
install(TARGETS ChatGLM DESTINATION python)
