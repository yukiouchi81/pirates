from game import event
from game.combat import Combat
from game.combat import Giant
from game.display import announce
import game.config as config
from game.ship import Ship
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
        
        
        
        amt = 1
        ship = config.the_player.ship
        ship.key =  ship.key + amt
        result["message"] = "There's something by the monster's corpse ... you obtained a key!!"
        
        
        return result


        #config.the_player.ship.food += n_appearing*2


