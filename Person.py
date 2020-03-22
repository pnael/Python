class Person:
    def __init__(self, name):
        self.name= name 

    def talk(self):
        print(f"Hi I am {self.name}")

phil = Person("Philippe")
print(phil.name)
phil.talk()