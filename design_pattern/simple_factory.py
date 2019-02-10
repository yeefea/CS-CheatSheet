class Circle:

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        print('draw a circle at ({},{}) with color {}'.format(self.x, self.y, self.color))


class CircleFactory:
    """
    简单工厂不符合开闭原则，添加新产品需要修改工厂类
    """

    @classmethod
    def get_red_circle(cls):
        return Circle(0, 0, 1, '#ff0000')

    @classmethod
    def get_green_circle(cls):
        return Circle(0, 0, 1, '#00ff00')

    @classmethod
    def get_blue_circle(cls):
        return Circle(0, 0, 1, '#0000ff')


if __name__ == '__main__':
    red_circle = CircleFactory.get_red_circle()
    blue_circle = CircleFactory.get_blue_circle()
    red_circle.draw()
    blue_circle.draw()
