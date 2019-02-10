class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance


class S(metaclass=Singleton):

    def __init__(self):
        print('init class S')


if __name__ == '__main__':
    for i in range(5):
        S()
