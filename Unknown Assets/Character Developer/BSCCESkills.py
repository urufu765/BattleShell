"""(example of a skill)


def skill1(self):  # skill-name-1 (this skill increases the character's speed)
    chance = random.randint(1, 100)
    print(self.Attempt)
    if chance > 20:
        self.Spd = round(self.Spd * 1.1)
        print(self.dSpd)
    else:
        print(self.Fail)
"""


class SIdentifier:
    Skill1 = "\ndef skill1(self):"
    Skill2 = "\ndef skill2(self):"
    Skill3 = "\ndef skill3(self):"


class Boost:
    Speedier = ("    chance = random.randint(1, 100)"
                "\n    print(self.Attempt)"
                "\n    if chance > 20:"
                "\n        self.Spd = round(self.Spd * 1.1)"
                "\n        print(self.dSpd)"
                "\n    else:"
                "\n        print(self.Fail)\n")
