# ex14_oo.py


# 1) class we saw
x = 'abc'   # object 'x'
print(type(x))  # x is instance of class string
print(dir(x))   # methods

y = 2.5
print(type(y))
#print(dir(y))

z = 2
print(type(z))
#print(dir(z))

l = list()
print(type(l))
#print(dir(l))

d = dict()
print(type(d))
#print(dir(d))
print()


# 2) first class
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

    #def __del__(self):
     #   print('I am destructed', self.name)


# object inheritance:
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')  # second independent instance
j.party()
s.party()
j.touchdown()
