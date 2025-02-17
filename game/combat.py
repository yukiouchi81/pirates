import random
import game.config as config
from game.display import announce
from game.display import menu
from game.crewmate import CrewMate
from game.context import Context


class Attack():
    def __init__ (self, name, description, success, damage_range):
        self.name = name
        self.description = description
        self.success = success
        self.damage_range = damage_range
    
    def __eq__(self, other):
        if not isinstance(other, Attack):
            return False
        if self.name == other.name and self.description == other.description and self.success == other.success and self.damage_range == other.damage_range:
            return True
        return False
        
    
class Combat():

    def __init__ (self, monsters):
        self.monsters = monsters

    def process_verb (self, verb, cmd_list, nouns):
        print (self.nouns + " can't " + verb)

    def combat (self):
        while len(self.monsters):
            combatants = config.the_player.get_pirates() + self.monsters
            min_t = None
            for c in combatants:
                t = (100 - c.cur_move)/c.speed
                if min_t == None:
                    min_t = t
                else:
                    min_t = min(t, min_t)
            for c in combatants:
                c.cur_move += c.speed*min_t
            speeds = [c.cur_move for c in combatants]
            max_move = max(speeds)
            ready = [c for c in combatants if c.cur_move == max_move]
            moving = random.choice(ready)
            moving.cur_move = 0
            options = []
            attacks = []
            items = []
            if isinstance(moving, CrewMate):
                announce(moving.name + " has seized  the initiative! What should they do?",pause=False)
                for t in self.monsters:
                    options.append("attack " + t.name)
                choice = menu (options)
                chosen_target = self.monsters[choice]

                options = []
                if "brawling" in moving.skills.keys():
                    options.append("punch")
                    attacks.append(Attack("punch", "punches", moving.skills["brawling"], (1,11)))
                    items.append(None)
                for i in moving.items:
                    if i.damage[1] > 0 and i.verb != None and i.skill in moving.skills.keys() and (i.firearm == False or i.charge == True):
                        putative_attk = Attack(i.name, i.verb2, moving.skills[i.skill], i.damage)
                        if putative_attk not in attacks:
                            options.append(i.verb + " with " + i.name)
                            attacks.append(putative_attk)
                            items.append(i)
                if len(attacks) > 0:
                    choice = menu (options)
                    chosen_attk = attacks[choice]
                    chosen_item = items[choice]
                    if chosen_item != None and chosen_item.firearm == True:
                        chosen_item.charge = False
                #else: run in circles, scream and shout
            else:
                chosen_target = random.choice(config.the_player.get_pirates())
                for key in moving.attacks.keys():
                    attacks.append(Attack(key, moving.attacks[key][0], moving.attacks[key][1], moving.attacks[key][2]))
                chosen_attk = random.choice(attacks)
            roll = random.randrange(100)
            if moving.lucky == True:
                roll = min(roll, random.randrange(100))
            if roll < chosen_attk.success + 10:
                announce (moving.name + " " + chosen_attk.description + " " + chosen_target.name + "!")
                damage = random.randrange(chosen_attk.damage_range[0],chosen_attk.damage_range[1]+1)
                deathcause = "slain by a " + moving.name + "'s " + chosen_attk.name
                chosen_target.inflict_damage(damage, deathcause)
                print(str(damage)+" damege to "+str(chosen_target.name))
                if chosen_target.health <= 0:
                    announce (chosen_target.name + " is killed!")
                else:
                    announce ("Remaining HP of "+chosen_target.name + ": " + str(chosen_target.health))
                
                    
            elif (roll == chosen_attk.success +10):
                announce (moving.name + " barely misses " + chosen_target.name + "!")
            else:
                announce (moving.name + " misses " + chosen_target.name + ".")
            self.monsters = [m for m in self.monsters if m.health >0]

        

class Monster:
    def __init__ (self, name, hp, attacks, speed):
        self.name = name
        self.health = hp
        self.attacks = attacks
        self.speed = speed
        self.cur_move = 0
        self.lucky = False
    
    def inflict_damage (self, num, deathcause):
        self.health = self.health - num
        if(self.health > 0):
            return False
        return True
    
class Sharks(Monster):
    def __init__ (self,name):
        attacks = {}
        attacks["bite"] = ["bites",random.randrange(80,90), (10,15)]
        attacks["bite2"] = ["bites",random.randrange(80,90), (10,15)]
        attacks["tail attack"] = ["tail attack",random.randrange(30,40), (15,20) ]
        #7 to 19 hp, bite attack, 160 to 200 speed (100 is "normal")
        super().__init__(name, random.randrange(10,15), attacks, 180 + random.randrange(-20,21))
        #Methods of the parent class are called from the child class.
    
class Macaque(Monster):
    def __init__ (self, name):
        attacks = {}
        attacks["bite"] = ["bites",random.randrange(70,100), (5,9)]
        #7 to 19 hp, bite attack, 160 to 200 speed (100 is "normal")
        super().__init__(name, random.randrange(7,10), attacks, 200 + random.randrange(-20,21))
        #Methods of the parent class are called from the child class.
class Drowned(Monster):
    def __init__ (self, name):
        attacks = {}
        attacks["bite"] = ["bites",random.randrange(35,51), (5,15)]
        attacks["punch 1"] = ["punches",random.randrange(35,51), (1,10)]
        attacks["punch 2"] = ["punches",random.randrange(35,51), (1,10)]
        #7 to 19 hp, bite attack, 65 to 85 speed (100 is "normal")
        super().__init__(name, random.randrange(15,20), attacks, 100 + random.randrange(-10,11))

class Giant(Monster):
    def __init__(self,name):
        attacks = {}
        attacks["tackle"] = ["tackles",100, (25,35) ]
        attacks["hydro cannon"] = ["bursts hydro cannon",random.randrange(40,50), (65,80) ]
        
        super().__init__(name, random.randrange(300,330), attacks, 250 + random.randrange(-10,11))
        
class Merfolks(Monster):
    def __init__(self,name):
        attacks = {}
        attacks["slash"] = ["slashes",random.randrange(30,40), (20,25) ]
        attacks["supersonic wave"] = ["emits the supersonic wave",100, (5,15) ]
        attacks["supersonic wave"] = ["emits the supersonic wave",100, (5,15) ]
        super().__init__(name, random.randrange(30,50), attacks, 130 + random.randrange(-10,11))
