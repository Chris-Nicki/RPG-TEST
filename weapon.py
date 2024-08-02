class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int
                 ):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value



fists = Weapon(name='fists', weapon_type='sharp', damage=1, value=2)
knife = Weapon(name='knife', weapon_type='sharp', damage=2, value=4)
brass_knuckles = Weapon(name='brass_knuckles', weapon_type='blunt', damage=4, value=8)
bat = Weapon(name='bat', weapon_type='blunt', damage=6, value=12)
hatchet = Weapon(name='hatchet', weapon_type='sharp', damage=8, value=16)
pistol = Weapon(name='pistol', weapon_type='gun', damage=10, value=20)