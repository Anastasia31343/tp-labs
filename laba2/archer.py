from unit import Unit
from interfaces import Attacker, Moveable


class Archer(Unit, Attacker, Moveable):
    """Лучник: юнит, который умеет атаковать и перемещаться."""

    def __init__(self, object_id, name, x, y, hp, damage):
        super().__init__(object_id, name, x, y, hp)
        self._damage = damage

    def attack(self, unit):
        if not self.is_alive():
            return  # мёртвый лучник не стреляет
        unit.receive_damage(self._damage)

    def move_to(self, x, y):
        if not self.is_alive():
            return
        self._set_position(x, y)
