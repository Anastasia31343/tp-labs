from archer import Archer
from fort import Fort
from mobile_house import MobileHouse

archer = Archer(1, "Лучник", 0, 0, 100, 15)
enemy = Archer(2, "Вражеский лучник", 5, 5, 40, 10)
fort = Fort(3, "Крепость", 10, 10, False, 30)
house = MobileHouse(4, "Дом на колёсах", 2, 2, True)

archer.attack(enemy)
print(enemy.get_name(), "- hp:", enemy.get_hp())

fort.attack(enemy)  # крепость ещё не построена, урона не будет
print("После выстрела недостроенной крепости:", enemy.get_hp())

fort.finish_building()
fort.attack(enemy)
fort.attack(enemy)
print("После двух выстрелов крепости:", enemy.get_hp(), "жив:", enemy.is_alive())

archer.move_to(3, 4)
print(archer.get_name(), "стоит в точке", (archer.get_x(), archer.get_y()))

house.move_to(7, 7)
print(house.get_name(), "стоит в точке", (house.get_x(), house.get_y()))