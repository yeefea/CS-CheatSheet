class CarElement:
    def accept(self, visitor):
        raise NotImplementedError()


class Engine(CarElement):
    def accept(self, visitor):
        visitor.visit_engine(self)


class Wheel(CarElement):
    def accept(self, visitor):
        visitor.visit_wheel(self)

class Car(CarElement):
    def __init__(self):
        self.elements = [
            Wheel(), Wheel(),
            Wheel(), Wheel(),
            Engine()
        ]

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)
        visitor.visit_car(self)

class CarElementVisitor:

    def visit_engine(self, engine):
        raise NotImplementedError()

    def visit_wheel(self, wheel):
        raise NotImplementedError()

    def visit_car(self, car):
        raise NotImplementedError()

class CarElementDoVisitor(CarElementVisitor):

    def visit_car(self, car):
        print("Starting my car.")
    def visit_wheel(self, wheel):
        print("Kicking my wheel.")
    def visit_engine(self, engine):
        print("Starting my engine.")


class CarElementPrintVisitor(CarElementVisitor):

    def visit_car(self, car):
        print("Visiting car.")
    def visit_wheel(self, wheel):
        print("Visiting wheel.")
    def visit_engine(self, engine):
        print("Visiting engine.")


if __name__ == '__main__':
    car = Car()
    car.accept(CarElementPrintVisitor())
    car.accept(CarElementDoVisitor())
