from datetime import date

class Pig:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
