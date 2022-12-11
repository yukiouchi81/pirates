from game import event
import random
from game.combat import Combat
from game.combat import Shark
from game.display import announce
from game.player import Player
import game.config as config

class Shark (event.Event):

    def __init__ (self):
        self.name = "Shark attack"

    def process (self, world):
        result = {}
        result["message"] = "the flock of sharks is defeated!"
        
        monsters = []
        min = 7
        uplim = 8
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(Shark("Hammerhead shark"))
            monsters[0].speed = 2*monsters[0].speed
            monsters[0].health = 3*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing: 
            monsters.append(Shark("Shark "+str(n)))
            n += 1
        announce ("You are attacked by a flock of sharks!")
        Combat(monsters).combat()
        result["newevents"] = [self]
       # x = random.randint(1,5)
        #config.the_player.ship.medicine += x
        return result


        

        

       # result["message"] = "You obtained the a water-proof nap pod from the corpse of merfolks."


