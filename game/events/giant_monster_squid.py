from game import event
from game.combat import Combat
from game.combat import Giant
from game.display import announce
import game.config as config

class GiantMonsterSquid(event.Event):
    def __init__(self):
        self.name = "Giant moster squid attack"

    def process(self, world):
        result = {}
        result["message"] = "the giant monster squid is defeated!"

        monsters = []
        n_appearing = 1
        n = 1
        while n <= n_appearing:
            monsters.append(Giant("Giant monster squid "+str(n)))
            n += 1
        announce ("The crew is attacked by a giant monster squid!")
        Combat(monsters).combat()
        result["newevents"] = []
        return result
        #config.the_player.ship.food += n_appearing*2



        
""" if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        
        return result
"""
