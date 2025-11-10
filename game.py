import random

from core.player import create_player
from core.orc import create_orc
from core.goblin import create_goblin

def Monster_Picker():
    randoms=random.randint(1,2)
    if randoms==1:
        return orc
    else:
        return goblin


def Game_start_display(player, monster):
    print(player,"\n",  monster)
    inpu=input('Enter one to fight Enter two to get out')
    if inpu==1:
        print('Starting to play')
    else:
        print('You lost the game')
    return inpu

def Who_is_first():
    player=random.randint(1,6)
    monster=random.randint(1,6)
    if monster>player:
        return 1
    else:
        return 2

def Attack_strength(player,monster):
    Attack_strengtha=random.randint(1,20)
    if first==1:
        Attack_strengtha+=monster[speed]
    else:
        Attack_strengtha += player[speed]

def attack(first,player,monster,Attack_strengtha):
    if first == 1:
        rival = player
        validity=monster
    else:
        rival = monster
        validity = player
    if Attack_strengtha>rival[armor_rating]
        print('injury')
        return 1 ,rival ,validity
    else:
        print('No harm done')
        return 2 ,rival ,validity

def The_extent_of_the_damage(validitya,rivala):
    Amount_of_damage=random.randint(1,6)
    Amount_of_damage+=validity[power]
    rival[hp]-=Amount_of_damage
    return rival[hp]






def play():
    monster=Monster_Picker()
    player = create_player()
    Are_we_continuing=Game_start_display(player,monster)
    if Are_we_continuing==1:
        first=Who_is_first()
        Attack_strengtha =Attack_strength(player,monster)
        attacka=attack(first,player,monster,Attack_strengtha)
        attackab=attacka[0]
        rivala=attacka[1]
        validitya=attacka[2]
        if attackab==1:
            Remaining_life=The_extent_of_the_damage(validitya,rivala)









