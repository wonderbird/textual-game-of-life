import abc

from game_app.cell import Cell


# Interface for the Universe View
#
# Python interfaces and their syntax are described in
# https://realpython.com/python-interface/
class UniverseView(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "on_produce_next_generation")
            and callable(subclass.on_produce_next_generation)
            and hasattr(subclass, "on_reset_to_seed")
            and callable(subclass.on_reset_to_seed)
            and hasattr(subclass, "update")
            and callable(subclass.update)
            and hasattr(subclass, "add")
            and callable(subclass.add)
            and hasattr(subclass, "remove")
            and callable(subclass.remove)
            and hasattr(subclass, "clear")
            and callable(subclass.clear)
        )

    @abc.abstractmethod
    def on_produce_next_generation(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def on_reset_to_seed(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, cell: Cell) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, cell: Cell) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self) -> None:
        raise NotImplementedError
