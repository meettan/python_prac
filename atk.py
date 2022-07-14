class Enemy:
    #atkl = 60
    #atkh = 80

    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getatkl(self):
        print(self.atkl)

    def getatkh(self):
        print(self.atkh)


enemy1 = Enemy(40,70)
enemy1.getatkl()

enemy2 = Enemy(80,90)
enemy2.getatkh()

"""
import random

playerhp = 300
enemyatkl = 60
enemyatkh = 80

while playerhp > 0 :
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp - dmg

    #print("cdcdcdvdv",playerhp)

    if playerhp <= 30:
        playerhp = 30
        print("Enemy stikes for",dmg,"points of damage.Current HP is ",playerhp)

    if playerhp > 30:
       continue 
        
    print("You have a low health")
    break
"""
