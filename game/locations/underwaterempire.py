from game import location
from game.events import *
from game import config
from game.display import announce
from game.items import Cutlass
from game.items import Flintlock

class UnderwaterEmpire(location.Location):
    def __init__(self,x,y,w):
        self.x = x
        self.y = y
        self.w = w
        self.name = "underwater empire"
        self.symbol = "U"
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["hunting ground"] =HuntingGround(self)
        self.locations["merfolk's dwelling"] = Merfolk_dwelling(self)
        self.locations["shark habitat"] = SharkHabitat(self)
        self.locations["deep water"] =DeepWater(self)
        self.locations["treasure room"] =TreasureRoom(self)
        
    def enter(self, ship):
        print("You found the entrance to an underground empire, what is your command?")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        
        self.event_chance = 50
        #self.events.append (seagull.Seagull())
        #self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["hunting ground"]
            announce ("You entered the new area of the empire.")
        elif(verb == "east"):
            config.the_player.next_loc = self.main_location.locations["shark habitat"]
            announce ("You entered the new area of the empire.")
        elif(verb == "west"):
            config.the_player.next_loc = self.main_location.locations["merfolk's dwelling"]
            announce ("You entered the new area of the empire.")

        
            
class HuntingGround(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "hunting ground"
        self.verbs['east'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['west'] = self
        
        
    def enter(self):
        announce('"Hunting Ground"')

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "east"):
            config.the_player.next_loc = self.main_location.locations["shark habitat"]
            announce ("You entered the new area of the empire.")
        elif(verb == "west"):
            config.the_player.next_loc = self.main_location.locations["merfolk's dwelling"]
            announce ("You entered the new area of the empire.")
        elif(verb == "north"):
            config.the_player.next_loc = self.main_location.locations["deep water"]
            announce ("You entered the new area of the empire.")
        elif(verb == "south"):
            config.the_player.next_loc = self.main_location.locations["beach"]
            announce ("You entered the new area of the empire.")
        
            

class Merfolk_dwelling (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "merfolk's dwelling"
    
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        
        
        self.event_chance = 100
        self.events.append(merfolk.Merfolk())
    def enter(self):
        announce('"Dwelling of Merfolk"')

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "west"):
            config.the_player.next_loc = self.main_location.locations["shark habitat"]
            announce ("You entered the new area of the empire.")
        elif(verb == "east"):
            config.the_player.next_loc = self.main_location.locations["hunting ground"]
            announce ("You entered the new area of the empire.")
        elif(verb == "north"):
            config.the_player.next_loc = self.main_location.locations["deep water"]
            announce ("You entered the new area of the empire.")
        elif(verb == "south"):
            announce ("It seems there is no south in this area")
        
class SharkHabitat (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "shark habitat"
        
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        #self.verbs['south'] = self
        
        self.event_chance = 50
        self.events.append(shark.Shark())
    def enter(self):
        announce('"Shark Habitat"')

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "east"):
            config.the_player.next_loc = self.main_location.locations["merfolk's dwelling"]
            announce ("You entered the new area of the empire.")

        elif(verb == "west"):
            config.the_player.next_loc = self.main_location.locations["hunting ground"]
            announce ("You entered the new area of the empire.")
        elif(verb == "north"):
            config.the_player.next_loc = self.main_location.locations["deep water"]
            announce ("You entered the new area of the empire.")
        
class DeepWater (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "deep water"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        
        
        self.event_chance = 100
        self.events.append(giant_monster_squid.GiantMonsterSquid())
    def enter(self):
        announce('"Deep Water"')

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "go east"):
            config.the_player.next_loc = self.main_location.locations["shark habitat"]
            announce ("You entered the new area of the empire.")

        elif(verb == "west"):
            config.the_player.next_loc = self.main_location.locations["merfolk's dwelling"]
            announce ("You entered the new area of the empire.")

        elif(verb == "north"):
            config.the_player.next_loc = self.main_location.locations["treasure room"]
            announce ("You entered the new area of the empire.")

        elif(verb == "south"):
            config.the_player.next_loc = self.main_location.locations["hunting ground"]
            announce ("You entered the new area of the empire.")


class TreasureRoom (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = 'treasure room'
        
        self.verbs['exit'] = self
        self.verbs['explore'] = self
        self.verbs['take'] = self
        self.verbs['south'] = self
        
        self.event_chance = 100
        self.events.append(giant_monster_squid.GiantMonsterSquid())
    def enter(self):
        announce('"Treasure Room" : Try to explore the room."')

    def process_verb (self, verb, cmd_list, nouns):
        
        if(verb == "south"):
            config.the_player.next_loc = self.main_location.locations["deep water"]
            announce ("You entered the new area of the empire.")

        elif(verb == "exit"):
            config.the_player.next_loc = self.main_location.locations["hunting ground"]
            announce ("You return to the beach.")
        
       # if(verb == "explore"):
           # config.the_player.next_loc = self.main_location.locations["hunting area"]
