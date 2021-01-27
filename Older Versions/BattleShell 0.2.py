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
# Character end


# Functions start
def attack():
    if Mainturn is True:
        print("You attacked!")
        Enemy.HP = (Enemy.HP - int(Main.Atk))
    elif Enemyturn is True:
        print("{} attacks!".format(Enemy.name))
        Main.HP = (Main.HP - int(Enemy.Atk))


def defend():
    print("You defended!")


def skip():
    if Mainturn is True:
        print("You skipped your turn!")
    elif Enemyturn is True:
        print("{} skips a turn!".format(Enemy.name))


def death():
    if Mainturn is True:
        print("You died!")
    elif Enemyturn is True:
        print("{} dies!".format(Enemy.name))
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
while Roundcheck is True:
    if Main.Spd > Enemy.Spd:
        Mainturn = True
        Enemyturn = False
        Roundcheck = False
    else:
        Mainturn = False
        Enemyturn = True
        Roundcheck = False
print("Welcome to BattleShell! The customizable turn-based battle game!")
while Game is True:
    Healthcheck = True
    MainCheck = True
    EnemyCheck = True
    Turn = int(0)
    Round = True
    while Healthcheck is True:
        if MainCheck is True:
            if Main.HP >= 100:
                MainHPbar = "██████████"
                MainCheck = False
            elif Main.HP >= 90:
                MainHPbar = "█████████_"
                MainCheck = False
            elif Main.HP >= 80:
                MainHPbar = "████████__"
                MainCheck = False
            elif Main.HP >= 70:
                MainHPbar = "███████___"
                MainCheck = False
            elif Main.HP >= 60:
                MainHPbar = "██████____"
                MainCheck = False
            elif Main.HP >= 50:
                MainHPbar = "█████_____"
                MainCheck = False
            elif Main.HP >= 40:
                MainHPbar = "████______"
                MainCheck = False
            elif Main.HP >= 30:
                MainHPbar = "███_______"
                MainCheck = False
            elif Main.HP >= 20:
                MainHPbar = "▓▓________"
                MainCheck = False
            elif Main.HP >= 10:
                MainHPbar = "░_________"
                MainCheck = False
            else:
                MainHPbar = "__________"
                MainCheck = False
        elif EnemyCheck is True:
            if Enemy.HP >= 100:
                EnemyHPbar = "██████████"
                EnemyCheck = False
            elif Enemy.HP >= 90:
                EnemyHPbar = "█████████_"
                EnemyCheck = False
            elif Enemy.HP >= 80:
                EnemyHPbar = "████████__"
                EnemyCheck = False
            elif Enemy.HP >= 70:
                EnemyHPbar = "███████___"
                EnemyCheck = False
            elif Enemy.HP >= 60:
                EnemyHPbar = "██████____"
                EnemyCheck = False
            elif Enemy.HP >= 50:
                EnemyHPbar = "█████_____"
                EnemyCheck = False
            elif Enemy.HP >= 40:
                EnemyHPbar = "████______"
                EnemyCheck = False
            elif Enemy.HP >= 30:
                EnemyHPbar = "███_______"
                EnemyCheck = False
            elif Enemy.HP >= 20:
                EnemyHPbar = "▓▓________"
                EnemyCheck = False
            elif Enemy.HP >= 10:
                EnemyHPbar = "░_________"
                EnemyCheck = False
            else:
                EnemyHPbar = "__________"
                EnemyCheck = False
        else:
            Healthcheck = False
    print("\n||YOU||"
          "\n{0}"
          "\n[{2}]{4}"
          "\n"
          "\n======================================="
          "\n||FOE||"
          "\n{1}"
          "\n[{3}]{5}"
          "\n"
          .format(Main.name, Enemy.name, MainHPbar, EnemyHPbar, Main.HP, Enemy.HP))
    while Round is True:
        if Turn == 2:
            Round = False
        elif Mainturn is True:
            if Main.HP > 0:
                Mainevent = True
                while Mainevent is True:
                    Act = input("\nIt's your turn! What do you do?"
                                "\nAttack or Skip?"
                                "\nYour choice: ")
                    if Act in ["Attack", "attack", "ATTACK"]:
                        attack()
                        Turn = (Turn + 1)
                        Mainturn = False
                        Enemyturn = True
                        Mainevent = False
                    elif Act in ["Skip", "skip", "SKIP"]:
                        skip()
                        Turn = (Turn + 1)
                        Mainturn = False
                        Enemyturn = True
                        Mainevent = False
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
"""