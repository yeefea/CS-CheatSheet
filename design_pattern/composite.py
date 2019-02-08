class Employee:

    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def get_subordinates(self):
        for s in self.subordinates:
            yield s
            tmp = s.get_subordinates()
            if tmp:
                yield from tmp

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Intern(Employee):

    def add_subordinate(self, employee):
        pass

    def get_subordinates(self):
        return None


founder = Employee('Steve')
ceo = Employee('Tim')
john = Employee('John')
david = Employee('david')

intern1 = Intern('student1')
intern2 = Intern('student2')
intern3 = Intern('student3')

founder.add_subordinate(ceo)
ceo.add_subordinate(john)
ceo.add_subordinate(david)
david.add_subordinate(intern1)
david.add_subordinate(intern2)
john.add_subordinate(intern3)

sub = list(founder.get_subordinates())
print(sub)
