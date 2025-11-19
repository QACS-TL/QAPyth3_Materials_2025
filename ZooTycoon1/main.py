import animal
from dog import Dog

zoo = []
ani1 = animal.Animal(name="Fido", species="Dog", colour="White", limb_count = 3)
# ani1.name = "Fido"
# ani1.species = "Dog"
# ani1.colour = "White"
# ani1.limb_count = 3

zoo.append(ani1)

ani2 = animal.Animal("Felix", "Cat", "Green", -1)
# ani2.name = "Felix"
# ani2.species = "Cat"
# ani2.colour = "Black"
# ani2.limb_count = 5
zoo.append(ani2)

#ani2.limb_count = -1
#ani2.set_limb_count(-1)

print(ani1.name, ani1.species, ani1.colour, ani1.limb_count)
#print(ani1.name, ani1.species, ani1.colour, ani1.get_limb_count())
print(ani2.name, ani2.species, ani2.colour, ani2.limb_count)

print(ani1.eat("Biscuits"))
print(ani2.eat("Fish"))

print(ani1.move("North", 5))
print(ani2.move("South", 20))

d = Dog(name="Rover", colour="White", limb_count = 3, tail_length=0.5)

print(d.eat("Fish"))
print(d.bark(5))
print(d.eat("cucumber"))

zoo.append(animal.Animal(name="Bonzo", species="Dog", colour="Pink", limb_count = 3))
zoo.append(animal.Animal(name="Fifi", species="Cat", colour="Orange", limb_count = 4))
zoo.append(d)
# zoo.append("Banana")

# Feeding time
cats = [ani for ani in zoo if ani.species == "Cat"]
for cat in cats:
    print(cat.eat("Fish"))
dogs = [ani for ani in zoo if ani.species == "Dog"]
for dog in dogs:
    print(dog.eat("Biscuits"))

for ani in zoo:
    if ani.species == "Cat":
        print(ani.eat("Cream"))
    elif ani.species == "Dog":
        print(ani.eat("Bone"))
    else:
        print("Not an animal")


