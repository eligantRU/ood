#include "WeatherData.h"

class CSelfDestroyer : public CDisplay
{
public:
	CSelfDestroyer(CWeatherData& weatherData)
		: m_weatherData(weatherData)
	{}

	void Update(const SWeatherInfo& data) override
	{
		m_weatherData.RemoveObserver(*this);
	}

private:
	CWeatherData & m_weatherData;
};

class CMockDisplay : public IObserver<SWeatherInfo>
{
public:
	CMockDisplay(string id)
		: m_id(id)
	{}

private:
	void Update(SWeatherInfo const& data) override
	{
		cout << m_id << endl;
	}

	string m_id;
};

void TestSafeNotification()
{
	CWeatherData wd;
	CSelfDestroyer observer(wd);

	CDisplay display;
	
	wd.RegisterObserver(observer);
	
	wd.SetMeasurements(3, 0.7, 760);
}

void TestPrioritedNotifications()
{
	CWeatherData wd;

	CMockDisplay display1("display1");
	wd.RegisterObserver(display1, 2);

	CMockDisplay display2("display2");
	wd.RegisterObserver(display2);

	CMockDisplay display3("display3");
	wd.RegisterObserver(display3, 1);

	wd.SetMeasurements(3, 0.7, 760);

	wd.RemoveObserver(display2);

	wd.SetMeasurements(10, 0.8, 761);
}

int main()
{
	//TestSafeNotification();

	TestPrioritedNotifications();

	/*CWeatherData wd;

	CDisplay display;
	wd.RegisterObserver(display);

	CStatsDisplay statsDisplay;
	wd.RegisterObserver(statsDisplay);

	wd.SetMeasurements(3, 0.7, 760);
	wd.SetMeasurements(4, 0.8, 761);

	wd.RemoveObserver(statsDisplay);

	wd.SetMeasurements(10, 0.8, 761);
	wd.SetMeasurements(-10, 0.8, 761);*/
	return 0;
}