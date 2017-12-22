# 定义一个“Animal”类，具有吃、喝、拉、撒的功能
class Animal:
    name = ''

    def eat(self):
        print("%s 吃 " % self.name)

    def drink(self):
        print("%s 喝 " % self.name)

    def shit(self):
        print("%s 拉 " % self.name)

    def pee(self):
        print("%s 撒 " % self.name)

    # 定义一个“Cat”类，继承“Animal”类所有功能，同时添加属于猫的“喵喵叫”功能


class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        print('喵喵叫')


# 定义一个“Dog”类，继承“Animal”类所有功能，同时添加属于狗的“汪汪叫”功能
class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '狗'

    def cry(self):
        print('汪汪叫')


# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()
