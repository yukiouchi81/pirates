from game import event
import random
from game.combat import Combat
from game.combat import Shark
from game.display import announce
import game.config as config
from game.player import Player

class Shark (event.Event):

    def __init__ (self):
        self.name = "shark attack"
        

    def process (self, world):
        result = {}
        result["message"] = "The lock of sharks are defeated!"
        
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
            monsters. append(Shark("Shark "+str(n)))
            n += 1
        announce ("You are attacked by a flock of sharks!")
        Combat(monsters).combat()
        result["newevents"] = [self]
        x = random.randint(1,5)
        config.the_player.ship.medicine += x
        
        return result


"""
from game import event
import random
from game.combat import Combat
from game.combat import Macaque
from game.display import announce
import game.config as config

class ManEatingMonkeys (event.Event):

    def __init__ (self):
        self.name = " monkey attack"

    def process (self, world):
        result = {}
        result["message"] = "the macaques are defeated! ...Those look pretty tasty!"
        monsters = []
        n_appearing = random.randrange(4,8)
        n = 1
        while n <= n_appearing:
            monsters.append(Macaque("Man-eating Macaque "+str(n)))
            n += 1
        announce ("The crew is attacked by a troop of man-eating macaques!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        
        return result

"""

