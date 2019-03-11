class AbstractOperation:
    def request(self):
        raise NotImplementedError()
        

class RealOperation(AbstractOperation):

    def request(self):
        print("perform operation")


class NullOperation(AbstractOperation):

    def request(self):
        pass

def get_operation(n):
    if n < 0:
        return NullOperation()
    return RealOperation()


if __name__ == '__main__':
    op = get_operation(1)
    op.request()
    op = get_operation(0)
    op.request()
    op = get_operation(-1)
    op.request()
