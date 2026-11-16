from abc import ABC, abstractmethod


class Attacker(ABC):
    """То, что может атаковать юниты."""

    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    """То, что может перемещаться."""

    # В задании метод не описан, поэтому сделала самый простой вариант
    @abstractmethod
    def move_to(self, x, y):
        pass