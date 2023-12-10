cmake_minimum_required(VERSION 3.0.0)
project(Integrales_numericas VERSION 0.1.0)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable(Integrales_numericas main.cpp plot_graph.h)

target_link_libraries( Integrales_numericas ${OpenCV_LIBS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)