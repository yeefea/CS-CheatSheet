# from select import select
#
#
# select()
# def fun():
#     yield 1
#     yield 2
#     yield 3
#
#
# def fun_2():
#     print('step 1')
#
#     print('step 2')
#
#     print('step 3')
#
#
# gen_list = [fun(), fun(), fun()]
#
# for gen in zip(*gen_list):
#     for x in gen:
#         print(x)
#
# schedule_list = []
#
#
# class Handle:
#     def __init__(self, gen):
#         self.gen = gen
#
#     def call(self):
#         try:
#             next(self.gen)
#         except:
#             pass
#         else:
#             schedule_list.append(self)
#
#
# def loop(*coroutines):
#     schedule_list.extend(Handle(c) for c in coroutines)
#
#     while schedule_list:
#         handle = schedule_list.pop(0)
#         handle.call()
#
#
# loop(fun_2(), fun_2(), fun_2())


def func1():
    yield
    print('logic1')
    yield
    print('logic2')
    # ...


def func2():
    yield
    print('logic3')
    yield
    print('logic4')
    # ...


def func3():
    print('logic5')
    yield from func1()
    print('logic6')
    yield from func2()
    # ...


coro1 = func1()
coro2 = func2()
coro3 = func3()
coros = [coro1, coro2, coro3]
while True:
    if len(coros) == 0:
        break
    coro = coros.pop()

    try:
        next(coro)
        coros.insert(0, coro)
    except StopIteration:
        pass
