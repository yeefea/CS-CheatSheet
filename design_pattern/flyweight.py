class ColoredPoint:

    def __init__(self, color):
        """

        :param color: shared state
        """
        self.color = color

    def draw(self, x, y):
        """

        :param x: unshared state
        :param y:
        :return:
        """
        print('draw a point at ({},{}) with color {}'.format(x, y, self.color))


class ColoredPointFactory:
    def __init__(self):
        self._color_map = {}

    def get_point(self, color):
        if color in self._color_map:
            ret = self._color_map[color]
        else:
            print('init new point with color {}'.format(color))
            ret = ColoredPoint(color)
            self._color_map[color] = ret
        return ret


if __name__ == '__main__':
    red = '#ff0000'
    yellow = '#ffff00'
    point_factory = ColoredPointFactory()
    p_red = point_factory.get_point(red)
    p_red.draw(1, 1)
    p_red.draw(2, 4)
    p_red.draw(3, 9)
    point_factory.get_point(red).draw(4, 16)

    point_factory.get_point(yellow).draw(1, 1)
    p_yellow = point_factory.get_point(yellow)
    p_yellow.draw(2, 2)
    p_yellow.draw(3, 3)
    p_yellow.draw(4, 4)
