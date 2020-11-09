"""
意图：
定义作用于对象结构中各元素的操作，不用改变各元素的类就可以定义这些元素的新操作

动机：
编译器，抽象语法树

适用性：
1. 一个对象结构包含很多类，想对这些对象实施一些依赖于具体类的操作
2. 需要对一个对象结构中的对象进行很多不同并且不相关的操作，会污染这些对象的类。visitor把相关的操作集中起来
3. 定义对象结构的类很少改变，但经常需要在此结构上定义新的操作

参与者：
Visitor e.g. NodeVisitor
ConcreteVisitor e.g. TypeCheckVisitor
Element e.g. Node
ConcreteElement  e.g. AssignmentNode
ObjectStructure  e.g. Program

效果：
1. 易于增加新的操作
2. 集中相关操作
3. 难以增加新的Element子类
4. 通过层次进行访问，访问的对象可以完全无关，不需要继承自相同的父类
5. 累积状态
6. 破坏封装

两个实现问题：
1. 双分派 double-dispatch
a.message(b)
根据a和b的实际类型绑定实际方法

2. 谁负责遍历对象结构
可以放到三个地方：对象结构中，访问者中，独立的迭代器对象中，通常由对象结构负责
非常复杂的遍历可以放在访问者中实现，比如遍历AST
"""
from typing import List

"""
Simple example
"""


class CarElement:
    def accept(self, visitor):
        raise NotImplementedError()


class Engine(CarElement):
    def accept(self, visitor):
        visitor.visit_engine(self)


class Wheel(CarElement):
    def accept(self, visitor):
        visitor.visit_wheel(self)


class Car(CarElement):
    def __init__(self):
        self.elements = [
            Wheel(), Wheel(),
            Wheel(), Wheel(),
            Engine()
        ]

    def accept(self, visitor):
        """
        后序遍历
        :param visitor:
        :return:
        """
        for element in self.elements:
            element.accept(visitor)
        visitor.visit_car(self)


class CarElementVisitor:

    def visit_engine(self, engine):
        raise NotImplementedError()

    def visit_wheel(self, wheel):
        raise NotImplementedError()

    def visit_car(self, car):
        raise NotImplementedError()


class CarElementDoVisitor(CarElementVisitor):

    def visit_car(self, car):
        print("Starting my car.")

    def visit_wheel(self, wheel):
        print("Kicking my wheel.")

    def visit_engine(self, engine):
        print("Starting my engine.")


class CarElementPrintVisitor(CarElementVisitor):

    def visit_car(self, car):
        print("Visiting car.")

    def visit_wheel(self, wheel):
        print("Visiting wheel.")

    def visit_engine(self, engine):
        print("Visiting engine.")


"""
Complex example
"""


class Node:
    def type_check(self):
        raise NotImplementedError()

    def generate_code(self):
        raise NotImplementedError()

    def pretty_print(self):
        raise NotImplementedError()

    def accept(self, visitor: "NodeVisitor"):
        raise NotImplementedError()


class VariableRefNode(Node):

    def accept(self, visitor: "NodeVisitor"):
        visitor.visit_variable_ref(self)

    def type_check(self):
        print('valref type check')

    def generate_code(self):
        print('valref code gen')

    def pretty_print(self):
        print('valref pretty print')


class AssignmentNode(Node):
    def accept(self, visitor: "NodeVisitor"):
        visitor.visit_assignment(self)

    def type_check(self):
        print('assign type check')

    def generate_code(self):
        print('assign code gen')

    def pretty_print(self):
        print('assign pretty print')


class NodeVisitor:
    def visit_assignment(self, node: AssignmentNode):
        raise NotImplementedError()

    def visit_variable_ref(self, node: VariableRefNode):
        raise NotImplementedError()


class TypeCheckingVisitor(NodeVisitor):

    def visit_assignment(self, node: AssignmentNode):
        node.type_check()

    def visit_variable_ref(self, node: VariableRefNode):
        node.type_check()


class CodeGeneratingVisitor(NodeVisitor):

    def visit_assignment(self, node: AssignmentNode):
        node.type_check()
        node.generate_code()

    def visit_variable_ref(self, node: VariableRefNode):
        node.type_check()
        node.generate_code()


class Program:

    def __init__(self, nodes: List[Node]):
        self._nodes = nodes

    def accept(self, visitor: "NodeVisitor"):
        for n in self._nodes:
            n.accept(visitor)


"""
Another example
"""


class Equipment:
    NAME = 'equipment'

    def power(self) -> float:
        raise NotImplementedError()

    def net_price(self) -> float:
        raise NotImplementedError()

    def discount_price(self) -> float:
        raise NotImplementedError()

    def accept(self, visitor: "EquipmentVisitor"):
        raise NotImplementedError()


class FloppyDisk(Equipment):
    NAME = 'FloppyDisk'

    def power(self):
        return 10

    def net_price(self):
        return 100

    def discount_price(self):
        return 90

    def accept(self, visitor: "EquipmentVisitor"):
        visitor.visit_floppy_disk(self)


class Card(Equipment):
    NAME = 'Card'

    def power(self):
        return 1

    def net_price(self):
        return 10

    def discount_price(self):
        return 9

    def accept(self, visitor: "EquipmentVisitor"):
        visitor.visit_card(self)


class Chassis(Equipment):
    NAME = 'VisitChassis'

    def __init__(self, parts: List[Equipment]) -> None:
        self._parts = parts

    def power(self) -> float:
        return 0

    def net_price(self) -> float:
        return 1000

    def discount_price(self) -> float:
        return 900

    def accept(self, visitor: "EquipmentVisitor"):
        for i in self._parts:
            i.accept(visitor)
        visitor.visit_chassis(self)


class Bus(Equipment):
    NAME = 'Bus'

    def power(self) -> float:
        return 10000

    def net_price(self) -> float:
        return 10000

    def discount_price(self) -> float:
        return 9000

    def accept(self, visitor: "EquipmentVisitor"):
        visitor.visit_bus(self)


class EquipmentVisitor:

    def visit_floppy_disk(self, e: FloppyDisk):
        raise NotImplementedError()

    def visit_card(self, e: Card):
        raise NotImplementedError()

    def visit_chassis(self, e: Chassis):
        raise NotImplementedError()

    def visit_bus(self, e: Bus):
        raise NotImplementedError()


class PricingVisitor(EquipmentVisitor):

    def __init__(self) -> None:
        self._total = 0.0

    @property
    def total(self):
        return self._total

    def visit_floppy_disk(self, e: FloppyDisk):
        self._total += e.net_price()

    def visit_card(self, e: Card):
        self._total += e.net_price()

    def visit_chassis(self, e: Chassis):
        self._total += e.discount_price()

    def visit_bus(self, e: Bus):
        self._total += e.net_price()


class InventoryVisitor(EquipmentVisitor):

    def visit_floppy_disk(self, e: FloppyDisk):
        pass

    def visit_card(self, e: Card):
        pass

    def visit_chassis(self, e: Chassis):
        pass

    def visit_bus(self, e: Bus):
        pass


if __name__ == '__main__':
    # simple
    car = Car()
    car.accept(CarElementPrintVisitor())
    car.accept(CarElementDoVisitor())

    # complex
    type_check = TypeCheckingVisitor()
    code_gen = CodeGeneratingVisitor()
    var = VariableRefNode()
    eq = AssignmentNode()
    prog = Program([var, eq])
    prog.accept(type_check)
    prog.accept(code_gen)
