#pragma once

#include <set>
#include <map>
#include <functional>

/*
Шаблонный интерфейс IObserver. Его должен реализовывать класс, 
желающий получать уведомления от соответствующего IObservable
Параметром шаблона является тип аргумента,
передаваемого Наблюдателю в метод Update
*/
template <typename T>
class IObserver
{
public:
	virtual void Update(T const& data) = 0;
	virtual ~IObserver() = default;
};

/*
Шаблонный интерфейс IObservable. Позволяет подписаться и отписаться на оповещения, а также
инициировать рассылку уведомлений зарегистрированным наблюдателям.
*/
template <typename T>
class IObservable
{
public:
	virtual ~IObservable() = default;
	virtual void RegisterObserver(IObserver<T> & observer, size_t priority) = 0;
	virtual void NotifyObservers() = 0;
	virtual void RemoveObserver(IObserver<T> & observer) = 0;
};

// Реализация интерфейса IObservable
template <class T>
class CObservable : public IObservable<T>
{
public:
	typedef IObserver<T> ObserverType;

	void RegisterObserver(ObserverType & observer, size_t priority = 0) override
	{
		m_observers[priority].insert(&observer);
		m_priorities[&observer] = priority;
	}

	void NotifyObservers() override
	{
		T data = GetChangedData();
		auto clone(m_observers);
		for (auto & [priority, observers] : clone)
		{
			for (auto & observer : observers)
			{
				observer->Update(data);
			}
		}
	}

	void RemoveObserver(ObserverType & observer) override
	{
		auto priority = m_priorities[&observer];
		m_observers[priority].erase(&observer);
		if (m_observers[priority].empty())
		{
			m_observers.erase(priority);
		}
		m_priorities.erase(m_priorities.find(&observer));
	}

protected:
	// Классы-наследники должны перегрузить данный метод, 
	// в котором возвращать информацию об изменениях в объекте
	virtual T GetChangedData()const = 0;

private:
	std::map<size_t, std::set<ObserverType *>> m_observers;
	std::map<ObserverType*, size_t> m_priorities;
};
