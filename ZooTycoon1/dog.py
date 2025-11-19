from animal import Animal


class Dog(Animal):
    _tail_length = 0.2
    def __init__(self, name="Anonymous", colour="Brown", limb_count=4, tail_length=0.2):
        super().__init__(name=name, species="Dog", colour=colour, limb_count=limb_count)
        self.tail_length = tail_length

    @property
    def tail_length(self):
        return self._tail_length

    @tail_length.setter
    def tail_length(self, value):
        if value < 5:
            value = 5
        self._tail_length = value

    def eat(self, food):
        return f"I'm an {self.species} called {self.name} using my muzzle to slobber and gobble {food}"

    def bark(self, number_of_woofs):
        return f"{'woof ' * number_of_woofs}"

    def __str__(self):
        return super.__str__(self) +  f" Tail Length: {self.tail_length}"