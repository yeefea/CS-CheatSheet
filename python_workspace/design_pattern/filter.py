"""
Intercepting filter pattern
https://en.wikipedia.org/wiki/Intercepting_filter_pattern
"""
MALE = 'm'
FEMALE = 'f'


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Filter:

    def apply(self, person):
        return True


class GenderFilter(Filter):
    def __init__(self, gender):
        super().__init__()
        self.gender = gender

    def apply(self, person):
        if person.gender == self.gender:
            return True
        return False


class AgeFilter(Filter):
    def __init__(self, min_age, max_age):
        super().__init__()
        self.min_age = min_age
        self.max_age = max_age

    def apply(self, person):
        if self.min_age <= person.age <= self.max_age:
            return True
        return False


class OrFilterChain(Filter):

    def __init__(self, filter_list):
        super().__init__()
        self.filter_list = filter_list

    def apply(self, person):
        for f in self.filter_list:
            if f.apply(person):
                return True
        return False


class AndFilterChain(Filter):

    def __init__(self, filter_list):
        self.filter_list = filter_list

    def apply(self, person):
        for f in self.filter_list:
            if not f.apply(person):
                return False
        return True


class FilterManager:

    def __init__(self, flt):
        self.flt = flt

    def filter(self, person_list):
        return [p for p in person_list if self.flt.apply(p)]


if __name__ == '__main__':
    p1 = Person('David', MALE, 40)
    p2 = Person('John', MALE, 80)
    p3 = Person('Alice', FEMALE, 15)
    person_list = [p1, p2, p3]

    f_age = AgeFilter(18, 70)
    f_age_young = AgeFilter(11, 15)
    f_or = OrFilterChain([f_age, f_age_young])
    f = AndFilterChain([GenderFilter(FEMALE), f_or])

    manager = FilterManager(f_or)
    res = manager.filter(person_list)
    print(res)
