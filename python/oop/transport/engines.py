"""
Engines module

Describes different types of engines
"""


class Engine:
    """
    Base engine class
    """
    def __init__(self, engine_name, engine_power, engine_type):
        self.engine_name = engine_name
        self.engine_power = engine_power
        self.engine_type = engine_type


class CarEngine(Engine):
    """
    Class for car engines
    """
    engine = 'Car engine'

    def __str__(self):
        return f'{self.engine}: {self.engine_name}, ' \
               f'power: {self.engine_power} c.u., type: {self.engine_type}'


class TrainEngine(Engine):
    """
    Class for train engines
    """
    engine = 'Train engine'

    def __str__(self):
        return f'{self.engine}: {self.engine_name}, ' \
               f'power: {self.engine_power} c.u., type: {self.engine_type}'


class ShipEngine(Engine):
    """
    Class for ship engines
    """
    engine = 'Ship engine'

    def __str__(self):
        return f'{self.engine}: {self.engine_name}, ' \
               f'power: {self.engine_power} c.u., type: {self.engine_type}'


class AirplaneEngine(Engine):
    """
    Class for airplane engines
    """
    engine = 'Airplane engine'

    def __init__(self, engine_name, engine_power, engine_type, engines_num):
        super().__init__(engine_name, engine_power, engine_type)
        self.engines_num = engines_num

    def __str__(self):
        return f'{self.engine}: {self.engine_name}, power: {self.engine_power} c.u., ' \
               f'type: {self.engine_type}, number: {self.engines_num}, ' \
               f'general power: {self.engine_power * self.engines_num} c.u.'
