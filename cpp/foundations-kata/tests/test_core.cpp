#include <catch2/catch_test_macros.hpp>

#include "core.hpp"

TEST_CASE("add sums two integers", "[core]") {
  REQUIRE(core::add(2, 3) == 5);
  REQUIRE(core::add(-1, 1) == 0);
}
