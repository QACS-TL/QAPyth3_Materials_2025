import unittest
import animal
import dog


class AnimalTests(unittest.TestCase):
    def test_string(self):
        # Arrange
        expected_result = "Name: Felix, Species: Cat, Colour: Brown, Limb Count: 4"
        ani = animal.Animal("Felix", "Cat", "Brown", 4)

        # Act
        result = ani.__str__()

        # Assert
        self.assertEqual(expected_result, result)

    def test_eat(self):
        # Arrange
        expected_result = "I'm an Cat called Felix using some of my 4 limbs to eat fish"
        ani = animal.Animal("Felix", "Cat", "Brown", 4)

        # Act
        result = ani.eat("fish")

        # Assert
        self.assertEqual(expected_result, result)


    def test_Illegal_limb_count(self):
        # Arrange
        expected_result = 0

        # Act
        ani = animal.Animal("Felix", "Cat", "Brown", -14)

        # Assert
        self.assertEqual(expected_result, ani.limb_count)

    def test_dog_initialiser(self):
        # Arrange
        expected_result = "Name: Felix, Species: Dog, Colour: Orange, Limb Count: 4, Tail Length: 0.75"
        d = dog.Dog(name="Felix", colour="Orange", limb_count = 4, tail_length=0.75)

        # Act
        result = d.__str__()

        # Assert
        self.assertEqual(expected_result, result)