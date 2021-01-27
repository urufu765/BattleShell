"""
BattleShell Custom Character Engine
by FOKKUSU~
Ver: 0.X
"""
from BSCCECharacters import *
from BSCCESkills import *
CharacterSelect = True
Skill1Select = True
Skill2Select = True
Skill3Select = True
cList = ["Leopard"]
sList = ["Speedier"]
sk = SIdentifier()
Character = ""
skill1 = ""
skill2 = ""
skill3 = ""

# Texts start
class Text:
    intro = ("Welcome to the BattleShell Custom Character Engine!"
             "\nUsing this, you can create your own character with the pre-selected modules!")
    Cselect = ("Pick a character!"
               "\nyour choice: ")
    Sselect = ("Pick a skill!"
               "\nyour choice: ")
    Selected = "You've selected:"
    Error = "Please select from the list!"


txt = Text()
# program start
print(txt.intro)
while CharacterSelect is True:
    print("Characters:"
          "\n{0}"
          .format(cList))
    Char = input(txt.Cselect)
    if len(Char) >= 1:
        if Char in "leopardLEOPARD":
            UserChar = Damage()
            Character = UserChar.Leopard
            print(txt.Selected, cList[0])
            CharacterSelect = False
        else:
            print(txt.Error)
    else:
        print(txt.Error)
while Skill1Select is True:
    print("Skills:"
          "\n{0}"
          .format(sList))
    Skill = input(txt.Sselect)
    if len(Skill) >= 1:
        if Skill in "speedierSPEEDIER":
            UserSkill1 = Boost()
            skill1 = UserSkill1.Speedier
            print(txt.Selected, cList[0])
            Skill1Select = False
        else:
            print(txt.Error)
    else:
        print(txt.Error)

while Skill2Select is True:
    print("Skills:"
          "\n{0}"
          .format(sList))
    Skill = input(txt.Sselect)
    if len(Skill) >= 1:
        if Skill in "speedierSPEEDIER":
            UserSkill2 = Boost()
            skill2 = UserSkill2.Speedier
            print(txt.Selected, cList[0])
            Skill2Select = False
        else:
            print(txt.Error)
    else:
        print(txt.Error)

while Skill3Select is True:
    print("Skills:"
          "\n{0}"
          .format(sList))
    Skill = input(txt.Sselect)
    if len(Skill) >= 1:
        if Skill in "speedierSPEEDIER":
            UserSkill3 = Boost()
            skill3 = UserSkill3.Speedier
            print(txt.Selected, cList[0])
            Skill3Select = False
        else:
            print(txt.Error)
    else:
        print(txt.Error)
print("Copy and paste this in Custom Characters and make sure to implement the character for use!"
      "\n{0}"
      "\n{1}"
      "\n{2}"
      "\n{3}"
      "\n{4}"
      "\n{5}"
      "\n{6}"
      .format(Character, sk.Skill1, skill1, sk.Skill2, skill2, sk.Skill3, skill3))
proceed = input("\nPress enter to continue...")
"""Change Log:
0.1: Created working version
0.2: Added others
"""
