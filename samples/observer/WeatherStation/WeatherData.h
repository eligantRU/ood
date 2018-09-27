#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <climits>
#include "Observer.h"

using namespace std;

class CStats
{
public:
	double GetMin() const
	{
		return m_minValue;
	}

	double GetMax() const
	{
		return m_maxValue;
	}

	void AddValue(double value)
	{
		m_minValue = std::min(m_minValue, value);
		m_maxValue = std::max(m_maxValue, value);

		m_accValue += value;
		++m_countAcc;
	}

	double GetAverage() const
	{
		return m_accValue / m_countAcc;
	}

private:
	double m_minValue = std::numeric_limits<double>::infinity();
	double m_maxValue = -std::numeric_limits<double>::infinity();
	double m_accValue = 0;
	unsigned m_countAcc = 0;
};

void PrintStats(ostream& stream, const CStats& stats, const string& index)
{
	stream << "Max " << index << " " << stats.GetMax() << endl;
	stream << "Min " << index << " " << stats.GetMin() << endl;
	stream << "Average " << index << " " << stats.GetAverage() << endl;
	stream << "----------------" << endl;
}

struct SWeatherInfo
{
	double temperature = 0;
	double humidity = 0;
	double pressure = 0;
};

class CDisplay: public IObserver<SWeatherInfo>
{
private:
	/* Метод Update сделан приватным, чтобы ограничить возможность его вызова напрямую
		Классу CObservable он будет доступен все равно, т.к. в интерфейсе IObserver он
		остается публичным
	*/
	void Update(SWeatherInfo const& data) override
	{
		cout << "Current Temp " << data.temperature << endl;
		cout << "Current Hum " << data.humidity << endl;
		cout << "Current Pressure " << data.pressure << endl;
		cout << "----------------" << endl;
	}
};

class CStatsDisplay : public IObserver<SWeatherInfo>
{
private:
	/* Метод Update сделан приватным, чтобы ограничить возможность его вызова напрямую
	Классу CObservable он будет доступен все равно, т.к. в интерфейсе IObserver он
	остается публичным
	*/
	void Update(SWeatherInfo const& data) override
	{
		m_tempStat.AddValue(data.temperature);
		m_humidityStat.AddValue(data.humidity);
		m_pressureStat.AddValue(data.pressure);

		PrintStats(std::cout, m_tempStat, "Temp");
		PrintStats(std::cout, m_humidityStat, "Humidity");
		PrintStats(std::cout, m_pressureStat, "Pressure");
	}

	CStats m_tempStat;
	CStats m_humidityStat;
	CStats m_pressureStat;
};

class CWeatherData : public CObservable<SWeatherInfo>
{
public:
	// Температура в градусах Цельсия
	double GetTemperature()const
	{
		return m_temperature;
	}
	// Относительная влажность (0...100)
	double GetHumidity()const
	{
		return m_humidity;
	}
	// Атмосферное давление (в мм.рт.ст)
	double GetPressure()const
	{
		return m_pressure;
	}

	void MeasurementsChanged()
	{
		NotifyObservers();
	}

	void SetMeasurements(double temp, double humidity, double pressure)
	{
		m_humidity = humidity;
		m_temperature = temp;
		m_pressure = pressure;

		MeasurementsChanged();
	}
protected:
	SWeatherInfo GetChangedData()const override
	{
		SWeatherInfo info;
		info.temperature = GetTemperature();
		info.humidity = GetHumidity();
		info.pressure = GetPressure();
		return info;
	}
private:
	double m_temperature = 0.0;
	double m_humidity = 0.0;	
	double m_pressure = 760.0;	
};
