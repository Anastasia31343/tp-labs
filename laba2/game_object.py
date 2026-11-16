from abc import ABC


class GameObject(ABC):
    """Базовый класс для всех игровых объектов."""

    def __init__(self, object_id, name, x, y):
        if type(self) is GameObject:
            raise TypeError("GameObject нельзя создавать напрямую")
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def _set_position(self, x, y):
        # Менять координаты могут только наследники (например, когда юнит идёт)
        self._x = x
        self._y = y