"""
  ___________
< Battleshell >
  ^^^^^^^^^^^
by Jason
Ver: 1.0
"""
import random
dead = False
win = False
Game = True
Round = False
Mainturn = False
Enemyturn = False
Roundcheck = True
CharSelect = True
FoerSelect = True
MainHPbar = bin(100)
EnemyHPbar = bin(100)
Turn = int(2)
"""Instructions of how to make custom character
(Making character)
class demo:
    name = "demo"
    # Changing stats:
    HP = int(100)
    Atk = int(10)
    Def = int(10)
    Spd = int(10)
    # Base stats:
    bHP = int(100)
    bAtk = int(10)
    bDef = int(10)
    bSpd = int(10)
    # Character dialog:
    dAtk = "Attack dialogue"
    dAtt = "Attack successful dialogue"
    Miss = "Attack unsuccessful dialogue"
    Fail = "Skill unsuccessful dialogue"
    dSpd = "Speed increase dialogue"
    dDef = "Defence increase dialogue"
    dDog = "Dodge successful dialogue"
    dHit = "Hurt dialogue"
    Attempt = "Skill attempt dialogue"
    (add character specific skill dialogues here)
    # Character skills:
    SKILL = ["skill-name-1", "skill-name-2", "skill-name-3"]
    
    (example of a skill)
    def skill1(self):  # skill-name-1 (this skill increases the character's speed)
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance > 20:
            self.Spd = round(self.Spd * 1.1)
            print(self.dSpd)
        else:
            print(self.Fail)
"""


# Characters start
# Stock Characters:
class Fox:
    name = "The Fox"
    # Changing stats:
    HP = int(80)
    Atk = int(9)
    Def = int(5)
    Spd = int(18)
    # Base stats:
    bHP = int(80)
    bAtk = int(9)
    bDef = int(5)
    bSpd = int(18)
    # Character dialog:
    dAtk = "The Fox attempts to scratch the foe with claws!"
    dAtt = "The Fox manages to land its attack!"
    Miss = "The Fox misses!"
    Fail = "The Fox fails!"
    dSpd = "The Fox boosts its speed!!"
    dDef = "The Fox increases its defence!"
    dDog = "The Fox manages to dodge the attack!"
    dHit = "The Fox is hit!"
    Attempt = "The Fox attempts to use a skill...\n"
    sBSm = "The Fox throws its body at the enemy!"
    sFa1 = "The Fox applies First Aid... It was super effective!"
    sFa2 = "The Fox applies First Aid... It got all its health back."
    sFa3 = "The Fox applies First Aid... It restored quite some health points"
    sFa4 = "The Fox applies First Aid... It restored some health points"
    # Character skills:
    SKILL = ["Speedier", "Body-Slam", "First-Aid"]

    def skill1(self):  # Speedier
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance > 20:
            self.Spd = round(self.Spd * 1.1)
            print(self.dSpd)
        else:
            print(self.Fail)

    def skill2(self):  # Body-Slam
        if Mainturn is True:
            hit = random.randint(1, Enemy.Spd)
            print(self.Attempt)
            if self.Spd > hit:
                Enemy.HP = (Enemy.HP - (self.Atk + (self.Spd / 2)))
                print(self.sBSm)
            else:
                print(self.Fail)
        elif Enemyturn is True:
            dodge = random.randint(1, Main.Spd)
            print(self.Attempt)
            if self.Spd > dodge:
                Main.HP = (Main.HP - (self.Atk + (self.Spd / 2)))
                print(self.sBSm)
            else:
                print(self.Fail)

    def skill3(self):  # First-Aid
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance == 100:
            self.HP = (self.HP + self.bHP)
            print(self.sFa1)
        elif chance > 90:
            self.HP = self.bHP
            print(self.sFa2)
        elif chance > 75:
            self.HP = (self.HP + 25)
            print(self.sFa3)
        elif chance > 45:
            self.HP = (self.HP + 10)
            print(self.sFa4)
        else:
            print(self.Fail)


