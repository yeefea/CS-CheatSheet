"""
动机
原理
优点
缺点
应用
"""
class Calculator:

    def __init__(self, operation):
        """
        :param operation: strategy
        """
        self.operation = operation
    
    def change_operation(self, operation):
        self.operation = operation

    def calculate(self, n1, n2):
        return self.operation.operate(n1, n2)


class Operation:

    def operate(self, n1, n2):
        raise NotImplementedError()

class Add(Operation):
    def operate(self, n1, n2):
        return n1 + n2

class Subtract(Operation):
    def operate(self, n1, n2):
        return n1 - n2

class Multiply(Operation):
    def operate(self, n1, n2):
        return n1 *n2

class Divide(Operation):

    def operate(self, n1, n2):
        return n1 / n2

if __name__ == '__main__':
    cal = Calculator(Add())
    print(cal.calculate(1,2))
    cal.change_operation(Subtract())
    print(cal.calculate(1,2))
    cal.change_operation(Multiply())
    print(cal.calculate(1,2))
    cal.change_operation(Divide())
    print(cal.calculate(1,2))

