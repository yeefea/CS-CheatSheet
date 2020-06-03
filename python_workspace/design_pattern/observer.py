"""
观察者模式定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象。
这个主题对象在状态发生变化时，会通知所有观察者对象，使它们能够自动更新自己。
1.避免循环引用。 
2.如果顺序执行，某一观察者错误会导致系统卡壳，一般采用异步方式。
"""

class Observer:

    def update(self, subject):
        raise NotImplementedError


class Subject(object):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self.observers:
            if modifier != observer:
                observer.update(self)


class Boardcast(Subject):

    def __init__(self):
        super().__init__()
        self.msg = None

    def send_message(self, msg):
        self.msg = msg
        self.notify(self)


class Listener(Observer):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, subject):
        print(f'Listener {self.name} received new message: {subject.msg}')


if __name__ == '__main__':
    john = Listener('John')
    david = Listener('David')
    boardcast = Boardcast()
    boardcast.attach(john)
    boardcast.attach(david)
    boardcast.send_message('Happy new year!')
    boardcast.send_message('Hahahahaha!')