class Werewolf:
    name = "The Werewolf"
    # Changing stats:
    HP = int(120)
    Atk = int(17)
    Def = int(15)
    Spd = int(10)
    # Base stats:
    bHP = int(120)
    bAtk = int(17)
    bDef = int(15)
    bSpd = int(10)
    # Character dialog:
    dAtk = "The Werewolf attempts to bite the foe!"
    dAtt = "The Werewolf succeeds in its attack!"
    Miss = "The Werewolf misses!"
    Fail = "The Werewolf fails!"
    dSpd = "The Werewolf increases its speed!"
    dDef = "The Werewolf increases its defence!"
    dDog = "The Werewolf dodges the attack!"
    dHit = "The Werewolf is hit!"
    Attempt = "The Werewolf attempts to use a skill...\n"
    sPu1 = "The Werewolf sucker-punches the foe!"
    sPu2 = "The Werewolf punches the foe!"
    sPOW = "The Werewolf becomes even more powerful with the cost of its defence!!"
    # Character skills
    SKILL = ["Iron-Armor", "Sucker-Punch", "Full-Moon"]

    def skill1(self):  # Iron-Armor
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance > 15:
            self.Def = round(self.Def * 1.15)
            print(self.dDef)
        else:
            print(self.Fail)

    def skill2(self):  # Sucker-Punch
        if Mainturn is True:
            chance = random.randint(1, 100)
            hit = random.randint(1, Enemy.Spd)
            if self.Spd > hit:
                if chance > 75:
                    Enemy.HP = (Enemy.HP - (50 + self.Atk))
                    print(self.sPu1)
                elif chance > 25:
                    Enemy.HP = (Enemy.HP - round(10 + (self.Atk / 2)))
                    print(self.sPu2)
                else:
                    print(self.Miss)
            else:
                print(self.Miss)
        elif Enemyturn is True:
            chance = random.randint(1, 100)
            dodge = random.randint(1, Main.Spd)
            if self.Spd > dodge:
                if chance > 75:
                    Main.HP = (Main.HP - (50 + self.Atk))
                    print(self.sPu1)
                elif chance > 25:
                    Main.HP = (Main.HP - round(10 + (self.Atk / 2)))
                    print(self.sPu2)
                else:
                    print(self.Miss)
            else:
                print(self.Miss)

    def skill3(self):  # Full-Moon
        chance = random.randint(1, 100)
        if chance > 50:
            self.Def = round(self.Def / 5)
            self.Atk = (self.Atk * 3)
            print(self.sPOW)
        else:
            print(self.Fail)


class Cougar:
    name = "The Cougar"
    # Changing stats:
    HP = int(60)
    Atk = int(22)
    Def = int(10)
    Spd = int(17)
    # Base stats:
    bHP = int(60)
    bAtk = int(22)
    bDef = int(10)
    bSpd = int(17)
    # Character dialog:
    dAtk = "The Cougar attempts to bite the foe!"
    dAtt = "The Cougar succeeds in its attack!"
    Miss = "The Cougar misses!"
    Fail = "The Cougar fails!"
    dSpd = "The Cougar increases its speed!"
    dDef = "The Cougar increases its defence!"
    dDog = "The Cougar dodges the attack!"
    dHit = "The Cougar is hit!"
    Attempt = "The Cougar attempts to use a skill...\n"
    sLAL = "The Cougar increases size, increasing all stats greatly with the cost of speed!"
    sLAx = "The Cougar increases size, increasing all stats with the cost of speed!"
    sOnU = "The Cougar heals itself!"
    # Character skills
    SKILL = ["Laugh-At-Life", "Speed-boost", "One-Up"]

    def skill1(self):  # Laugh-At-Life
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance > 95:
            self.HP = (self.HP + (self.bHP * 3))
            self.Atk = (self.Atk + (self.bAtk * 2))
            self.Def = (self.Def + (self.bDef * 2))
            self.Spd = round(self.Spd / 2)
            print(self.sLAL)
        elif chance > 75:
            self.HP = (self.HP + self.bHP)
            self.Atk = (self.Atk + self.bAtk)
            self.Def = (self.Def + self.bDef)
            self.Spd = round(self.Spd / 2)
            print(self.sLAx)
        else:
            print(self.Fail)

    def skill2(self):  # Speed-boost
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance > 50:
            self.Spd = (self.Spd + 10)
            print(self.dSpd)
        elif chance > 10:
            self.Spd = (self.Spd + 3)
            print(self.dSpd)
        else:
            print(self.Fail)

    def skill3(self):  # One-Up
        chance = random.randint(1, 100)
        print(self.Attempt)
        if chance > 50:
            self.HP = (self.HP + self.bHP)
            print(self.sOnU)
        else:
            print(self.Fail)
# Custom Characters:
# Characters end


