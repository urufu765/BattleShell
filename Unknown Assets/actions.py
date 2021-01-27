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
