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
"""


class Damage:
    Leopard = ('class Leopard:'
               '\n    name = "The Leopard"'
               '\n    # Changing stats:'
               '\n    HP = int(130)'
               '\n    Atk = int(20)'
               '\n    Def = int(5)'
               '\n    Spd = int(19)'
               '\n    # Base stats:'
               '\n    bHP = int(130)'
               '\n    bAtk = int(20)'
               '\n    bDef = int(5)'
               '\n    bSpd = int(19)'
               '\n    # Character dialog:'
               '\n    dAtk = "The Leopard attempts to scratch the foe with claws!"'
               '\n    dAtt = "The Leopard manages to land its attack!"'
               '\n    Miss = "The Leopard misses!"'
               '\n    Fail = "The Leopard fails!"'
               '\n    dSpd = "The Leopard boosts its speed!!"'
               '\n    dDef = "The Leopard increases its defence!"'
               '\n    dDog = "The Leopard manages to dodge the attack!"'
               '\n    dHit = "The Leopard is hit!"'
               '\n    Attempt = "The Leopard attempts to use a skill..."\n')
