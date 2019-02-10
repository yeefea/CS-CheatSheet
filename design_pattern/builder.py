from abc import abstractmethod


class Car:
    def __init__(self, wheels=4, seats=4, color='Black'):
        self.wheels = wheels
        self.seats = seats
        self.color = color

    def __str__(self):
        return 'Car(wheels={},seats={},color={})'.format(
            self.wheels, self.seats, self.color)


class Builder:

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_seats(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def build(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value
        return self

    def set_seats(self, value):
        self.car.seats = value
        return self

    def set_color(self, value):
        self.car.color = value
        return self

    def build(self):
        return self.car


class CarBuilderDirector(object):
    @staticmethod
    def construct():
        builder = CarBuilder()
        builder.set_wheels(8)
        builder.set_seats(4)
        builder.set_color('Red')
        return builder.build()


if __name__ == '__main__':
    car = CarBuilderDirector.construct()
    print(car)
