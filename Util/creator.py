import random
from model.human import Human
import string

class HumanCreator:
    @staticmethod
    def create(size):
        NAMES = ("Alex", "Kate", "Mary", "Alice", "Peter", "Ivan", "Stuart",
                "Max", "Vladimir", "Evgen", "Victor", "Mikl")
        ALFABET = string.ascii_uppercase

        MAX_AGE = 130
        MIN_AGE = 0

        ls = []

        for _ in range(size):
            firstname = random.choice(NAMES)
            surname = ALFABET[random.randrange(len(ALFABET))]
            age = random.randint(MIN_AGE, MAX_AGE)
            alive = random.randrange(2)
            human = Human(firstname, surname, age, alive)
            ls.append(human)

        return ls

