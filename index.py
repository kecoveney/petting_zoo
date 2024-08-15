from walking import Donkey, Llama, Goat, Sheep, Pig
from slithering import Copperhead, RatSnake, CornSnake, BallPython, KingSnake
from swimming import Mallard, Goldfish, Koi, Turtle, Frog

# Creating instances of each class with a shift and food for walking animals
miss_fuzz = Llama(name="Miss Fuzz", species="Llama", shift="morning", food="Llama Chow")
billy = Goat(name="Billy", species="Goat", shift="midday", food="Hay")
charlie = Donkey(name="Charlie", species="Donkey", shift="afternoon", food="Carrots")
wooly = Sheep(name="Wooly", species="Sheep", shift="morning", food="Grass")
porky = Pig(name="Porky", species="Pig", shift="midday", food="Pig Feed")

# Creating instances of slithering animals
slither = Copperhead(name="Slither", species="Copperhead", food="Mice")
sneaky = RatSnake(name="Sneaky", species="Rat Snake", food="Rats")
stripey = CornSnake(name="Stripey", species="Corn Snake", food="Crickets")
curly = BallPython(name="Curly", species="Ball Python", food="Rats")
king = KingSnake(name="King", species="King Snake", food="Mice")

# Creating instances of swimming animals
quackers = Mallard(name="Quackers", species="Mallard", food="Duck Feed")
bubbles = Goldfish(name="Bubbles", species="Goldfish", food="Fish Flakes")
splash = Koi(name="Splash", species="Koi", food="Koi Pellets")
shellie = Turtle(name="Shellie", species="Turtle", food="Turtle Pellets")
ribbit = Frog(name="Ribbit", species="Frog", food="Insects")

# Feeding the animals
miss_fuzz.feed()
billy.feed()
charlie.feed()
wooly.feed()
porky.feed()

slither.feed()
sneaky.feed()
stripey.feed()
curly.feed()
king.feed()

quackers.feed()
bubbles.feed()
splash.feed()
shellie.feed()
ribbit.feed()


# Printing the name of each critter to verify
print(miss_fuzz)
print(billy)
print(charlie)
print(wooly)
print(porky)

print(slither)
print(sneaky)
print(stripey)
print(curly)
print(king)

print(quackers)
print(bubbles)
print(splash)
print(shellie)
print(ribbit)
