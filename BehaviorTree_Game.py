import random

class NPC:
    def __init__(self, name, state):
        self.type = "NPC"
        self.name = name
        self.state = state
        self.alive = True
        self.hp = 20
        self.dodge = 0
        self.defense = 0
        self.temphp = 0
        
    def stateTransition(self, newState):
        print("NPC transitions from " + self.state.name + " to " + newState.name)
        self.state.active = False
        self.state = newState
        newState.active = True
        
class Player:
    def __init__(self, name):
        self.type = "Player"
        self.name = name
        self.alive = True
        self.hp = 30
        
        
        
class passiveState:
    def __init__(self):
        self.name = "Passive"
        self.active = True
            
class attackState:
    def __init__(self):
        self.name = "Attack"
        self.active = False
        
class defendState:
    def __init__(self):
        self.name = "Defend"
        self.active = False
        
class deadState:
    def __init__(self):
        self.name = "Dead"
        self.active = False
        
class healState:
    def __init__(self):
        self.name = "Heal"
        self.active = False
        
class dodgeState:
    def __init__(self):
        self.name = "Dodge"
        self.active = False
        
class doubleattackState:
    def __init__(self):
        self.name = "Attack_Twice"
        self.active = False
        
class insultState:
    def __init__(self):
        self.name = "Insult"
        self.active = False
        
        
    
def combat(attacker, defender):
    print(attacker.name + " is attacking " + defender.name + "!\n")
    
    hitDamage = 0 
    if(attacker.type == "NPC"):
        hitDamage = random.randint(1, 5)
    else:
        hitDamage = random.randint(6, 8)
    
    if(defender.dodge == 0):
        hitDamage = hitDamage-defender.defense
        if(hitDamage > 0):
            defender.hp = defender.hp - hitDamage
            print(attacker.name + " attacked for " + str(hitDamage) + " damage!\n")
        else:
            print(defender.name + " deflected the attack!\n")
    else:
        print(defender.name + " dodged the attack!\n")
    
    defender.dodge = 0
    defender.defense = 0
        
    if(attacker.hp <= 0):
        attacker.alive = False
    if(defender.hp <= 0):
        defender.alive = False
    print(attacker.name + "'s hp = " + str(attacker.hp) + "")
    print(defender.name + "'s hp = " + str(defender.hp) + "\n")
    
def heal(user):
    print(user.name + "tries  healing itself!\n")
    chance = random.randint(0,1)
    if(chance == 0):
        print(user.name + "failed to heal!\n")
    else:
        hpgive = random.randint(1,5)
        user.hp = user.hp + hpgive
        print(user.name + " healed for = " + str(hpgive) + "!\n")
        
def insult(attacker, defender):
    print(attacker.name + " insults " + defender.name + "!\n")
    Rude = ["Beegees are mediocre",
            "Disney Star Wars is better than the original trilogy",
            "Locklair is not funny (find better insult)"]
    rudebuck = random.randint(0,2)
    print(Rude[rudebuck])
    
def treeStart(npc, player):
    aState = attackState()
    deState = defendState()
    
    playerTurn(npc, player)
    
    if(npc.hp < 12):
        npc.stateTransition(aState)
        aggroTree(npc, player)
    else:
        npc.stateTransition(deState)
        protectTree(npc, player)
        
def aggroTree(npc, player):
    aState = attackState()
    daState = doubleattackState()
    deState = defendState()
    
    npcTurn(npc, player)
    playerTurn(npc, player)
    chance = random.randint(0,2)
    if(chance == 2):
        npc.stateTransition(daState)
    if(npc.hp < 6):
        npc.stateTransition(deState)
        protectTree(npc, player)
    else:
        aggroTree(npc, player)
        
def protectTree(npc, player):
    deState = defendState()
    doState = dodgeState()
    hState = healState()
    iState = insultState()
    dead = deadState()
    
    npcTurn(npc, player)
    playerTurn(npc, player)
    
    chance = random.randint(0,2)
    if(chance == 1):
        print("The " + npc.name + " gets a free turn!\n")
        npc.stateTransition(iState)
        npcTurn(npc, player)
        npc.stateTransition(doState)
    elif(chance == 2):
        print("The " + npc.name + " gets a free turn!\n")
        npc.stateTransition(hState)
        npcTurn(npc, player)
        npc.stateTransition(doState)
    
    npc.stateTransition(doState)
    if(npc.temphp > npc.hp):
        if(npc.hp <= 0):
            npc.alive = False
        else:
            aggroTree(npc, player)
    else:
        npc.temphp = npc.hp
        protectTree(npc, player)
    
def playerTurn(npc, player):
    print(player.name + "'s turn.")
    move = input("Type *yes* to attack or *no* to remain still: ")
    if(move == "yes"):
        combat(player, npc)
    
def npcTurn(npc, player):
    print(npc.name + "'s turn.\n")
    print(npc.name + "'s current state = " + npc.state.name)
    if(npc.state.name == "Attack"):
        combat(npc, player)
    if(npc.state.name == "Attack_Twice"):
        print("The " + npc.name + " will attack twice!\n")
        combat(npc, player)
        combat(npc, player)
    if(npc.state.name == "Heal"):
        heal(npc)
    if(npc.state.name == "Defend"):
        npc.defense = random.randint(0, 5)
    if(npc.state.name == "Dodge"):
        npc.dodge == random.randint(0,2)
    if(npc.state.name == "Insult"):
        insult(npc, player)
    if(npc.state.name == "Dead"):
        print("The " + npc.name + " has died!\n")
        npc.alive = False
    else:
        print("The " + npc.name + " does nothing...\n")
        
        
        
def main():
    pState = passiveState()
    
    npc = NPC("Goblin", pState)
    print("NPC initiated with name " + npc.name + ". NPC initial state is " + npc.state.name + ".")
    player = Player("Player")
    print("Player initiated with name " + player.name + ".\n\n")
    
    while(npc.alive == True and player.alive == True):
        treeStart(npc, player)
    print("Game Over")
        
        
        
if __name__ == "__main__":
    main()


