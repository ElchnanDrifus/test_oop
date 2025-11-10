import random
def create_goblin():
    name=input('enter name for the monster  ')
    hp = 20
    speed = random.randint(5,10)
    power = random.randint(5, 10)
    armor_rating = 1
    randoms=random.randint(1,3)
    weapon =''
    if randoms==1:
        weapon='knife'
    elif randoms==2:
        weapon='sword'
    else:
        weapon='ax'
    goblin={'name': name, 'hp': hp, 'speed': speed, 'power': power, 'armor_rating': armor_rating,'weapon':weapon}
    print(f'monster goblin Her name{name}')
    return goblin