import random
from time import sleep

class Weapons:
    """Completed by Matt
    Serves to describe the Weapons in the Arsenal of both players
    
        Args:
            self: initliazes the class
            """
    def __init__(self):
        """Initializes the class.
        
            Describes the arsenal, their power, their status, and uses."""
        self.arsenal = ["shield", "sword", "spear", "mace", "axe"]
        self.arsenalpwr = {"shield": 5, "sword": 5, "spear": 5, "mace": 5, "axe": 5}
        self.arsenalbreak = {"shield": False, "sword": False, "spear": False, "mace": False, "axe": False}
        self.shielduses = 5
        
    def arsenalstatus(self):
        """This is the status of the player's arsenal, which can be accessed during the game to view. We also keep track of the Shield's break status.
        
            """
        counter = 1
        for weapon in self.arsenalpwr:
            print(f"Object {counter} Name:", weapon) 
            print("\t Power:", self.arsenalpwr[weapon], 
                  "\t Broken:", self.arsenalbreak[weapon])
            counter += 1
            if weapon == "shield":
                print("\t Uses:", self.shielduses)
                
    def powerupall(self):
        """This function increases all weapons in the arsenal every time it is called"""
        self.arsenalpwr["sword"] += 1 #increase weapon by x
        self.arsenalpwr["spear"] += 1
        self.arsenalpwr["mace"] += 1
        self.arsenalpwr["axe"] += 1
        
        
    def shield(self, player, otherplayerweapon, otherplayer): # player is determinant by other class
        """This is the Shield object in the arsenal. It blocks damage from the opponent and heals its user. Unfortunately, they're boring, and if both players use it, 5 damage is dealt to both players.
            It can only be used 5 turns.
            
            Args:
                player: you, the real player
                otherplayer: computer player
                otherplayerweapon: the computer player's weapon used that turn"""
        if otherplayerweapon == "shield":
            player.subhp(5) #playerhp #playerhp is a variable
            #otherplayer.subhp(5) #otherhp
        else:
            player.addhp(5) #playerhp
        self.shielduses -= 1
        if self.shielduses == 0:
            self.arsenalbreak["shield"] = True
        
    def sword(self, player, otherplayerweapon, otherplayer): #hp needs to be called hp
        """The Sword is an object in the arsenal. Strong to mace but weak to axe.
        
            Args:
                player: you, the real player
                otherplayer: computer player
                otherplayerweapon: the computer player's weapon used that turn"""
        if otherplayerweapon == "mace":
            otherplayer.subhp(2 + self.arsenalpwr["sword"])
        elif otherplayerweapon == "axe":
            otherplayer.subhp(self.arsenalpwr["sword"] - 3)
        elif otherplayerweapon == "sword":
            chance = random.randint (0,1)
            if chance == 0:
                otherplayer.addhp(0)
            else:
                otherplayer.subhp(self.arsenalpwr["sword"])
        elif otherplayerweapon == "shield":
            pass
        else:
            otherplayer.subhp(self.arsenalpwr["sword"])
    
    def spear(self, player, otherplayerweapon, otherplayer):
        """The Spear is an object in the arsenal. Strong to axe but weak to mace.
        
            Args:
                player: you, the real player
                otherplayer: computer player
                otherplayerweapon: the computer player's weapon used that turn"""
        if otherplayerweapon == "axe":
            otherplayer.subhp(2 + self.arsenalpwr["spear"])
        elif otherplayerweapon == "mace":
            otherplayer.subhp(self.arsenalpwr["spear"] - 3)
        elif otherplayerweapon == "spear":
            chance = random.randint (0,1)
            if chance == 0:
                otherplayer.addhp(0)
            else:
                otherplayer.subhp(self.arsenalpwr["spear"])
        elif otherplayerweapon == "shield":
            pass
        else:
            otherplayer.subhp(self.arsenalpwr["spear"])

    def mace(self, player, otherplayerweapon, otherplayer):
        """The Mace is an object in the arsenal. Strong to spear but weak to sword.
        
            Args:
                player: you, the real player
                otherplayer: computer player
                otherplayerweapon: the computer player's weapon used that turn"""
        if otherplayerweapon == "spear":
            otherplayer.subhp(2 + self.arsenalpwr["mace"])
        elif otherplayerweapon == "sword":
            otherplayer.subhp(self.arsenalpwr["mace"] - 3)
        elif otherplayerweapon == "mace":
            chance = random.randint (0,1)
            if chance == 0:
                otherplayer.addhp(0)
            else:
                otherplayer.subhp(self.arsenalpwr["mace"])
        elif otherplayerweapon == "shield":
            pass
        else:
            otherplayer.subhp(self.arsenalpwr["mace"])
            
    def axe(self, player, otherplayerweapon, otherplayer):
        """The Axe is an object in the arsenal. Strong to sword but weak to spear.
        
            Args:
                player: you, the real player
                otherplayer: computer player
                otherplayerweapon: the computer player's weapon used that turn"""
        if otherplayerweapon == "sword":
            otherplayer.subhp(2 + self.arsenalpwr["axe"])
        elif otherplayerweapon == "spear":
            otherplayer.subhp(self.arsenalpwr["axe"] - 3)
        elif otherplayerweapon == "axe":
            chance = random.randint (0,1)
            if chance == 0:
                otherplayer.addhp(0)
            else:
                otherplayer.subhp(self.arsenalpwr["axe"]) 
        elif otherplayerweapon == "shield":
            pass   
        else:
            otherplayer.subhp(self.arsenalpwr["axe"])

