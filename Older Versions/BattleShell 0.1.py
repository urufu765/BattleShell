"""
Battleshell
BattleShell.py
This file should be the hub to separate files, while containing the main code.
The separate code should be the graphics and the character grid.
"""
import random
dead = False
win = False
Game = True
Round = False
Mainturn = False
Enemyturn = False
Roundcheck = True
Turn = int(2)


# Character start
class Fox:
    name = "The Fox"
    HP = int(100)
    Atk = int(7)
    Def = int(5)
    Spd = int(20)


class Werewolf:
    name = "The Werewolf"
    HP = int(150)
    Atk = int(20)
    Def = int(10)
    Spd = int(10)
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


Main = Werewolf()
Enemy = Fox()
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
    print("\n                        ````. `             ||                                              "
          "\n                  ..`-``   :oo/```          ||                                              "
          "\n                  . .+   ``       ````      ||                                              "
          "\n                 ``     `        .-:/os+.   ||                                              "
          "\n            `-`.```     -++     -/yo/::--`  ||                                              "
          "\n          ``-:.o/  ./+oyhhy`    .yhh/       ||               `-                             "
          "\n          .  `   +--+yyy:-: `/ys+ommho      ||             -omh/                            "
          "\n          .    ..+ssyyhy:-+/. :dd  mdy/     ||      `:/oosss+-:d                            "
          "\n          .   -o+oshdhhhs//-   -+ydmdys     ||   -sdmdhho.....oh                            "
          "\n         `   /s++osyy:   .oyo://ohyhs/y     ||  yNdhhhhh+-...+N-                            "
          "\n         : `oyssyyyo.      +y- `.--.` :     || oNdhhhhhhhhydmh-        /s/`                 "
          "\n        -s:yhdhhhyy`       +md+`            || dmhhhhhhdmho/`         oNmmm:   `+dmy        "
          "\n        hhddmmdhhyy         -ymdo-`         || ymhhhhhmh.             hdhmdNs -dmmmN`       "
          "\n        hdmdhyshhh+   ` ----:+hmmmmh+:-`    || .mmdhhhm-oyhdddyyo/.   hdhdNmNsdmdNdN`       "
          "\n          -//:ohhy.  -+ssoyys//::/++o+++++- ||   /syymNmdhhhhhhhhdmdy//mdNmmdddddNmd``      "
          "\n         --:+syyy: ./++hy/`..        :/shyy-||     .mmhhhhhhhhhhhhhhhdmmmdhd  ymdhddsN.     "
          "\n         +ooyyyyh/++++omd+`             `..`||    `mdhhhhhhhhhhhhhhhhhhhhhhm ddNmhhddd+- .-`"
          "\n        .oyyyyyyd+++++hmmdy:                ||    +Nhhhhhhhhhhhhhhhhhhhhhhhhhddhhhhhhhdmmddm"
          "\n       . yyyyoydh+++ohmmmmmho`              ||    +NhhhhhhmhhhhhhhhhhhhhhhhhhhhNmmmmmmdhyyys"
          "\n      `/`s+:-:hmsoshmmmyydmhyo              ||    .mdhhhhhmy+:sshhhhhhhhyo+ddddmm+ .`       "
          "\n      ++++++++dhyy+osyhs++ooyy/             ||   .ohmhhhhhmNs:..omhhhmy/-.:dhhy+-`          "
          "\n     /++++oo+syy+` `++++ooooyy+             ||   +NdhhddmmNh+dmhyNdhdNoosyddhhddssoss+.     "
          "\n    /+++syyo+/-`     /++sys+/:`             ||    /mdydh+`-N::yh:NdhmN/-` `/smd+-.:./m+     "
          "\n   /+++oyy+           +++oy+`               ||     /m.-/+m.osso :Nhhmh        :d+.:-+m      "
          "\n  /++++yys            `ooyhy+               ||     m/.-.sd      hmyyN/         :dhdoo/      "
          "\n /++++ohy/             ``-o:`               ||     .ooshd+     -N::.No:                     "
          "\n:+++++oyy.                                  ||                 `m+..:oNo                    "
          "\nssoyyyyyo                                   ||                  myhyym/`                    "
          "\n  -/:/-.                                    ||                  `-- `                       "
          "\n      ______________                        ||           _________                          "
          "\n     < The Werewolf >  [{0}]         ||          < The Fox >  [{1}]           "
          "\n      ^^^^^^^^^^^^^^    {2}%                ||           ^^^^^^^^^    {3}%                  "
          .format(MainHPbar, EnemyHPbar, Main.HP, Enemy.HP))
    while Round is True:
        if Turn == 2:
            Round = False
        elif Mainturn is True:
            if Main.HP > 0:
                Mainevent = True
                while Mainevent is True:
                    Act = input("\nIt's your turn! What do you do?"
                                "\nAttack or Skip?")
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
elif dead is True:
    print("You lose! {} seems to be too powerful!".format(Enemy.name))
    progress = input("Press enter to continue...")

"""CHANGE LOG:
0.1: Made game FUNCTIONAL
"""