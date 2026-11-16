from game_object import GameObject


class Building(GameObject):
    """Постройка: может быть достроена или ещё нет."""

    def __init__(self, object_id, name, x, y, built):
        if type(self) is Building:
            raise TypeError("Building нельзя создавать напрямую")
        super().__init__(object_id, name, x, y)
        self._built = built

    def is_built(self):
        return self._built

    def finish_building(self):
        self._built = True