class Player:
    """Completed by Matt
    
    This class controls each player's HP, storing it, adding to or subtracting from it. We also give the players their moves in this class, with the human player being prompted with an input."""
    def __init__(self, weapons):
        """Initilizing the object.
        
            Args:
                self: initialization 
                weapons: from the Weapons class"""
        self.weapons = weapons
        self.hp = 100
    
    def addhp(self, dmgvalue):
        """Adding HP to a Player
            
            Args:
                self: initialization
                dmgvalue: integer, the value of the damage dealt"""
        self.hp += dmgvalue
        if self.hp >= 100:
            self.hp = 100
    
    def subhp(self, dmgvalue):
        """Subtracting HP from a Player
            
            Args:
                self: initialization
                dmgvalue: integer, the value of the damage dealt"""
        self.hp -= dmgvalue
        if self.hp <= 0:
            self.hp = 0
            
    def getplayermove(self):
        """Player is prompted with a choice for their turn, choosing to view the status page, or choosing a weapon for the next Round of the battle.
        
            Returns:
                Choice: either the status of the arsenal or a weapon from the arsenal, resulting in gameplay for the round
                Prints: an error in the form of a formatted string if an input is invalid"""
        choice = input("Player, pick your Weapon! [shield, sword, spear, mace, axe]")
        if choice == "status":
            return choice
        while choice not in self.weapons.arsenal or self.weapons.arsenalbreak[choice] or (choice == "shield" and self.weapons.shielduses == 0):
            print("Something doesn't seem quite right. Use a weapon that exists in your Arsenal. Try Again!\n")
            sleep(2.0)
            choice = input("Player, pick your Weapon! [shield, sword, spear, mace, axe]")
            if choice == "status":
                return choice
        return(choice)
    
    def getcompmove(self):
        """Computer player randomly chooses a weapon from the arsenal to play."""
        compmove = random.choice(self.weapons.arsenal)
        while compmove not in self.weapons.arsenal or self.weapons.arsenalbreak[compmove] or (compmove == "shield" and self.weapons.shielduses == 0):
            compmove = random.choice(self.weapons.arsenal)
        return(compmove)

