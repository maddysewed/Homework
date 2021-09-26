def main():
    class Bird():
        def __init__(self, name) -> None:
            self.name = name

        def __str__(self) -> str:
            return f"{self.name} bird can walk"

        def fly(self):
            ...

        def walk(self):
            return print(f"{self.name} bird can walk")


    class FlyingBird(Bird):
        ration = "mostly grains"

        def __init__(self, name, ration=ration) -> None:
            self.name = name
            self.ration = ration
              
        def __str__(self) -> str:
            return f"{self.name} can walk and fly"

        def fly(self):
            return f"{self.name} can fly"

        def walk(self):
            super().walk()

        def eat(self):
            return print(f"{self.name} eat {self.ration}")

    
    class NonFlyingBird(Bird):
        ration = "mostly fish"

        def __init__(self, name, ration=ration) -> None:
            self.name = name
            self.ration = ration  

        def __str__(self) -> str:
            return f"{self.name} bird can walk and swim"

        def swim(self):
            return f"{self.name} bird can swim"

        def walk(self):
            super().walk()

        def fly(self):
            raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

        def eat(self):            
            return print(f"{self.name} eats {self.ration}")


    class SuperBird(NonFlyingBird, FlyingBird):
        ration = "mostly fish"

        def __init__(self, name, ration=ration) -> None:
            super().__init__(name, ration)  

        def __str__(self) -> str:
            return f"{self.name} bird can walk, swim and fly"

        def swim(self):
            super().swim()

        def walk(self):
            super().walk()

        def fly(self):
            super(FlyingBird, self).fly()

        def eat(self):            
            super().eat()


    b = Bird("Any") # Testing
    b.walk()
    print(str(b))
    c = FlyingBird("Canary")
    print(str(c))
    c.eat()
    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    #p.fly()
    p.eat()
    s = SuperBird("Gull")
    print(str(s))
    s.eat()

if __name__ == "__main__":
    main()