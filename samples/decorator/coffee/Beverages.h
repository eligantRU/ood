#pragma once

#include "IBeverage.h"

// Базовая реализация напитка, предоставляющая его описание
class CBeverage : public IBeverage
{
public:
	CBeverage(const std::string& description)
		: m_description(description)
	{
	}

	std::string GetDescription() const override final
	{
		return m_description;
	}

private:
	std::string m_description;
};

// Кофе
class CCoffee : public CBeverage
{
public:
	CCoffee(const std::string& description = "Coffee")
		: CBeverage(description)
	{
	}

	double GetCost() const override
	{
		return 60;
	}
};

// Капуччино
class CCapuccino : public CCoffee
{
public:
	CCapuccino()
		: CCoffee("Capuccino")
	{
	}

	double GetCost() const override
	{
		return 80;
	}
};

class CDoubleCapuccino : public CCoffee
{
public:
	CDoubleCapuccino()
		: CCoffee("Double capuccino")
	{
	}

	double GetCost() const override
	{
		return 120;
	}
};

// Латте
class CLatte : public CCoffee
{
public:
	CLatte()
		: CCoffee("Latte")
	{
	}

	double GetCost() const override
	{
		return 90;
	}
};

class CDoubleLatte : public CCoffee
{
public:
	CDoubleLatte()
		: CCoffee("Double latte")
	{
	}

	double GetCost() const override
	{
		return 130;
	}
};

// Чай
class CTea : public CBeverage
{
public:
	CTea(const std::string& description = "Tea")
		: CBeverage(description)
	{
	}

	double GetCost() const override
	{
		return 30;
	}
};

class CRedTea : public CTea
{
public:
	CRedTea()
		: CTea("Red tea")
	{
	}

	double GetCost() const override
	{
		return 30;
	}
};

class CGreenTea : public CTea
{
public:
	CGreenTea()
		: CTea("Green tea")
	{
	}

	double GetCost() const override
	{
		return 30;
	}
};

class CBlackTea : public CTea
{
public:
	CBlackTea()
		: CTea("Black tea")
	{
	}

	double GetCost() const override
	{
		return 30;
	}
};

class CYellowTea : public CTea
{
public:
	CYellowTea()
		: CTea("Yellow tea")
	{
	}

	double GetCost() const override
	{
		return 30;
	}
};

// Молочный коктейль
class CMilkshake : public CBeverage
{
public:
	CMilkshake(const std::string& description = "Milkshake")
		: CBeverage(description)
	{
	}

	double GetCost() const override
	{
		return 80;
	}
};

class CSmallMilkshake : public CMilkshake
{
public:
	CSmallMilkshake()
		: CMilkshake("Small milkshake")
	{
	}

	double GetCost() const override
	{
		return 50;
	}
};

class CMediumMilkshake : public CMilkshake
{
public:
	CMediumMilkshake()
		: CMilkshake("Medium milkshake")
	{
	}

	double GetCost() const override
	{
		return 60;
	}
};

class CLargeMilkshake : public CMilkshake
{
public:
	CLargeMilkshake()
		: CMilkshake("Large milkshake")
	{
	}

	double GetCost() const override
	{
		return 80;
	}
};
