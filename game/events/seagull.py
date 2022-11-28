from game import event
from game.player import Player
from game.context import Context
from game.crewmate import CrewMate
import game.config as config
import game.ship as ship
import random

class Seagull (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "seagull visitor"
        self.seagulls = 1
        self.verbs['chase'] = self
        self.verbs['feed'] = self
        self.verbs['help'] = self
        self.verbs['kill'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
            self.go = True
            r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "the seagulls fly off."
                if (self.seagulls > 1):
                    self.seagulls = self.seagulls - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.lucky == True):
                    self.result["message"] = "luckly, the seagulls fly off."
                else:
                    self.result["message"] = c.get_name() + " is attacked by the seagulls."
                    if (c.inflict_damage (self.seagulls, "Pecked to death by seagulls")):
                        self.result["message"] = ".. " + c.get_name() + " is pecked to death by the seagulls!"
        if (verb == "kill"):
            self.go = True
            self.result["newevents"].append (Seagull())
            self.result["message"] = "You killed the seagulls and procured food."
            amt = random.randint(10,16)
            ship_food = config.the_player.ship
            ship_food.food =  ship_food.food + amt
            #increase food stores from seagull
    
            
            

        elif (verb == "feed"):
            self.seagulls = self.seagulls + 1
            self.result["newevents"].append (Seagull())
            self.result["message"] = "the seagulls are happy"
            self.go = True
        elif (verb == "help"):
            print ("the seagulls will pester you until you feed them or chase them off")
            self.go = False
        else:
            print ("it seems the only options here are to feed or chase or kill")
            self.go = False

            



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.seagulls) + " seagulls has appeared what do you want to do?")
            Player.get_interaction ([self])

        return self.result
