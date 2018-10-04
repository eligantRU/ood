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

void TestSafeNotification()
{
	CWeatherData wd;
	CSelfDestroyer observer(wd);

	CDisplay display;
	
	wd.RegisterObserver(observer);
	
	wd.SetMeasurements(3, 0.7, 760);
}

int main()
{
	TestSafeNotification();

	CWeatherData wd;

	CDisplay display;
	wd.RegisterObserver(display);

	CStatsDisplay statsDisplay;
	wd.RegisterObserver(statsDisplay);

	wd.SetMeasurements(3, 0.7, 760);
	wd.SetMeasurements(4, 0.8, 761);

	wd.RemoveObserver(statsDisplay);

	wd.SetMeasurements(10, 0.8, 761);
	wd.SetMeasurements(-10, 0.8, 761);
	return 0;
}