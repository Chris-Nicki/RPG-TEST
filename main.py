from character import Hero, Enemy
from weapon import knife, brass_knuckles, bat, pistol

hero = Hero(name='Hero', health=100)
enemy = Enemy(name='Enemy', health = 100, weapon=knife)



while True:
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()


    hero.equip(brass_knuckles)
    hero.drop(brass_knuckles)
    input()
