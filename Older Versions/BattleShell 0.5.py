"""
  ___________
< Battleshell >
  ^^^^^^^^^^^
by Jason
Ver: 0.X
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
Turn = int(2)


# Character start
class Fox:
    name = "The Fox"
    # Changing stats:
    HP = int(80)
    Atk = int(9)
    Def = int(5)
    Spd = int(23)
    # Base stats:
    bHP = int(80)
    bAtk = int(9)
    bDef = int(5)
    bSpd = int(23)
    # Character dialog:
    dAtk = "The Fox attempts to scratch the foe with claws!"
    dAtt = "The Fox manages to land its attack!"
    Miss = "The Fox misses!"
    Fail = "The Fox fails!"
    dSpd = "The Fox boosts its speed!!"
    dDef = "The Fox increases its defence!"
    dDog = "The Fox manages to dodge the attack!"
    dHit = "The Fox is hit!"
    Attempt = "The Fox attempts to use a skill..."
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
        hit = random.randint(1, Enemy.Spd)
        print(self.Attempt)
        if self.Spd > hit:
            Enemy.HP = (Enemy.HP - (self.Atk + (self.Spd / 2)))
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
    dSpd = "The Werewolf increases its speed!"
    dDef = "The Werewolf increases its defence!"
    dDog = "The Werewolf dodges the attack!"
    dHit = "The Werewolf is hit!"
# Character end


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


CL = ["Werewolf", "Fox"]
# User choice of character:
while CharSelect is True:
    Character = input("Pick your character:"
                      "\n- {0}"
                      "\n- {1}"
                      "\nYour character of choice: "
                      .format(CL[0], CL[1]))
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
    else:
        print("There is only {}".format(CL))
# Computer's choice
FoeSelect = random.randint(0, (len(CL) - 1))
while FoerSelect is True:
    if CL[FoeSelect] == "Werewolf":
        Enemy = Werewolf()
        FoerSelect = False
    elif CL[FoeSelect] == "Fox":
        Enemy = Fox()
        FoerSelect = False
    else:
        print("There seems to be too little characters to play this game!")
        Roundcheck = False
        Game = False
print("Welcome to BattleShell! The customizable turn-based battle game!")
while Game is True:
    Roundcheck = True
    Healthcheck = True
    MainCheck = True
    EnemyCheck = True
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
                MainHPbar = "██████████"
                MainCheck = False
            elif Main.pHP >= 90:
                MainHPbar = "█████████_"
                MainCheck = False
            elif Main.pHP >= 80:
                MainHPbar = "████████__"
                MainCheck = False
            elif Main.pHP >= 70:
                MainHPbar = "███████___"
                MainCheck = False
            elif Main.pHP >= 60:
                MainHPbar = "██████____"
                MainCheck = False
            elif Main.pHP >= 50:
                MainHPbar = "█████_____"
                MainCheck = False
            elif Main.pHP >= 40:
                MainHPbar = "████______"
                MainCheck = False
            elif Main.pHP >= 30:
                MainHPbar = "███_______"
                MainCheck = False
            elif Main.pHP >= 20:
                MainHPbar = "▓▓________"
                MainCheck = False
            elif Main.pHP >= 10:
                MainHPbar = "░_________"
                MainCheck = False
            else:
                MainHPbar = "__________"
                MainCheck = False
        elif EnemyCheck is True:
            Enemy.pHP = round((Enemy.HP / Enemy.bHP) * 100)
            if Enemy.pHP >= 100:
                EnemyHPbar = "██████████"
                EnemyCheck = False
            elif Enemy.pHP >= 90:
                EnemyHPbar = "█████████_"
                EnemyCheck = False
            elif Enemy.pHP >= 80:
                EnemyHPbar = "████████__"
                EnemyCheck = False
            elif Enemy.pHP >= 70:
                EnemyHPbar = "███████___"
                EnemyCheck = False
            elif Enemy.pHP >= 60:
                EnemyHPbar = "██████____"
                EnemyCheck = False
            elif Enemy.pHP >= 50:
                EnemyHPbar = "█████_____"
                EnemyCheck = False
            elif Enemy.pHP >= 40:
                EnemyHPbar = "████______"
                EnemyCheck = False
            elif Enemy.pHP >= 30:
                EnemyHPbar = "███_______"
                EnemyCheck = False
            elif Enemy.pHP >= 20:
                EnemyHPbar = "▓▓________"
                EnemyCheck = False
            elif Enemy.pHP >= 10:
                EnemyHPbar = "░_________"
                EnemyCheck = False
            else:
                EnemyHPbar = "__________"
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
                    EnemyAct = random.randint(1, 2)
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
"""