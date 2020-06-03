from abc import ABCMeta, abstractmethod


class AbstractMazeFactory(metaclass=ABCMeta):

    @abstractmethod
    def make_maze(self):
        pass

    @abstractmethod
    def make_wall(self):
        pass

    @abstractmethod
    def make_room(self, n):
        pass

    @abstractmethod
    def make_door(self, room1, room2):
        pass


class Maze:
    def render(self):
        print('rendering a maze')


class EnchantedMaze(Maze):
    def render(self):
        print('rendering an enchanted maze')


class Wall:
    pass


class Room:
    pass


class EnchantedRoom(Room):
    pass


class Door:
    pass


class MazeFactory(AbstractMazeFactory):

    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall

    def make_room(self, n):
        return Room

    def make_door(self, room1, room2):
        return Door


class EnchantedMazeFactory(MazeFactory):

    def make_maze(self):
        return EnchantedMaze()

    def make_room(self, n):
        return EnchantedRoom()


if __name__ == '__main__':
    enchanted_factory = EnchantedMazeFactory()
    enchanted_maze = enchanted_factory.make_maze()
    enchanted_maze.render()
