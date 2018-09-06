#include <cassert>
#include <functional>
#include <iostream>
#include <memory>
#include <vector>

using namespace std;

namespace
{

function<void()> GetQuackBehavior()
{
	return [] {
		cout << "Quack Quack!!!" << endl;
	};
}

function<void()> GetSqueakBehavior()
{
	return [] {
		cout << "Squeek!!!" << endl;
	};
}

function<void()> GetMuteQuackBehavior()
{
	return [] {};
}
	
function<void()> GetWaltzDanceBehavior()
{
	return [] {
		cout << "I'm dancing waltz" << endl;
	};
}

function<void()> GetMinuetDanceBehavior()
{
	return [] {
		cout << "I'm dancing minuet" << endl;
	};
}

function<void()> GetNoDanceBehavior()
{
	return [] {};
}

function<void()> GetFlyWithWings()
{
	uint64_t m_flightsCount = 0;
	return [=] () mutable {
		cout << "I'm flying with wings!! [" << ++m_flightsCount << "]" << endl;
	};
}

function<void()> GetFlyNoWay()
{
	return [] {};
}

} // namespace

class Duck
{
public:
	Duck(function<void()>&& flyBehaviorFn,
		function<void()>&& quackBehaviorFn,
		function<void()>&& danceBehaviorFn)
		: m_quackBehaviorFn(move(quackBehaviorFn))
		, m_danceBehaviorFn(move(danceBehaviorFn))
	{
		SetFlyBehavior(move(flyBehaviorFn));
	}
	void Quack() const
	{
		m_quackBehaviorFn();
	}
	void Swim()
	{
		cout << "I'm swimming" << endl;
	}
	void Fly()
	{
		m_flyBehaviorFn();
	}
	void Dance()
	{
		m_danceBehaviorFn();
	}
	void SetFlyBehavior(function<void()>&& flyBehaviorFn)
	{
		m_flyBehaviorFn = move(flyBehaviorFn);
	}
	virtual void Display() const = 0;
	virtual ~Duck() = default;

private:
	function<void()> m_flyBehaviorFn;
	function<void()> m_quackBehaviorFn;
	function<void()> m_danceBehaviorFn;
};

class MallardDuck : public Duck
{
public:
	MallardDuck()
		: Duck(GetFlyWithWings(), GetQuackBehavior(), GetWaltzDanceBehavior())
	{
	}

	void Display() const override
	{
		cout << "I'm mallard duck" << endl;
	}
};

class RedheadDuck : public Duck
{
public:
	RedheadDuck()
		: Duck(GetFlyWithWings(), GetQuackBehavior(), GetMinuetDanceBehavior())
	{
	}
	void Display() const override
	{
		cout << "I'm redhead duck" << endl;
	}
};
class DecoyDuck : public Duck
{
public:
	DecoyDuck()
		: Duck(GetFlyNoWay(), GetMuteQuackBehavior(), GetNoDanceBehavior())
	{
	}
	void Display() const override
	{
		cout << "I'm decoy duck" << endl;
	}
};
class RubberDuck : public Duck
{
public:
	RubberDuck()
		: Duck(GetFlyNoWay(), GetSqueakBehavior(), GetNoDanceBehavior())
	{
	}
	void Display() const override
	{
		cout << "I'm rubber duck" << endl;
	}
};

class ModelDuck : public Duck
{
public:
	ModelDuck()
		: Duck(GetFlyNoWay(), GetQuackBehavior(), GetNoDanceBehavior())
	{
	}
	void Display() const override
	{
		cout << "I'm model duck" << endl;
	}
};

void DrawDuck(Duck const& duck)
{
	duck.Display();
}

void PlayWithDuck(Duck& duck)
{
	DrawDuck(duck);
	duck.Quack();
	duck.Fly();
	duck.Dance();
	cout << endl;
}

void main()
{
	MallardDuck mallarDuck;
	PlayWithDuck(mallarDuck);

	RedheadDuck redheadDuck;
	PlayWithDuck(redheadDuck);

	RubberDuck rubberDuck;
	PlayWithDuck(rubberDuck);

	DecoyDuck decoyDuck;
	PlayWithDuck(decoyDuck);

	ModelDuck modelDuck;
	PlayWithDuck(modelDuck);
	modelDuck.SetFlyBehavior(GetFlyWithWings());
	PlayWithDuck(modelDuck);
	PlayWithDuck(modelDuck);
	modelDuck.SetFlyBehavior(GetFlyWithWings());
	PlayWithDuck(modelDuck);
}
