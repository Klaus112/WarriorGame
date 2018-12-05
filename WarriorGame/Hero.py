


class Hero:
    def __init__(self, name):
    
        self.Name = name
        self.HeroLevel = 1
        self.WeaponLevel = 1
        self.GoldValue = 5
        self.Damage = 10*(self.WeaponLevel+self.HeroLevel)
        self.Health = 22*(self.HeroLevel)

    def setWeaponLevel(self, value):
        self.WeaponLevel += value
        self.update()

    def setHeroLevel(self, value):
        self.HeroLevel += value
        self.update()
    
    def update (self):
        self.Damage = 10*(self.WeaponLevel+self.HeroLevel)
        self.Health = 22*(self.HeroLevel)