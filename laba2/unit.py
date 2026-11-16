from game_object import GameObject


class Unit(GameObject):
    """Юнит: тот, кем можно управлять и кто может получить урон."""

    def __init__(self, object_id, name, x, y, hp):
        if type(self) is Unit:
            raise TypeError("Unit нельзя создавать напрямую")
        super().__init__(object_id, name, x, y)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        if damage <= 0 or not self.is_alive():
            return
        self._hp = max(0, self._hp - damage)
