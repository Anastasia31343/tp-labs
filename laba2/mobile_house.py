from building import Building
from interfaces import Moveable


class MobileHouse(Building, Moveable):
    """Дом на колёсах: постройка, которая умеет ездить."""

    def move_to(self, x, y):
        if not self.is_built():
            return  # ехать может только готовый дом
        self._set_position(x, y)