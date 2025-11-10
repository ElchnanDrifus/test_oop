import random
def create_orc():
    name=input('enter name for the monster  ')
    hp = 50
    speed = random.randint(0,5)
    power = random.randint(10, 15)
    armor_rating = random.randint(2, 8 )
    randoms=random.randint(1,3)
    weapon =''
    if randoms==1:
        weapon='knife'
    elif randoms==2:
        weapon='sword'
    else:
        weapon='ax'
    orc={'name': name, 'hp': hp, 'speed': speed, 'power': power, 'armor_rating': armor_rating,'weapon':weapon}
    print(f'monster orc Her name{name}')
    return orc
