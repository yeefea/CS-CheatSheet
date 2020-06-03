from threading import Thread, Condition, Lock, Semaphore

atomic_counter = 0
counter_lk = Lock()


def atomic_inc():
    global atomic_counter
    counter_lk.acquire()
    atomic_counter += 1
    counter_lk.release()


def worker(n):
    for i in range(n):
        atomic_inc()


def demo_lock():
    global atomic_counter
    th1 = Thread(target=worker, args=(100000,))
    th2 = Thread(target=worker, args=(100000,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(atomic_counter)


def demo_cv():
    pass


def demo_sem():
    pass


if __name__ == '__main__':
    demo_lock()
    demo_cv()
