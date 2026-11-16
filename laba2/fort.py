from building import Building
from interfaces import Attacker


class Fort(Building, Attacker):
    """Крепость: постройка, которая стреляет из пушек."""

    def __init__(self, object_id, name, x, y, built, damage):
        super().__init__(object_id, name, x, y, built)
        self._damage = damage

    def attack(self, unit):
        if not self.is_built():
            return  # из недостроенной крепости пушки не стреляют
        unit.receive_damage(self._damage)