class DrawAPI:
    def draw_circle(self, x, y, radius, rgba):
        raise NotImplementedError


class Plot2D(DrawAPI):
    def draw_circle(self, x, y, radius, rgba):
        print(f'draw circle using matplotlib with color {rgba}')


class Render3D(DrawAPI):
    def draw_circle(self, x, y, radius, rgba):
        print(f'draw circle using OpenGL with color {rgba}')


class Shape:
    def __init__(self, draw_api):
        self.draw_api = draw_api


class Circle(Shape):
    def __init__(self, x, y, radius, rgba, draw_api):
        super().__init__(draw_api)
        self.x = x
        self.y = y
        self.radius = radius
        self.rgba = rgba

    def draw(self):
        self.draw_api.draw_circle(self.x, self.y, self.radius, self.rgba)


plot = Plot2D()
render = Render3D()
red_circle = Circle(0, 0, 1, '#ff0000', plot)
green_circel = Circle(1, 1, 3, '#00ff00', render)
red_circle.draw()
green_circel.draw()
red_circle.draw_api = render
red_circle.draw()
