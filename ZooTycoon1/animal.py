import this


class Animal:
    _limb_count = 0
    _colour = "Brown"

    def __init__(self, name="Anonymous", species="Animal", colour="Brown", limb_count=4):
        self.name = name
        self.species = species
        self.colour = colour
        self.limb_count = limb_count

    @property
    def limb_count(self):
        return self._limb_count

    @limb_count.setter
    def limb_count(self, value):
        if value < 0:
            value = 0
        self._limb_count = value

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if not value in ("Brown", "Black", "White", "Orange", "Purple", "Pink"):
            value = "Brown"
        self._colour = value

    def eat(self, food):
        return f"I'm a {self.species} called {self.name} using some of my {self._limb_count} limbs to eat {food}"

    def move(self, direction, distance):
        return f"I'm an {self.species} called {self.name} moving {direction} for {distance} metres"

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Colour: {self.colour}, Limb Count: {self.limb_count}"