class Specials:
    """Special moves that players have access to. (Methods created by Nasim)"""
    
    def p1_super_attack(self, opponent, Player1):
        """Player 1 has a random chance to deal 10-20 extra damage to Player2.
        Args:
            opponent (Player): The computer player
        Side effects:
            prints to let the player know that they've dealt extra damage and informs them how much hp Player 2 lost.
        """
        if random.randint(1,20) == 20:
            extra_damage = random.randint(10,20)
            opponent.subhp(extra_damage)
            print(f"You have performed a super attack! Ser Gregor has lost {extra_damage} hp!")
            Player1.weapons.powerupall()
            Player1.weapons.arsenalstatus()
        else:
            pass
    
    def comp_super_attack(self, opponent, Player2):
        """Player 2 (computer player) has a random chance to deal 10-20 extra damage to Player 1.
        Args:
            opponent (Player): The human player
        Side effects:
            prints to let the player know that they've lost extra damage and how much hp they've lost.
        """
        if random.randint(1,20) == 20:
            extra_damage = random.randint(10,20)
            opponent.subhp(extra_damage)
            print(f"Ser Gregor has performed a super attack! You lost {extra_damage} hp!")
            Player2.weapons.powerupall()
        else:
            pass
    
    def p1_super_heal(self, player):
        """Player 1 has a random chance to gain 10-20 hp.
        Side effects:
            Prints to let the player know how much hp they've gained.
        """
        if random.randint(1,20) == 20:
            gained_health = random.randint(10,20)
            player.addhp(gained_health)
            print(f"You have performed a super heal! You've gained {gained_health} hp!")
        else:
            pass
    
    def comp_super_heal(self, player):
        """Player 2 has a random chance to gain 10-20 hp.
        Side effects:
            Prints to let the player know how much hp Player 2 gained.
        """
        if random.randint(1,20) == 20:
            gained_health = random.randint(10,20)
            player.addhp(gained_health)
            print(f"Ser Gregor has performed a super heal! He gained {gained_health} hp!")
        else:
            pass

    def p1_breaking(self, arsenal):
        """Player 1 has a chance of breaking up to 3 weapons, excluding their shield.
        Args:
            arsenal (list): list of weapons the players have access to.
        Side effects:
            prints to let the player know which weapon has broken.
        Returns:
            list: the player's new arsenal excluding their broken weapons.
        """
        broke = 0
        while broke <= 3:
            if random.randint(1,40) == 40:
                new_arsenal = [self.arsenal.pop(x) for x in arsenal if x != "shield"]
                broke += 1
                broken_weapon = list(set(arsenal) - set(new_arsenal))
                print(f"Your {broken_weapon} broke! Continue the battle without it!")

                return new_arsenal
            else:
                pass
    
    def comp_breaking(self, arsenal):
        """Player 2 has a chance of breaking up to 3 weapons, excluding their shield.
        Args:
            arsenal (list): list of weapons the computer player has access to.
        Side effects:
            prints to let the player know which weapon Player 2 has broken.
        Returns:
            list: the computer player's new arsenal excluding their broken weapons.
        """
        broke = 0
        while broke <= 3:
            if random.randint(1,40) == 40:
                new_arsenal = [self.arsenal.pop(x) for x in arsenal if x != "shield"]
                broke += 1
                broken_weapon = (list(set(arsenal) - set(new_arsenal)))[0]
                print(f"Ser Gregor's {broken_weapon} broke! Lucky you!")
                return new_arsenal
            else:
                pass
    

def intro():
    """Introduces the game to the player.
    
    Side effects:
        prints the instructions of the game.
        
    (Function created by Nasim)
    """
    while True:
        print("Here's how the battle will go. You will choose between four weapons: a sword, a spear, an axe, and a mace.\n")
        sleep(1.5)
        print("A sword will beat an opponent's mace. A mace will beat their spear. A spear will beat their axe. And an axe will beat their sword. You will deal equal damage if you both use the same weapon, but there's a chance you both will miss.\n")
        sleep(1.5)
        print("You have the option of using a shield (which may grant you a couple hp) but use it wisely! Your shield can only get hit 5 times before breaking. If it breaks, then you'll only have luck by your side weakling.\n")
        sleep(1.5)
        print("If you both use your shield, you'll both take damage as the crowd will throw rocks. THEY WANT AN ENTERTAINING SHOW SO YOU BETTER GIVE IT TO THEM!\n")
        response = input("Do you understand the rules? (yes or no): ")
        if response == "yes" or response == "yessir" or response == "yup" or response == "y":
            break
        else:
            print("\nHmmm, so you are weak and stupid... I will repeat myself then! LISTEN CAREFULLY!\n")
            sleep(4.0)
            continue
    print("\nYou seem ready now... LET THE GAMES BEGIN!! \n\n")
    sleep(3.0)

