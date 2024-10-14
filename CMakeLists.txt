cmake_minimum_required(VERSION 3.5.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

project(Cynthesis)

include_directories(${CMAKE_SOURCE_DIR}/include)

set(SOURCES
    ${CMAKE_SOURCE_DIR}/main.cc
    ${CMAKE_SOURCE_DIR}/src/core.cc
    ${CMAKE_SOURCE_DIR}/src/utils/renderQueue.cc
)

set(HEADERS
    ${CMAKE_SOURCE_DIR}/include/core.h
    ${CMAKE_SOURCE_DIR}/include/camera.h
    ${CMAKE_SOURCE_DIR}/include/utils/renderQueue.h
    ${CMAKE_SOURCE_DIR}/include/entities/entity.h
)

add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

find_package(SDL2 REQUIRED)
target_link_libraries(${PROJECT_NAME} SDL2)


find_package(SDL2_image REQUIRED)
target_link_libraries(${PROJECT_NAME} SDL2_image)


set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${CMAKE_SOURCE_DIR}/assets ${CMAKE_BINARY_DIR}/bin/assets
)
