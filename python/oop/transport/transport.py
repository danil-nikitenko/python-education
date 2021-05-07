"""
A transport module

Describes different types of transport
"""
from abc import ABC, abstractmethod
import engines as e


class Transport(ABC):
    """
    Transport class

    Base class for different transport classes
    """
    total = 0

    def __init__(self, model, weight):
        self.model = model
        self.weight = weight
        Transport.total += 1

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.key() == other.key()

    def __hash__(self):
        return hash(self.key())

    def __bool__(self):
        return bool(self.weight)

    @property
    def model(self):
        """Get method"""
        return self._model

    @model.setter
    def model(self, new_model):
        """Set method"""
        if not new_model:
            raise ValueError('Vehicle model is missing')
        self._model = new_model

    @classmethod
    def total_vehicles(cls):
        """Returns the number of Transport objects"""
        print(f'Total vehicles: {cls.total}')

    @abstractmethod
    def move(self):
        """Launches transport"""

    @abstractmethod
    def key(self):
        """
        Returns key values.

        Required for __eq__ method
        """


class Car(Transport, e.CarEngine):
    """
    Car class

    Describes car. Parent class: Transport
    """
    transport = 'Car'

    def __init__(self, model, weight, manufacture_year,
                 max_speed, engine_name, engine_power, engine_type):
        super().__init__(model, weight)
        e.CarEngine.__init__(self, engine_name, engine_power, engine_type)
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed

    def __str__(self):
        return f'This is a {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} km/h, ' \
               f'weight: {self.weight} tons\n{super().__str__()}'

    def __del__(self):
        print(f'Car({self.model}) stopped')

    def key(self):
        return self.transport, self.model, self.manufacture_year

    def move(self):
        print(f'Car({self.model}) is moving')


class Train(Transport, e.TrainEngine):
    """
    Train class

    Describes train. Parent class: Car
    """
    transport = 'Train'

    def __init__(self, model, weight, manufacture_year,
                 max_speed, wagons_num, engine_name, engine_power, engine_type):
        super().__init__(model, weight)
        e.TrainEngine.__init__(self, engine_name, engine_power, engine_type)
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed
        self.wagons_num = wagons_num

    def __str__(self):
        return f'This is a {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} km/h, ' \
               f'wagons number: {self.wagons_num}, weight: {self.weight} tons\n' \
               f'{super().__str__()}'

    def __del__(self):
        print(f'Train({self.model}) stopped')

    def key(self):
        return self.transport, self.model, self.manufacture_year

    def move(self):
        print(f'Train({self.model}) is moving')


class Ship(Transport, e.ShipEngine):
    """
    Ship class

    Describes ship. Parent class: Car
    """
    transport = 'Ship'

    def __init__(self, model, weight, manufacture_year,
                 max_speed, ship_type, engine_name, engine_power, engine_type):
        super().__init__(model, weight)
        e.ShipEngine.__init__(self, engine_name, engine_power, engine_type)
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed
        self.ship_type = ship_type

    def __str__(self):
        return f'This is a {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} knots, ' \
               f'type: {self.ship_type}, weight: {self.weight} tons \n{super().__str__()}'

    def __del__(self):
        print(f'Ship({self.model}) stopped')

    def key(self):
        return self.transport, self.model, self.manufacture_year, self.ship_type

    def move(self):
        print(f'Ship({self.model}) is moving')

    @staticmethod
    def km_to_knots(kilometers):
        """Converts kilometers to knots"""
        return round(kilometers * 0.54, 2)


class Airplane(Transport, e.AirplaneEngine):
    """
    Airplane class

    Describes airplane. Parent class: Ship
    """
    transport = 'Airplane'

    def __init__(self, model, weight, manufacture_year, max_speed,
                 airplane_type, flight_range, engine_name, engine_power, engine_type, engines_num):
        super().__init__(model, weight)
        e.AirplaneEngine.__init__(self, engine_name, engine_power, engine_type, engines_num)
        self.manufacture_year = manufacture_year
        self.max_speed = max_speed
        self.airplane_type = airplane_type
        self.flight_range = flight_range

    def __str__(self):
        return f'This is an {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} km/h, ' \
               f'type: {self.airplane_type}, range: {self.flight_range}, ' \
               f'weight: {self.weight} tons\n{super().__str__()}'

    def __del__(self):
        print(f'Airplane({self.model}) stopped')

    def key(self):
        return self.transport, self.model, self.manufacture_year, self.airplane_type

    def move(self):
        print(f'Airplane({self.model}) is moving')


car = Car('CarModel', 2, 2000, 180, 'EngineName', 200, 'EngineType')
print(car)
car.move()
print()

train = Train('TrainModel', 100, 1994, 120, 5, 'EngineName', 2000, 'EngineType')
print(train)
train.move()
print()

ship = Ship('ShipModel', 1000, 2002, 17, 'Tanker', 'EngineName', 3000, 'EngineType')
print(ship)
ship.move()
print()

plane = Airplane('PlaneModel', 250, 2004, 945, 'Passenger', '9,700 to 15,840 km',
                 'EngineName', 2000, 'EngineType', 4)
print(plane)
plane.move()
print()

# сравнивает транспорт по его массе
print('train > car: ', train > car)
# сравнивает транспорт по параметрам transport, model, manufacture_year
print('car == plane: ', car == plane)
another_car = Car('CarModel', 3, 2000, 200, 'AnotherEngineName', 250, 'AnotherEngineType')
print('car == another_car: ', car == another_car)
# хеши одинаковых объектов равны
print('hash(car) == hash(plane): ', hash(car) == hash(plane))
print('hash(car) == hash(car): ', hash(car) == hash(car))
# bool() возвращает True если значение массы больше нуля
print('bool(car): ', bool(car))
# @classmethod, возвращает общее количество транспорта
Transport.total_vehicles()
# @staticmethod, переводит километры в морские узлы
print('60 km to knots:', Ship.km_to_knots(60))
print()
