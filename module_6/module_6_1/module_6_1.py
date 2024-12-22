class Animal:
    def __init__(self, name=''):
        self.name = name
        self.fed = False
        self.alive = True

    def eat(self, food):
        if food.edible:
            print(F'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(F'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name=''):
        self.edible = False
        self.name = name


class Mammal(Animal):  # наследует eat от Animal
    pass


class Predator(Animal):  # наследует eat от Animal
    pass


class Flower(Plant):  # наследует от Plant
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
