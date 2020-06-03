"""
原型模式
"""
import copy

class Circle:

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def __copy__(self):
        return Circle(self.x, self.y, self.radius, self.color)
    
    def __deepcopy__(self):
        return Circle(self.x, self.y, self.radius, self.color)

    def __str__(self):
        return 'Circle({},{},{},{})'.format(self.x, self.y, self.radius, self.color)

if __name__ == '__main__':

    proto_circle = Circle(1, 1, 1, '#ff0000')
    circles = []
    
    for i in range(10):
        tmp = copy.copy(proto_circle)
        tmp.x += i
        tmp.y -= i
        circles.append(tmp)
    
    for c in circles:
        print(c)

    