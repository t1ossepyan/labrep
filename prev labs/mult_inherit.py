class Flyer:
    def fly(self):
        print("Летает!")

class Swimmer:
    def swim(self):
        print("Плавает!")

class Duck(Flyer, Swimmer):  
    pass

duck = Duck()
duck.fly()   
duck.swim()  
