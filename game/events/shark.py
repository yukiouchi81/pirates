
from game import event
import random
from game.combat import Combat
from game.combat import Sharks
from game.display import announce
import game.config as config
from game.player import Player
from game.context import Context
class Shark (event.Event):

    def __init__ (self):
        self.name = "shark attack"
        

    def process (self, world):
        result = {}
        result["message"] = "The lock of sharks are defeated!"
        
        monsters = []
        min = 5
        uplim = 6
        if random.randrange(2) == 0:
            min = 4
            uplim = 5
            monsters.append(Sharks("Hammerhead shark"))
            monsters[0].speed = 1.5*monsters[0].speed
            monsters[0].health = 3*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters. append(Sharks("Shark"+str(n)))
            n += 1
        announce ("You are attacked by a flock of sharks!")
        Combat(monsters).combat()
        result["newevents"] = [self]
        amt = random.randint(1,5)
        ship = config.the_player.ship
        ship.medicine =  ship.medicine + amt
        result["message"] = "You obtained medicine from the corpse of sharks."

        return result

