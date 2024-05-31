class Weapon:
    def __init__(self, name: str, damage: int, range: int):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.is_alive():
            if abs(actor.get_coords()[0] - target.get_coords()[0]) <= self.range and abs(actor.get_coords()[1] - target.get_coords()[1]) <= self.range:
                target.get_damage(self.damage)
                print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
            else:
                print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print(f"Враг уже повержен")

    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0

    def get_coords(self):
        return (self.pos_x, self.pos_y)

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon_index = 0

    def hit(self, target):
        if not self.weapons:
            print("Я безоружен")
        elif isinstance(target, BaseEnemy):
            self.weapons[self.current_weapon_index].hit(self, target)
        else:
            print("Могу ударить только Врага")

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapons.append(weapon)
            if len(self.weapons) == 1:
                self.current_weapon_index = 0
            print(f"Подобрал {weapon}")
        else:
            print("Это не оружие")

    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
        elif len(self.weapons) == 1:
            print("У меня только одно оружие")
        else:
            self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
            print(f"Сменил оружие на {self.weapons[self.current_weapon_index]}")

    def heal(self, amount):
        self.hp = min(self.hp + amount, 200)
        print(f"Полечился, теперь здоровья {self.hp}")
