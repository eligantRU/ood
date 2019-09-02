#include "stdafx.h"

#include "../gumball_machine/GumBallMachineWithState.h"

#include <boost/format.hpp>
#include <boost/test/tools/output_test_stream.hpp>

using namespace::with_state;

struct gumballmachine
{	
	gumballmachine()
		: m(2)
	{}
	boost::test_tools::output_test_stream strm;
	CGumballMachine m;
};

BOOST_FIXTURE_TEST_SUITE(Gumball_machine_with_state, gumballmachine)

	BOOST_AUTO_TEST_CASE(has_correct_state_after_creation)
	{
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for quarter
)"));
	}

	BOOST_AUTO_TEST_CASE(can_print_valid_inventory)
	{
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for quarter
)"));
		strm.str("");
		m.InsertQuarter();
		m.TurnCrank();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 1 gumball
Machine is waiting for quarter
)"));
	}

	BOOST_AUTO_TEST_CASE(do_nothing_when_turn_crank_without_quarter)
	{
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for quarter
)"));
	}

	BOOST_AUTO_TEST_CASE(when_no_quarter_cannot_eject_quarter)
	{
		m.EjectQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for quarter
)"));
	}

	BOOST_AUTO_TEST_CASE(can_take_quarter)
	{
		m.InsertQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for turn of crank
)"));
	}

	BOOST_AUTO_TEST_CASE(cannot_take_multiple_quarter)
	{
		m.InsertQuarter();
		m.InsertQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for turn of crank
)"));
	}

	BOOST_AUTO_TEST_CASE(can_eject_quarter_if_have_quarter)
	{
		m.InsertQuarter();
		m.EjectQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 2 gumballs
Machine is waiting for quarter
)"));
	}

	BOOST_AUTO_TEST_CASE(can_take_gumball_when_have_quarter)
	{
		m.InsertQuarter();
		m.TurnCrank();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 1 gumball
Machine is waiting for quarter
)"));
	}

	BOOST_AUTO_TEST_CASE(do_nothing_when_no_gumballs_inside)
	{
		m.InsertQuarter();
		m.TurnCrank();

		m.InsertQuarter();
		m.TurnCrank();

		m.InsertQuarter();
		m.TurnCrank();

		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016 (with state)
Inventory: 0 gumballs
Machine is sold out
)"));
	}
BOOST_AUTO_TEST_SUITE_END()
