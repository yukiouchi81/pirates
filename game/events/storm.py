from game import event
from game.location import Location

class Storm(event.Event):
    def __init__(self):
        self.name = "Storm swallows the crew."
