#include "stdafx.h"

#include "../gumball_machine/NaiveGumBallMachine.h"

#include <boost/format.hpp>
#include <boost/test/tools/output_test_stream.hpp>

struct NaiveGumballMachine
{
	NaiveGumballMachine()
		: m(2)
	{
	}
	boost::test_tools::output_test_stream strm;
	naive::CGumballMachine m;
};

BOOST_FIXTURE_TEST_SUITE(Naive_gumball_machine, NaiveGumballMachine)

	BOOST_AUTO_TEST_CASE(has_correct_state_after_creation)
	{
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for quarter
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(can_print_valid_inventory)
	{
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for quarter
Money: 0
)"));
		strm.str("");
		m.InsertQuarter();
		m.TurnCrank();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 1 gumball
Machine is waiting for quarter
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(do_nothing_when_turn_crank_without_quarter)
	{
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for quarter
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(when_no_quarter_cannot_eject_quarter)
	{
		m.EjectQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for quarter
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(can_take_quarter)
	{
		m.InsertQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for turn of crank
Money: 1
)"));
	}

	BOOST_AUTO_TEST_CASE(cannot_take_quarter_if_no_gumbolls)
	{
		m.InsertQuarter();
		m.TurnCrank();

		m.InsertQuarter();
		m.TurnCrank();

		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 0 gumballs
Machine is sold out
Money: 0
)"));

		m.InsertQuarter();
		strm.clear();

		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 0 gumballs
Machine is sold out
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(can_take_multiple_quarters)
	{
		m.InsertQuarter();
		m.InsertQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for turn of crank
Money: 2
)"));
	}

	BOOST_AUTO_TEST_CASE(cannot_take_more_than_two_quarters)
	{
		m.InsertQuarter();
		m.InsertQuarter();
		m.InsertQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for turn of crank
Money: 2
)"));
	}

	BOOST_AUTO_TEST_CASE(can_eject_multiple_quarters_if_have_quarters)
	{
		m.InsertQuarter();
		m.InsertQuarter();
		m.EjectQuarter();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 2 gumballs
Machine is waiting for quarter
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(can_take_gumball_when_have_quarter)
	{
		m.InsertQuarter();
		m.InsertQuarter();
		m.TurnCrank();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 1 gumball
Machine is waiting for turn of crank
Money: 1
)"));
		strm.clear();
		m.TurnCrank();
		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 0 gumballs
Machine is sold out
Money: 0
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
Inventory: 0 gumballs
Machine is sold out
Money: 0
)"));
	}

	BOOST_AUTO_TEST_CASE(can_eject_quarters_if_no_gumballs)
	{
		m.InsertQuarter();
		m.InsertQuarter();
		m.TurnCrank();
		m.InsertQuarter();
		m.TurnCrank();
		m.EjectQuarter();

		strm << m.ToString();
		BOOST_CHECK(strm.is_equal(R"(
Inventory: 0 gumballs
Machine is sold out
Money: 0
)"));
	}
BOOST_AUTO_TEST_SUITE_END()
