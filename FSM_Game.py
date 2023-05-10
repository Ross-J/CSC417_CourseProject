import random


class NPC:
    def __init__(self, name, state):
        self.type = "NPC"
        self.name = name
        self.state = state
        self.alive = True
        self.hp = 20
                
    def stateTransition(self, newState):
        print("\nNPC transitions from " + self.state.name + " state to " + newState.name + " state.")
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
        



def combat(attacker, defender):
    print(attacker.name + " is attacking " + defender.name + "!\n")
    
    # Calculate damage done during combat from attacker to defender
    # Player will attack with higher random and NPC with lower random damage
    # If NPC is in defend state, subtract random defense value from player's attack
    defense = 0 
    hitDamage = 0 
    if(defender.type == "NPC"):
        defense = random.randint(0, 5)
    if(attacker.type == "NPC"):
        hitDamage = random.randint(1, 5)
    else:
        hitDamage = random.randint(6, 8) - defense
    defender.hp = defender.hp - hitDamage
    
    # After each combat function, check if NPC or Player are dead
    if(attacker.hp <= 0):
        attacker.alive = False
    if(defender.hp <= 0):
        defender.alive = False

    print(defender.name + " takes " + str(hitDamage) + " damage.")
    print(attacker.name + "'s hp = " + str(attacker.hp) + "")
    print(defender.name + "'s hp = " + str(defender.hp) + "")



        
def playerTurn(player):
    print("\n" + player.name + "'s turn.")
    move = input("Type *yes* to attack or *no* to remain passive: ")
    return move
    
def npcTurn(npc):
    print("\n" + npc.name + "'s turn.")
    
    
    
        
def main():
    # Initialize NPC states
    pState = passiveState()
    aState = attackState()
    dState = defendState()
    dead = deadState()
    
    # Initialize NPC and Player
    npcName = input("Please enter NPC's name: ")
    npc = NPC(npcName, pState)
    print("NPC initiated with name " + npc.name + ". " + npc.name + "'s initial state is " + npc.state.name + ". " + npc.name + " has " + str(npc.hp) + " hp.\n")
    playerName = input("Please enter player's name: ")
    player = Player(playerName)
    print("Player initiated with name " + player.name + ". " + player.name + " has " + str(player.hp) + " hp.")

    # Game Loop
    while(npc.alive == True and player.alive == True):
        
        # Player's turn
        # When Player attacks NPC, call combat function and change NPC states if conditions are met
        # When Player does not attack, turn moves directly to NPC
        pMove = playerTurn(player)
        if(pMove == "yes"):
            combat(player, npc)
            if(npc.state != dState and npc.hp <= 5):
                npc.stateTransition(dState)
            elif(npc.state != aState and npc.state != dState):
                npc.stateTransition(aState)
            if(npc.alive == False):
                npc.stateTransition(dead)
                break
            if(player.alive == False):
                npc.stateTransition(pState)
        if(pMove == "no"):
            print("\nNPC remains in " + npc.state.name + " state.")
            
        # NPC's turn
        # When NPC attacks Player, call combat function 
        npcTurn(npc)
        if(npc.state.name == "Attack"):
            combat(npc, player)
    
    # After both turns, check whether game should continue
    if(player.alive == False):
        print("Player is dead.")
    if(npc.alive == False):
        print("NPC is dead.")
    print("\nGAME OVER")
        



if __name__ == "__main__":
    main()