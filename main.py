class Animal(object):
    def __init__(self, name, health):
        self.name = name 
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(self, name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(self, name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print self.health , "im a dragon"



# animal1 = Animal("qwer", 100)
# animal1.walk().run().display_health()

doggo = Dog("dogoo")
doggo.run().walk().pet().display_health()

dragon1 = Dragon("dragger")
dragon1.fly().fly().display_health()