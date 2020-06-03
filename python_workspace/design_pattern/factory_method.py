class Shape:
    TYPE = 'shape'

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    TYPE = 'circle'

    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print('rendering a circle')


class Square(Shape):
    TYPE = 'square'

    def __init__(self, x, y, length):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length

    def draw(self):
        print('rendering a square')


class ShapeFactory:
    """
    符合开闭原则，需要新增产品时继承ShapeFactory类，不需要修改
    """

    def get_shape(self):
        """
        工厂方法
        :return:
        """
        pass


class CircleFactory(ShapeFactory):
    def get_shape(self):
        return Circle(0, 0, 1)


class SquareFactory(ShapeFactory):

    def get_shape(self):
        return Square(0, 0, 1)


if __name__ == '__main__':
    circle_factory = CircleFactory()
    square_factory = SquareFactory()
    c = circle_factory.get_shape()
    s = square_factory.get_shape()
    c.draw()
    s.draw()
