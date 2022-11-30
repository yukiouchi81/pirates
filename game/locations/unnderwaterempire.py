from game import Location

class UnderwaterEmpire(Location.location):
    def __init__(self)
    self.name = "underwater empire"
    self.symbol = U
    self.visitable = True
    self.starting_location = Epipelagic(self)
    self.locations = {}
    self.locations["epipelagic"] = self.starting_location
    self.locations["mesopelagic"] = Mesopelagic(self)
    self.locations["bathypelagic"] = Bathypelagic(self)
    self.locations["abyssopelagic"] =Abyssopelagic(self)
    self.locations["hadalpelagic"] =Abyssopelagic(self)
    def enter(self, ):
        print("You found the entrance to an underground empire, what is your command?")


class Epipelagic ():
    def __init__ (self, m):
        super().__init__(m)
        self.name = "epipelagic"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self self.verbs['swim'] = self
        self.verbs['go deeper'] = self
        
        self.event_chance = 50
        self.events.append(giant_monster_squid.GiantMonsterSquid())
    def enter(self):
        announce("You entered epipelagic zone on the underwater empire.")

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["epipelagic"]
        if(verb == "go deeper"):
            config.the_player.next_loc = self.main_location.locations["mesopelagic"]

            

class Mesopelagic ():
    def __init__ (self, m):
        super().__init__(m)
        self.name = "mesopelagic"
        self.verbs['go deeper'] = self
        self.verbs['surface'] = self
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        
        
        self.event_chance = 50
       # self.events.append(seagull.Seagull())
    def enter(self):
        announce("You entered mesopelagic zone on the underwater empire.")

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["mesopelagic"]
        if(verb == "go deeper"):
            config.the_player.next_loc = self.main_location.locations["bathypelagic"]
        if (verb == "surface"):
            config.the_player.next_loc = self.main_location.locations["epipelagic"]
            

class Bathypelagic ():
    def __init__ (self, m):
        super().__init__(m)
        self.name = "bathypelagic"
        self.verbs['go deeper'] = self
        self.verbs['surface'] = self
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        
        self.event_chance = 50
       # self.events.append(seagull.Seagull())
    def enter(self):
        announce("You entered bathypelagic zone on the underwater empire.")

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["bathypelagic"]
        if(verb == "go deeper"):
            config.the_player.next_loc = self.main_location.locations["abyssopelagic"]
        if (verb == "surface"):
            config.the_player.next_loc = self.main_location.locations["mesopelagic"]
            


class Abyssopelagic ():
    def __init__ (self, m):
        super().__init__(m)
        self.name = "abyssopelagic"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['go deeper'] = self
        self.verbs['surface'] = self
        
        self.event_chance = 50
       #self.events.append(seagull.Seagull())
    def enter(self):
        announce("You entered bathypelagic zone on the underwater empire.")

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["abyssopelagic"]
        if(verb == "go deeper"):
            config.the_player.next_loc = self.main_location.locations["hadalpelagic"]
        if (verb == "surface"):
            config.the_player.next_loc = self.main_location.locations["bathypelagic"]
            
class Hadalpelagic ():
    def __init__ (self, m):
        super().__init__(m)
        self.name = "hadalpelagic"
        self.verbs['surface'] = self
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        
        self.event_chance = 50
        self.events.append(giant_monster_squid.GiantMonsterSquid())
    def enter(self):
        announce("You entered bathypelagic zone on the underwater empire.")

    def process_verb (self, verb, cmd_list, nouns):
        if(verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["hadalpelagic"]
        if (verb == "surface"):
            config.the_player.next_loc = self.main_location.locations["abyssopelagic"]
            
