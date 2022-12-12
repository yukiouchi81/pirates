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
        self.verbs['kill'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
            self.result["message"] = "the seagulls fly off."
            self.go = True
                
        if (verb == "kill"):
            
            self.result["newevents"].append (Seagull())
            self.result["message"] = "You killed the seagulls and procured food."
            amt = random.randint(12,16)
            ship_food = config.the_player.ship
            ship_food.food =  ship_food.food + amt
            self.go = True
            
        elif (verb == "feed"):
            self.seagulls = self.seagulls + 1
            self.result["newevents"].append (Seagull())
            self.result["message"] = "the seagulls are happy"
            self.go = True

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