def main():
    """Begins by continuing the instroduction and then allows the entire game to run. 
    
    Side effects:
        Prints more introduction parts.
        Creates instances of the player class for both players.
        Prints each round number and each player's hp + choice of weapon.
    (Function created by Nasim + Matt)
    """
    print("Welcome to the Medieval Ages!\nI'm Gordo, the King's right hand!\n")
    sleep(2.0)
    print("We are throwing you into battle against the powerful and undefeated Ser Gregor Clegane! \nWill you fight for your honor and win the battle? SHOW US WHAT YOU GOT!\n")
    sleep(3.0)
    name = input("Before we begin, what should we call you weakling?")
    print(f"Hmm... Your name is {name}? Sounds interesting...\n")
    sleep(3.0)
    print(f"INTERESTINGLY STUPID!! We will call you weakling unless you prove yourself to be worthy of being called {name}.\n")
    sleep(3.0)
    intro()

    roundnum = 1
    
    Player1 = Player(Weapons())
    Player2 = Player(Weapons())
    special_move = Specials()

    while Player1.hp > 0 and Player2.hp > 0:
        print(f"Round {roundnum}")
        Player1move = Player1.getplayermove()
        Player2move = Player2.getcompmove()

        if Player1move == "status":
            Player1.weapons.arsenalstatus()
            continue
        if Player1move == "mace":
            Player1.weapons.mace(Player1, Player2move, Player2)
            special_move.p1_super_attack(Player2, Player1)
            #special_move.p1_breaking(Player1.weapons)

        elif Player1move == "shield":
            Player1.weapons.shield(Player1, Player2move, Player2)
            special_move.p1_super_heal(Player1)

        elif Player1move == "sword":
            Player1.weapons.sword(Player1, Player2move, Player2)
            special_move.p1_super_attack(Player2, Player1)
           # special_move.p1_breaking(Player1.weapons)

        elif Player1move == "spear":
            Player1.weapons.spear(Player1, Player2move, Player2)
            special_move.p1_super_attack(Player2, Player1)
           # special_move.p1_breaking(Player1.weapons)

        elif Player1move == "axe":
            Player1.weapons.axe(Player1, Player2move, Player2)
            special_move.p1_super_attack(Player2, Player1)
           # special_move.p1_breaking(Player1.weapons)

            
        if Player2move == "mace":
            Player2.weapons.mace(Player2, Player1move, Player1)
            special_move.comp_super_attack(Player1, Player2)
           # special_move.comp_breaking(Player2.weapons)
            roundnum += 1

        elif Player2move == "shield":
            Player2.weapons.shield(Player2, Player1move, Player1)
            special_move.comp_super_heal(Player2)
            roundnum += 1
            
        elif Player2move == "sword":
            Player2.weapons.sword(Player2, Player1move, Player1)
            special_move.comp_super_attack(Player1, Player2)
           # special_move.comp_breaking(Player2.weapons)
            roundnum += 1

        elif Player2move == "spear":
            Player2.weapons.spear(Player2, Player1move, Player1)
            special_move.comp_super_attack(Player1, Player2)
          #  special_move.comp_breaking(Player2.weapons)
            roundnum += 1

        elif Player2move == "axe":
            Player2.weapons.axe(Player2, Player1move, Player1)
            special_move.comp_super_attack(Player1, Player2)
           # special_move.comp_breaking(Player2.weapons)
            roundnum += 1
        
        print(f"{name} chose:", Player1move)
        print("Ser Gregor chose:", Player2move)
        print(f"{name}'s HP", Player1.hp)
        print("Ser Gregor's HP", Player2.hp, "\n")
        sleep(2.0)
        continue
        
    if Player1.hp <= 0 and Player2.hp <= 0:
        print("\nIt seems that both of our fighters have met their match... It's a Draw")
    elif Player1.hp <= 0:
        print("\nYou Lose, scoundrel! Sir Gregor Clegane remains undefeated! Better luck next time...")
    else:
        print(f"\nUNBELIEVABLE! YOU'VE WON!! Sir Gregor Clegane is no longer undefeated. You are not a weakling... \nYou, {name}, are now a Medieval Legend! But will you last?...")

if __name__ == "__main__":
    main()
    
# Completed by Nasim Mahdi & Matt Ober (mober18)
