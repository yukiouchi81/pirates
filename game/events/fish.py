from game import event
from game.player import Player
from game.context import Context
from game.crewmate import CrewMate
import game.config as config
import game.ship as ship
import random

class Fish (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "Fish"
        self.seagulls = 1
        self.verbs['chase'] = self
        self.verbs['kill'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
            self.go = True
            self.result["message"] = "the fish swim away."
            self.result["newevents"].append (Fish())
        if(verb == "kill"):
            self.go = True
            self.result["message"] = "You killed the fish and procured food."
            amt = random.randint(20,25)
            ship_food = config.the_player.ship
            ship_food.food =  ship_food.food + amt

        else:
            print ("it seems the only options here are chase or kill")
            self.go = False


    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print ("Fish has appeared what do you want to do?")
            Player.get_interaction ([self])

        return self.result
