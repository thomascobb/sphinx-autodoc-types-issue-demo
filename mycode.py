from __future__ import annotations

from typing import Generic, TypeVar, Union

#: A variable
X = Union[str, int]

#: Another variable
Y = TypeVar("Y")


class Z:
    """A class we pass as an arg"""


class Bar(Generic[Y]):
    """The class we want
    
    :param X x: an arg
    :param Y y: another arg
    :param Z z: a third arg
    """

    def __init__(self, x: X, y: Y, z: Z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def foo(self) -> Y:
        return self.y
