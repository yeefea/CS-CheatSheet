"""
解释器模式在实际工作中很少用到
"""

class Expression:
    def interpreter(self, ctx):
        raise NotImplementedError()

class TerminialExpression(Expression):
    """
    终结表达式
    """
    def __init__(self, data):
        self.data = data
    
    def interpreter(self, ctx):
        if self.data in ctx:
            return True
        return False

class OrExpression(Expression):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def interpreter(self, ctx):
        return self.exp1.interpreter(ctx) or self.exp2.interpreter(ctx)

class AndExpression(Expression):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    
    def interpreter(self, ctx):
        return self.exp1.interpreter(ctx) and self.exp2.interpreter(ctx)

if __name__ == '__main__':
    david = TerminialExpression('David')
    john = TerminialExpression('John')
    is_single = OrExpression(david, john)
    vikram = TerminialExpression('Vikram')
    committed = TerminialExpression('Committed')
    is_committed = AndExpression(vikram, committed)
    print(is_single.interpreter('David'))
    print(is_single.interpreter('John'))
    print(is_single.interpreter('Alice'))
    print(is_committed.interpreter('Committed, Vikram'))
    print(is_committed.interpreter('Single, Vikram'))