from game import location
from game.events import *
from game import config
from game.display import announce
from game.items import Cutlass
from game.items import Flintlock
from game.ship import Ship
from game.player import Player

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
        print("\nYou found the underground empire.")

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
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['give'] = self
        
        
        self.event_chance = 100
        self.events.append (fish.Fish())
        self.events.append (fish.Fish())
        self.events.append (nothing.Nothing())
        self.events.append (nothing.Nothing())
        self.events.append (nothing.Nothing())
        self.events.append (sickness.Sickness())
        self.events.append (lucky.LuckyDay())
       

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
        elif (verb == "west"):
            announce ("You walked all the way to the west, but there is nothing interesting.")
        elif (verb == "east"):
            announce ("You walked all the way to the east, but there is nothing interesting.")
        
        elif (verb == "give"):
            # give medicine to crewmember
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (Ship().medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        Ship().medicine =  Ship().medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")
        else:
            announce ("Error: Ship object doe not understand verb " + verb)
        
       
class HuntingGround(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "hunting ground"
        self.verbs['east'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['west'] = self
        self.verbs['give'] = self


        self.event_chance = 50
        self.events.append (man_eating_monkeys.ManEatingMonkeys())
        self.events.append (man_eating_monkeys.ManEatingMonkeys())
        self.events.append (fish.Fish())
        self.events.append (nothing.Nothing())
        self.events.append (sickness.Sickness())
        self.events.append (lucky.LuckyDay())

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
            announce ("You return to the beach..")
        
        elif (verb == "give"):
            # give medicine to crewmember
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (Ship().medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        Ship().medicine =  Ship().medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")
        else:
            announce ("Error: Ship object doe not understand verb " + verb)

class Merfolk_dwelling (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "merfolk's dwelling"
    
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['give'] = self
        
        self.event_chance = 100
        self.events.append(merfolk.Merfolk())
        #self.events.append (fish.Fish())
        #self.events.append (nothing.Nothing())

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
        elif (verb == "give"):
            # give medicine to crewmember
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (Ship().medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        Ship().medicine =  Ship().medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")
        else:
            announce ("Error: Ship object doe not understand verb " + verb)
        
class SharkHabitat (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "shark habitat"
        
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        #self.verbs['south'] = self
        self.verbs['give'] = self
        
        self.event_chance = 30
        self.events.append(shark.Shark())
        self.events.append(shark.Shark())
        self.events.append (fish.Fish())
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
        elif (verb == "give"):
            # give medicine to crewmember
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (Ship().medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        Ship().medicine =  Ship().medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")
        else:
            announce ("Error: Ship object doe not understand verb " + verb)
        
class DeepWater (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "deep water"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['give'] = self
        
        
        self.event_chance = 100
        self.events.append(giant_monster_squid.GiantMonsterSquid())
        self.events.append (fish.Fish())
        self.events.append (fish.Fish())
        self.events.append (nothing.Nothing())
        self.events.append (nothing.Nothing())


        
    def enter(self): 
        announce("'Deep Water'")
        announce("Something enormous is moving around you...")
            

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "east"):
            config.the_player.next_loc = self.main_location.locations["shark habitat"]
            announce ("You entered the new area of the empire.")

        elif(verb == "west"):
            config.the_player.next_loc = self.main_location.locations["merfolk's dwelling"]
            announce ("You entered the new area of the empire.")

        elif(verb == "north"):
            config.the_player.next_loc = self.main_location.locations["treasure room"]
            

        elif(verb == "south"):
            config.the_player.next_loc = self.main_location.locations["hunting ground"]
            announce ("You entered the new area of the empire.")
      
        elif (verb == "give"):
            # give medicine to crewmember
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (Ship().medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        Ship().medicine =  Ship().medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")
        else:
            announce ("Error: Ship object doe not understand verb " + verb)
class TreasureRoom (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = 'treasure room'
        
        self.verbs['exit'] = self
        self.verbs['take'] = self
        self.verbs['give'] = self
        
        
        self.event_chance = 100
       
    def enter(self):
        ship = config.the_player.ship
        description = ""
        if ship.get_key() < 1:
            announce("The area is locked. You need a key to the next area.")
            config.the_player.location = self.main_location.locations["deep water"]
            
        else: 
            announce('"Treasure Room" ')
            if ship.get_treasure() < 5:
                description = description + " You see a pile of treasures on the floor. Collect 5 treasures."
                announce (description)
                
    def process_verb (self, verb, cmd_list, nouns):
        ship = config.the_player.ship
        
        if(verb == "exit"):
            config.the_player.next_loc = self.main_location.locations["beach"]
            announce ("You return to the beach.")

        elif verb == "take":
            
            if ship.get_treasure() < 5:
                announce ("You collect the treasure.")
                amt = 1
                ship.treasure =  ship.treasure + amt
                self.go = True
                
            else:
                announce ("You don't see anything to take.")
                announce ("Enter command 'exit' to exit the empire.")
                
        elif (verb == "give"):
            if (len(cmd_list) > 3):
                if ((cmd_list[1] == "medicine") and (cmd_list[3] in nouns.keys())):
                    if (Ship().medicine > 0):
                        nouns[cmd_list[3]].receive_medicine(1)
                        Ship().medicine =  SHip().medicine - 1
                    else:
                        announce ("no more medicine to give")
            else:
                announce ("Give medicine to who?")
        
        else:
         announce("THere's no such command")
               
        
        
       # if(verb == "explore"):
           # config.the_player.next_loc = self.main_location.locations["hunting area"]
