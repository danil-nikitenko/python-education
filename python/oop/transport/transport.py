"""
A transport module

Describes different types of transport
"""


class Transport:
    """
    Transport class

    Base class for different transport class
    """
    def __init__(self, manufacture_year):
        self.manufacture_year = manufacture_year


class Car(Transport):
    """
    Car class

    Describes car. Parent class: Transport
    """
    transport = 'Car'

    def __init__(self, manufacture_year, model, max_speed):
        super().__init__(manufacture_year)
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return f'This is a {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} km/h'


class Train(Car):
    """
    Train class

    Describes train. Parent class: Car
    """
    transport = 'Train'

    def __init__(self, manufacture_year, model, max_speed, wagons_num):
        super().__init__(manufacture_year, model, max_speed)
        self.wagons_num = wagons_num

    def __str__(self):
        return f'This is a {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} km/h, ' \
               f'wagons number: {self.wagons_num}'


class Ship(Car):
    """
    Ship class

    Describes ship. Parent class: Car
    """
    transport = 'Ship'

    def __init__(self, manufacture_year, model, max_speed, type):
        super().__init__(manufacture_year, model, max_speed)
        self.type = type

    def __str__(self):
        return f'This is a {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} knots, type: {self.type}'


class Airplane(Ship):
    """
    Airplane class

    Describes airplane. Parent class: Ship
    """
    transport = 'Airplane'

    def __init__(self, manufacture_year, model, max_speed, type, range):
        super().__init__(manufacture_year, model, max_speed, type)
        self.range = range

    def __str__(self):
        return f'This is an {self.transport}, model: {self.model}, manufacture year: ' \
               f'{self.manufacture_year}, maximum speed: {self.max_speed} km/h, ' \
               f'type: {self.type}, range: {self.range}'


car = Car(2000, 'CarModel', 180)
print(car, '\n')

train = Train(1994, 'TrainModel', 120, 25)
print(train, '\n')

ship = Ship(2002, 'ShipModel', 17, 'Tanker')
print(ship, '\n')

plane = Airplane(2004, 'PlaneModel', 945, 'Passenger', '9,700 to 15,840 km')
print(plane)
