from game import event
import random
from game.combat import Combat
from game.combat import Merfolk
from game.display import announce
from game.player import Player
import game.config as config

class Merfolk (event.Event):

    def __init__ (self):
        self.name = "Merfolk attack"

    def process (self, world):
        result = {}
        result["message"] = "the swarm of merfolks!"

        monsters = []
        n_appearing = random.randrange(4,8)
        n = 1
        """
        monsters = []
        min = 4
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(Merfolk("King of merfolk"))
            monsters[0].speed = 1.8*monsters[0].speed
            monsters[0].health = 3*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        """
        while n <= n_appearing: 
            monsters.append(Merfolk("Merfolk"+str(n)))
            n += 1
        announce ("You are attacked by a swarm of merfolks!")
        Combat(monsters).combat()
        
        #result["newevents"] = [self]
        #config.the_player.ship.nappod += 1
        return result
        

        #result["message"] = "You obtained the a water-proof nap pod from the corpse of merfolks."
        

