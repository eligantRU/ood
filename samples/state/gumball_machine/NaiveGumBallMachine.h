#pragma once

#include <boost/format.hpp>
#include <iostream>

namespace naive
{
class CGumballMachine
{
public:
	const size_t MAX_MONEY = 2;

	enum class State
	{
		SoldOut, // Жвачка закончилась
		NoQuarter, // Нет монетки
		HasQuarter, // Есть монетка
		Sold, // Монетка выдана
	};

	CGumballMachine(unsigned count)
		: m_count(count)
		, m_state(count > 0 ? State::NoQuarter : State::SoldOut)
	{
	}

	void InsertQuarter()
	{
		using namespace std;
		switch (m_state)
		{
		case State::SoldOut:
			cout << "You can't insert a quarter, the machine is sold out\n";
			break;
		case State::NoQuarter:
			InsertQuarterImpl();
			m_state = State::HasQuarter;
			break;
		case State::HasQuarter:
			if (m_money == MAX_MONEY)
			{
				cout << "You can't insert another quarter\n";
			}
			else
			{
				InsertQuarterImpl();
			}
			break;
		case State::Sold:
			cout << "Please wait, we're already giving you a gumball\n";
			break;
		}
	}

	void EjectQuarter()
	{
		using namespace std;
		switch (m_state)
		{
		case State::HasQuarter:
			cout << "Quarter returned\n";
			m_money = 0;
			m_state = State::NoQuarter;
			break;
		case State::NoQuarter:
			cout << "You haven't inserted a quarter\n";
			break;
		case State::Sold:
			cout << "Sorry you already turned the crank\n";
			break;
		case State::SoldOut:
			if (m_money)
			{
				m_money = 0;
				cout << "You eject all quarters" << endl;
			}
			else
			{
				cout << "You can't eject, you haven't inserted a quarter yet\n";
			}
			break;
		}
	}

	void TurnCrank()
	{
		using namespace std;
		switch (m_state)
		{
		case State::SoldOut:
			cout << "You turned but there's no gumballs\n";
			break;
		case State::NoQuarter:
			cout << "You turned but there's no quarter\n";
			break;
		case State::HasQuarter:
			cout << "You turned...\n";
			m_state = State::Sold;
			Dispense();
			break;
		case State::Sold:
			cout << "Turning twice doesn't get you another gumball\n";
			break;
		}
	}

	void Refill(unsigned numBalls)
	{
		m_count = numBalls;
		m_state = numBalls > 0 ? State::NoQuarter : State::SoldOut;
	}

	std::string ToString() const
	{
		std::string state = (m_state == State::SoldOut) ? "sold out" : (m_state == State::NoQuarter) ? "waiting for quarter" : (m_state == State::HasQuarter) ? "waiting for turn of crank" : "delivering a gumball";

		/*
Mighty Gumball, Inc.
C++-enabled Standing Gumball Model #2016
		*/

		auto fmt = boost::format(R"(
Inventory: %1% gumball%2%
Machine is %3%
Money: %4%
)");
		return (fmt % m_count % (m_count != 1 ? "s" : "") % state % m_money).str();
	}

private:
	void InsertQuarterImpl()
	{
		if (m_money == MAX_MONEY)
		{
			std::cout << "You cannot insert more than " << MAX_MONEY << "quarter(s)" << std::endl;
			return;
		}
		++m_money;

		using namespace ::std;
		cout << "You inserted the " << m_money << "__ quarter" << endl;
	}

	void Dispense()
	{
		using namespace std;
		switch (m_state)
		{
		case State::Sold:
			cout << "A gumball comes rolling out the slot\n";
			--m_count;
			--m_money;
			if (m_count == 0)
			{
				cout << "Oops, out of gumballs\n";
				m_state = State::SoldOut;
			}
			else
			{
				m_state = m_money ? State::HasQuarter : State::NoQuarter;
			}
			break;
		case State::NoQuarter:
			cout << "You need to pay first\n";
			break;
		case State::SoldOut:
		case State::HasQuarter:
			cout << "No gumball dispensed\n";
			break;
		}
	}

	unsigned m_count; // Количество шариков
	unsigned m_money = 0;
	State m_state = State::SoldOut;
};
} // namespace naive
