cmake_minimum_required(VERSION 3.20)
project(project_name LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

add_compile_options(-Wall -Wextra -Wpedantic)

# ---- Library (put reusable code here so tests can link it) ----
add_library(core
  src/core.cpp
)
target_include_directories(core PUBLIC src)

# ---- Main executable ----
add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE core)

# ---- Tests (Catch2 via FetchContent; swap for GoogleTest if you prefer) ----
include(FetchContent)
FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v3.5.2
)
FetchContent_MakeAvailable(Catch2)

enable_testing()
add_executable(tests tests/test_core.cpp)
target_link_libraries(tests PRIVATE core Catch2::Catch2WithMain)

include(CTest)
include(Catch)
catch_discover_tests(tests)
