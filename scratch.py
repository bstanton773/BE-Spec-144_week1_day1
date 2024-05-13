class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + ' ' + self.last

    def __repr__(self):
        return f"<Person|{self.first} {self.last}>"



me = Person('Brian', 'Stanton')
you = Person('James','Carlson')

us = [me, you]


print(type(me))
print(you)
print(us)