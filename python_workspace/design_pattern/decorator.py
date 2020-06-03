import time

# from functools import wraps
# wrappers are more Pythonic!


class Subject:

    def run(self):
        print('sleep 1s')
        time.sleep(1)


class TimingDecorator(Subject):

    def __init__(self, subject):
        super().__init__()
        self._subject = subject

    def run(self):
        t0 = time.time()
        super().run()
        t1 = time.time()
        print('time elapsed: {}'.format(t1 - t0))


if __name__ == '__main__':
    subject = TimingDecorator(Subject())
    subject.run()
