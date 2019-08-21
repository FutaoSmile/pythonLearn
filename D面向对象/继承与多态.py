class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def wang(self):
        print('wang wang wang...')

    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def eat(self):
        print('eat eat eat...')

    def run(self):
        print('Cat is running...')


def run(m_object):
    m_object.run()
    pass


a1 = Animal()
a1.run()

d1 = Dog()
d1.run()
d1.wang()

d2 = Dog()
d2.run()
d2.wang()

c1 = Cat()
c1.run()
c1.eat()

c2 = Cat()
c2.run()
c2.eat()

print('-----------')
run(a1)
run(d1)
run(c1)
