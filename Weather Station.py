from typing import List


class Observer:
    def update(self, temp, humidity, pressure):
        pass


class Subject:

    def registerObserver(self, o:Observer):
        pass

    def removeObserver(self, o:Observer):
        pass

    def notifyObserver(self):
        pass


class DisplayElement:

    def display(self):
        pass


class WeatherData(Subject):

    def __init__(self):
        self.observers: List[Observer] = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def registerObserver(self, o: Observer):
        self.observers.append(o)

    def removeObserver(self, o: Observer):
        i = self.observers.index(o)
        if i >= 0:
            self.observers.remove(o)

    def notifyObserver(self):
        for obs in self.observers:
            obs.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObserver()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentConditionsDisplay(DisplayElement, Observer):
    def __init__(self, weatherData: Subject):
        self.temperature: float = 0
        self.humidity: float = 0
        self.pressure: float = 0

        self.weatherData: Subject = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity")

class MyDisplay(DisplayElement, Observer):
    def __init__(self, weatherData: Subject):
        self.temperature: float = 0
        self.humidity: float = 0
        self.pressure: float = 0

        self.weatherData: Subject = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current pressure: " + str(self.pressure))


class WeatherStation:
    weatherData: WeatherData = WeatherData()
    currentDisplay: CurrentConditionsDisplay = CurrentConditionsDisplay(weatherData)
    myDisplay = MyDisplay(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)


if __name__ == "__main__":
    WeatherStation = WeatherStation()
