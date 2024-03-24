class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water.")

    # build on method from super class Animal
    def breathe(self):
        # do everything that Animal breathe() does
        super().breathe()
        # add additional functionalities
        print("Doing this underwater.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