# Functions start
def attack():
    if Mainturn is True:
        hit = random.randint(0, Enemy.Spd)
        print(Main.dAtk)
        if Main.Spd > hit:
            print(Main.dAtt)
            matk = (Main.Atk + (Main.Atk / Enemy.Def))
            Enemy.HP = (Enemy.HP - int(matk))
        else:
            print(Main.Miss)
    elif Enemyturn is True:
        dodge = random.randint(0, Main.Spd)
        print(Enemy.dAtk)
        if Enemy.Spd > dodge:
            print(Main.dHit)
            eatk = (Enemy.Atk + (Enemy.Atk / Main.Def))
            Main.HP = (Main.HP - int(eatk))
        else:
            print(Main.dDog)


def skill(x):
    if Mainturn is True:
        if x == "1":
            Main.skill1()
        elif x == "2":
            Main.skill2()
        elif x == "3":
            Main.skill3()
    elif Enemyturn is True:
        if x == "1":
            Enemy.skill1()
        elif x == "2":
            Enemy.skill2()
        elif x == "3":
            Enemy.skill3()


def skip():
    if Mainturn is True:
        print("You skipped your turn!")
    elif Enemyturn is True:
        print("{} skips a turn!".format(Enemy.name))


def death():
    if Enemyturn is True:
        print("{} loses!".format(Enemy.name))
# Functions end


Em = "~empty slot~"
CL = ["Werewolf", "Fox", "Cougar", Em, Em, Em, Em, Em, Em, Em]  # Add custom character by replacing Em with Class name
# User choice of character:
while CharSelect is True:
    Character = input("Pick your character:"
                      "\n- {0}"
                      "\n- {1}"
                      "\n- {2}"
                      "\n- {3}"
                      "\n- {4}"
                      "\n- {5}"
                      "\n- {6}"
                      "\n- {7}"
                      "\n- {8}"
                      "\n- {9}"
                      "\nYour character of choice: "
                      .format(CL[0], CL[1], CL[2], CL[3], CL[4], CL[5], CL[6], CL[7], CL[8], CL[9]))
    if Character in ["Werewolf", "werewolf", "WEREWOLF"]:
        print("You selected the Werewolf!")
        Main = Werewolf()
        del CL[0]
        CharSelect = False
    elif Character in ["Fox", "fox", "FOX"]:
        print("You selected the Fox!")
        Main = Fox()
        del CL[1]
        CharSelect = False
    elif Character in ["Cougar", "cougar", "COUGAR"]:
        print("You selected the Cougar!")
        Main = Cougar()
        del CL[2]
        CharSelect = False
    elif Character in "emptyEMPTY":
        print("Empty space, add custom character then implement to this slot to use!"
              "\nSee code for instructions")
    else:
        print("Choose one of the listed characters!")
    """implementing character:
    elif Character in [(class name)]:
        print("You selected (character)!")
        Main = (class name)()
        del CL[n]
        CharSelect = False
    """
# Computer's choice
while FoerSelect is True:
    FoeSelect = random.randint(0, (len(CL) - 1))
    if CL[FoeSelect] == "Werewolf":
        Enemy = Werewolf()
        FoerSelect = False
    elif CL[FoeSelect] == "Fox":
        Enemy = Fox()
        FoerSelect = False
    elif CL[FoeSelect] == "Cougar":
        Enemy = Cougar()
        FoerSelect = False
    elif CL[FoeSelect] == Em:
        FoeSelect = random.randint(0, (len(CL) - 1))
    else:
        print("There seems to be too little characters to play this game!"
              "\nYou need at least 2!")
        Roundcheck = False
        Game = False
    """implementing character for computer
    elif CL[FoeSelect] == "(class name)":
        Enemy = (class name)()
        FoerSelect = False
    """
