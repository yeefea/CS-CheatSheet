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
