from walking import Donkey, Llama, Goat, Sheep, Pig
from slithering import Copperhead, RatSnake, CornSnake, BallPython, KingSnake
from swimming import Mallard, Goldfish, Koi, Turtle, Frog

# Creating instances of each class with a shift for walking animals
miss_fuzz = Llama(name="Miss Fuzz", species="Llama", shift="morning")
billy = Goat(name="Billy", species="Goat", shift="midday")
charlie = Donkey(name="Charlie", species="Donkey", shift="afternoon")
wooly = Sheep(name="Wooly", species="Sheep", shift="morning")
porky = Pig(name="Porky", species="Pig", shift="midday")

# Creating instances of slithering animals
slither = Copperhead(name="Slither", species="Copperhead")
sneaky = RatSnake(name="Sneaky", species="Rat Snake")
stripey = CornSnake(name="Stripey", species="Corn Snake")
curly = BallPython(name="Curly", species="Ball Python")
king = KingSnake(name="King", species="King Snake")

# Creating instances of swimming animals
quackers = Mallard(name="Quackers", species="Mallard")
bubbles = Goldfish(name="Bubbles", species="Goldfish")
splash = Koi(name="Splash", species="Koi")
shellie = Turtle(name="Shellie", species="Turtle")
ribbit = Frog(name="Ribbit", species="Frog")

# Printing the name of each critter to verify
print(miss_fuzz)
print(billy)
print(charlie)
print(wooly)
print(porky)

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