print("Welcome to BattleShell! The customizable turn-based battle game!")
while Game is True:
    Healthcheck = True
    MainCheck = True
    EnemyCheck = True
    if Turn == 2:
        Roundcheck = True
        Turn = int(0)
    Round = True
    while Roundcheck is True:
        if Main.Spd > Enemy.Spd:
            Mainturn = True
            Enemyturn = False
            Roundcheck = False
        else:
            Mainturn = False
            Enemyturn = True
            Roundcheck = False
    while Healthcheck is True:
        if MainCheck is True:
            Main.pHP = round((Main.HP / Main.bHP) * 100)
            if Main.pHP >= 100:
                MainHPbar = "████████████████████"
                MainCheck = False
            elif Main.pHP >= 95:
                MainHPbar = "███████████████████_"
                MainCheck = False
            elif Main.pHP >= 90:
                MainHPbar = "██████████████████__"
                MainCheck = False
            elif Main.pHP >= 85:
                MainHPbar = "█████████████████___"
                MainCheck = False
            elif Main.pHP >= 80:
                MainHPbar = "████████████████____"
                MainCheck = False
            elif Main.pHP >= 75:
                MainHPbar = "███████████████_____"
                MainCheck = False
            elif Main.pHP >= 70:
                MainHPbar = "██████████████______"
                MainCheck = False
            elif Main.pHP >= 65:
                MainHPbar = "█████████████_______"
                MainCheck = False
            elif Main.pHP >= 60:
                MainHPbar = "████████████________"
                MainCheck = False
            elif Main.pHP >= 55:
                MainHPbar = "███████████_________"
                MainCheck = False
            elif Main.pHP >= 50:
                MainHPbar = "██████████__________"
                MainCheck = False
            elif Main.pHP >= 45:
                MainHPbar = "█████████___________"
                MainCheck = False
            elif Main.pHP >= 40:
                MainHPbar = "████████____________"
                MainCheck = False
            elif Main.pHP >= 35:
                MainHPbar = "███████_____________"
                MainCheck = False
            elif Main.pHP >= 30:
                MainHPbar = "██████______________"
                MainCheck = False
            elif Main.pHP >= 25:
                MainHPbar = "▓▓▓▓▓_______________"
                MainCheck = False
            elif Main.pHP >= 20:
                MainHPbar = "▓▓▓▓________________"
                MainCheck = False
            elif Main.pHP >= 15:
                MainHPbar = "▓▓▓_________________"
                MainCheck = False
            elif Main.pHP >= 10:
                MainHPbar = "░░__________________"
                MainCheck = False
            elif Main.pHP >= 5:
                MainHPbar = "░___________________"
                MainCheck = False
            else:
                MainHPbar = "____________________"
                MainCheck = False
        elif EnemyCheck is True:
            Enemy.pHP = round((Enemy.HP / Enemy.bHP) * 100)
            if Enemy.pHP >= 100:
                EnemyHPbar = "████████████████████"
                EnemyCheck = False
            elif Enemy.pHP >= 95:
                EnemyHPbar = "███████████████████_"
                EnemyCheck = False
            elif Enemy.pHP >= 90:
                EnemyHPbar = "██████████████████__"
                EnemyCheck = False
            elif Enemy.pHP >= 85:
                EnemyHPbar = "█████████████████___"
                EnemyCheck = False
            elif Enemy.pHP >= 80:
                EnemyHPbar = "████████████████____"
                EnemyCheck = False
            elif Enemy.pHP >= 75:
                EnemyHPbar = "███████████████_____"
                EnemyCheck = False
            elif Enemy.pHP >= 70:
                EnemyHPbar = "██████████████______"
                EnemyCheck = False
            elif Enemy.pHP >= 65:
                EnemyHPbar = "█████████████_______"
                EnemyCheck = False
            elif Enemy.pHP >= 60:
                EnemyHPbar = "████████████________"
                EnemyCheck = False
            elif Enemy.pHP >= 55:
                EnemyHPbar = "███████████_________"
                EnemyCheck = False
            elif Enemy.pHP >= 50:
                EnemyHPbar = "██████████__________"
                EnemyCheck = False
            elif Enemy.pHP >= 45:
                EnemyHPbar = "█████████___________"
                EnemyCheck = False
            elif Enemy.pHP >= 40:
                EnemyHPbar = "████████____________"
                EnemyCheck = False
            elif Enemy.pHP >= 35:
                EnemyHPbar = "███████_____________"
                EnemyCheck = False
            elif Enemy.pHP >= 30:
                EnemyHPbar = "██████______________"
                EnemyCheck = False
            elif Enemy.pHP >= 25:
                EnemyHPbar = "▓▓▓▓▓_______________"
                EnemyCheck = False
            elif Enemy.pHP >= 20:
                EnemyHPbar = "▓▓▓▓________________"
                EnemyCheck = False
            elif Enemy.pHP >= 15:
                EnemyHPbar = "▓▓▓_________________"
                EnemyCheck = False
            elif Enemy.pHP >= 10:
                EnemyHPbar = "░░__________________"
                EnemyCheck = False
            elif Enemy.pHP >= 5:
                EnemyHPbar = "░___________________"
                EnemyCheck = False
            else:
                EnemyHPbar = "____________________"
                EnemyCheck = False
        else:
            Healthcheck = False
    print("\n==========================="
          "\n||YOU||"
          "\n{0}"
          "\n[{2}]{4}"
          "\n{6}/{7}"
          "\n==========================="
          "\n||FOE||"
          "\n{1}"
          "\n[{3}]{5}"
          "\n{8}/{9}"
          "\n==========================="
          .format(Main.name, Enemy.name, MainHPbar, EnemyHPbar, Main.pHP, Enemy.pHP, Main.HP, Main.bHP, Enemy.HP,
                  Enemy.bHP))
    while Round is True:
        if Turn == 2:
            Round = False
        elif Mainturn is True:
            if Main.HP > 0:
                Mainevent = True
                while Mainevent is True:
                    Act = input("\nIt's your turn! What do you do?"
                                "\nAttack or Skill?"
                                "\nYour choice: ")
                    if Act in ["Attack", "attack", "ATTACK"]:
                        attack()
                        Turn = (Turn + 1)
                        Mainturn = False
                        Enemyturn = True
                        Mainevent = False
                    elif Act in ["Skill", "skill", "SKILL"]:
                        Input = True
                        while Input is True:
                            x = input("\nChoose a skill:"
                                      "\n1: {0}"
                                      "\n2: {1}"
                                      "\n3: {2}"
                                      "\nYour choice: "
                                      .format(Main.SKILL[0], Main.SKILL[1], Main.SKILL[2]))
                            if x in ["1", "2", "3"]:
                                skill(x)
                                Turn = (Turn + 1)
                                Mainturn = False
                                Enemyturn = True
                                Mainevent = False
                                Input = False
                            else:
                                print("Choose from the skills please!")
                    else:
                        print("Attack or Skip only!")
            else:
                death()
                dead = True
                Turn = int(2)
                Game = False
                Round = False
                Mainturn = False
        elif Enemyturn is True:
            if Enemy.HP > 0:
                Enemyevent = True
                while Enemyevent is True:
                    EnemyAct = random.randint(1, 5)
                    if EnemyAct == 1:
                        attack()
                        Turn = (Turn + 1)
                        Enemyturn = False
                        Mainturn = True
                        Enemyevent = False
                    elif EnemyAct == 2:
                        skip()
                        Turn = (Turn + 1)
                        Enemyturn = False
                        Mainturn = True
                        Enemyevent = False
                    elif EnemyAct == 3:
                        skill("1")
                        Turn = (Turn + 1)
                        Enemyturn = False
                        Mainturn = True
                        Enemyevent = False
                    elif EnemyAct == 4:
                        skill("2")
                        Turn = (Turn + 1)
                        Enemyturn = False
                        Mainturn = True
                        Enemyevent = False
                    elif EnemyAct == 5:
                        skill("3")
                        Turn = (Turn + 1)
                        Enemyturn = False
                        Mainturn = True
                        Enemyevent = False
            else:
                death()
                win = True
                Turn = int(2)
                Game = False
                Round = False
                Enemyturn = False
        else:
            Round = False
if win is True:
    print("Congratulations! You beat {}!".format(Enemy.name))
    progress = input("Press enter to continue...")
if dead is True:
    print("You lose! {} seems to be too powerful!".format(Enemy.name))
    progress = input("Press enter to continue...")
"""CHANGE LOG:
0.1: Made game FUNCTIONAL
0.2: Changed title and changed graphics, and added character choice... and changed stats
0.3: Put text where they belong. Changed the turn determiner as well
0.4: made actions better and rounded the percentages
0.5: removed skips and put in more actions.. and added Fox skills
0.6: added Werewolf skills
0.7: Allowed bot to use dem skills
0.8: Made graphic appear every round and changed the round determiner to calculate the round every 2 rounds
0.8.1: Bug-fix
0.8.2: Changed stuff around back to how it was before
0.9: cut characters out and put it in separate file and added character "Cougar:
0.9.1: characters are brought back into main code due to variable errors and added instructions
0.9.2: Bug-fixes (The Cougar had a problem due to one of the skills causing data comparison issues)
0.10: Made making character easier, 1st public version
0.10.1: Made main and enemy HP bar bigger
1.0: Made Werewolf less weak, changed a text, 1st public version.
"""