"""
模板方法模式
"""
class Game:

    def run(self):
        print('*' * 10, 'START', '*' * 10)
        self._initialize()
        self._start()
        self._end()
        print('*' * 10, 'END', '*' * 10)

    def _initialize(self):
        raise NotImplementedError

    def _start(self):
        raise NotImplementedError

    def _end(self):
        raise NotImplementedError


class RpgGame(Game):

    def _initialize(self):
        print('init RPG game, add scene, roles')

    def _start(self):
        print('start RPG game')

    def _end(self):
        print('end RPG game')

class Chess(Game):

    def _initialize(self):
        print('init checkerboard')
    
    def _start(self):
        print('start chess')
    
    def _end(self):
        print('end chess')

if __name__ == '__main__':
    game = RpgGame()
    game.run()
    game = Chess()
    game.run()

