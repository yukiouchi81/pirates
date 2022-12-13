from game import event
import random
from game.combat import Combat
from game.combat import Merfolks
from game.display import announce
from game.player import Player
import game.config as config
from game.ship import Ship

class Merfolk (event.Event):

    def __init__ (self):
        self.name = "Merfolk attack"

    def process (self, world):
        result = {}
        result["message"] = "The swarm of merfolks is defeated!"

        
        monsters = []
        min = 4
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(Merfolks("King of merfolk"))
            monsters[0].speed = 3*monsters[0].speed
            monsters[0].health = 3*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        
        while n <= n_appearing: 
            monsters.append(Merfolks("Merfolk"+str(n)))
            n += 1
        announce ("You are attacked by a swarm of merfolks!")
        Combat(monsters).combat()
        
        result["newevents"] = [self]
        
        
        amt = random.randrange(1,3)
        ship = config.the_player.ship
        ship.nappod =  ship.nappod + amt
        result["message"] = "\nYou obtained " +str(ship.nappod)+" water-proof nap pod from the corpse of merfolks.\nYou can use a nap pod with rest or sleep command."
        return result
        
        
        

