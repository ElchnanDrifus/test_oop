import random
def create_player():
    name=input('enter username  ')
    hp = 50
    speed = random.randint(5,10)
    power = random.randint(5, 10)
    armor_rating = random.randint(5, 15)
    player={'name':name,'hp':hp,'speed':speed,'power':power,'armor_rating':armor_rating}
    print(f'player name {name}')
    return player


