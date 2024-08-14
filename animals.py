from datetime import date

# Petting Area Critters
class Donkey:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Llama:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Sheep:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Pig:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

# Glass Tank Critters
class Copperhead:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class RatSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class CornSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class BallPython:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class KingSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

# Pond Critters
class Mallard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

# Creating instances of each class without the date_added parameter
miss_fuzz = Llama(name="Miss Fuzz", species="Llama")
billy = Goat(name="Billy", species="Goat")
charlie = Donkey(name="Charlie", species="Donkey")
wooly = Sheep(name="Wooly", species="Sheep")
porky = Pig(name="Porky", species="Pig")

slither = Copperhead(name="Slither", species="Copperhead")
sneaky = RatSnake(name="Sneaky", species="Rat Snake")
stripey = CornSnake(name="Stripey", species="Corn Snake")
curly = BallPython(name="Curly", species="Ball Python")
king = KingSnake(name="King", species="King Snake")

quackers = Mallard(name="Quackers", species="Mallard")
bubbles = Goldfish(name="Bubbles", species="Goldfish")
splash = Koi(name="Splash", species="Koi")
shellie = Turtle(name="Shellie", species="Turtle")
ribbit = Frog(name="Ribbit", species="Frog")

# Printing the name of each critter to verify
print(miss_fuzz.name)
print(billy.name)
print(charlie.name)
print(wooly.name)
print(porky.name)

print(slither.name)
print(sneaky.name)
print(stripey.name)
print(curly.name)
print(king.name)

print(quackers.name)
print(bubbles.name)
print(splash.name)
print(shellie.name)
print(ribbit.name)
