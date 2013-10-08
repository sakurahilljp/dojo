
# Subject abstract class
class Subject(object):
    def __init__(self):
        self.observers = []

    def add_observer(self, obj):
        if obj not in self.observers:
            self.observers.append(obj) 

    def remove_observer(self, obj):
        if obj in self.observers:
            self.observers.remove(obj)
    
    def notify(self):
        protocol = self.create_protocol()
        for obj in self.observers:
            obj.update( protocol )

    def create_protocol(self):
        raise 0, 'must be implemented.'

# Observer abstract class
class Observer(object):
    def __init__(self):
        pass
    def update(self, protocol):
        raise 0, 'must be implemented'

# base class for Display
class DisplayElement(Observer):
    def update(self, protocol):
        self.display(protocol)

    def display(self, protocol):
        raise 0, 'must be implemented'

class WeatherData(Subject):
    def __init__(self):
        Subject.__init__(self)

        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()

    def create_protocol(self):
        return { "temperature": self.temperature,
                 "humidity": self.humidity,
                 "pressure": self.pressure }

class CurrentConditionDisplay(DisplayElement):
    def display(self, protocol):
        print ''
        print '*** Current Condition Display ***'
        print '  Temperature: %s deg C' % protocol['temperature']
        print '  Humidity:  : %s %%' % protocol['humidity']
        print '  Pressure:  : %s atm' % protocol['pressure']
        print ''

class ForecastDisplay(DisplayElement):
    def display(self, protocol):

        if protocol['temperature'] > 35:
            forecast = 'hot'
        elif protocol['temperature'] < 15:
            forecast = 'cold'
        else:
            forecast = "warm"

        print ''
        print "*** ForecastDisplay ***"
        print ''
        print '  It will be "%s" tommorow.' % forecast
        print ''

if __name__ == '__main__':
    weather = WeatherData()
    currentDisplay = CurrentConditionDisplay()
    forcastDisplay = ForecastDisplay()

    observers = [currentDisplay, forcastDisplay]

    for obj in observers:
        weather.add_observer(obj)

    print '\n>>> Updating Weather Data...'
    weather.set_measurements( 36, 36, 1.01 )

    print '\n>>> Updating Weather Data...'
    weather.set_measurements( 10, 36, 1.01 )

    print '\n>>> Updating Weather Data...'
    weather.set_measurements( 26, 36, 1.01 )

    for obj in observers:
        weather.remove_observer(obj)
