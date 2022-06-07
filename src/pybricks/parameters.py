# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Constant parameters/arguments for the Pybricks API."""

from __future__ import annotations

from typing import Union
from enum import Enum as _Enum

from .geometry import Matrix

Number = Union[int, float]


class _PybricksEnumMeta(type(_Enum)):
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(_Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return "{}.{}".format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Color:
    """Light or surface color."""

    h: int
    s: int
    v: int

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): Hue (0--360)
            s (Number, %): Saturation.
            v (Number, %): Brightness value.
        """
        self.h = h % 360
        self.s = max(0, min(s, 100))
        self.v = max(0, min(v, 100))

    def __repr__(self):
        return "Color(h={}, s={}, v={})".format(self.h, self.s, self.v)

    def __eq__(self, other: Color) -> bool:
        ...

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)


class Port(_PybricksEnum):
    """Port on the programmable brick or hub."""

    # Generic motor/sensor ports
    A: Port = ord("A")
    B: Port = ord("B")
    C: Port = ord("C")
    D: Port = ord("D")
    E: Port = ord("E")
    F: Port = ord("F")

    # NXT/EV3 sensor ports
    S1: Port = ord("1")
    S2: Port = ord("2")
    S3: Port = ord("3")
    S4: Port = ord("4")


class Stop(_PybricksEnum):
    """Action after the motor stops."""

    COAST: Port = 0
    """Let the motor move freely."""

    BRAKE: Port = 1
    """Passively resist small external forces."""

    HOLD: Port = 2
    """Keep controlling the motor to hold it at the commanded angle. This is
    only available on motors with encoders."""


class Direction(_PybricksEnum):
    """Rotational direction for positive speed or angle values."""

    CLOCKWISE: Direction = 0
    """A positive speed value should make the motor move clockwise."""

    COUNTERCLOCKWISE: Direction = 1
    """A positive speed value should make the motor move counterclockwise."""


class Button(_PybricksEnum):
    """Buttons on a hub or remote."""

    LEFT_DOWN: Button = 1
    LEFT_MINUS: Button = 1
    DOWN: Button = 2
    RIGHT_DOWN: Button = 3
    RIGHT_MINUS: Button = 3
    LEFT: Button = 4
    CENTER: Button = 5
    RIGHT: Button = 6
    LEFT_UP: Button = 7
    LEFT_PLUS: Button = 7
    UP: Button = 8
    BEACON: Button = 8
    RIGHT_UP: Button = 9
    RIGHT_PLUS: Button = 9
    BLUETOOTH: Button = 9


class Side(_PybricksEnum):
    """Side of a hub or a sensor."""

    RIGHT: Side = 6
    FRONT: Side = 0
    TOP: Side = 8
    LEFT: Side = 4
    BACK: Side = 5
    BOTTOM: Side = 2


class Icon:
    UP: Matrix
    DOWN: Matrix
    LEFT: Matrix
    RIGHT: Matrix
    ARROW_RIGHT_UP: Matrix
    ARROW_RIGHT_DOWN: Matrix
    ARROW_LEFT_UP: Matrix
    ARROW_LEFT_DOWN: Matrix
    ARROW_UP: Matrix
    ARROW_DOWN: Matrix
    ARROW_LEFT: Matrix
    ARROW_RIGHT: Matrix
    HAPPY: Matrix
    SAD: Matrix
    EYE_LEFT: Matrix
    EYE_RIGHT: Matrix
    EYE_LEFT_BLINK: Matrix
    EYE_RIGHT_BLINK: Matrix
    EYE_RIGHT_BROW: Matrix
    EYE_LEFT_BROW: Matrix
    EYE_LEFT_BROW_UP: Matrix
    EYE_RIGHT_BROW_UP: Matrix
    HEART: Matrix
    PAUSE: Matrix
    EMPTY: Matrix
    FULL: Matrix
    SQUARE: Matrix
    TRIANGLE_RIGHT: Matrix
    TRIANGLE_LEFT: Matrix
    TRIANGLE_UP: Matrix
    TRIANGLE_DOWN: Matrix
    CIRCLE: Matrix
    CLOCKWISE: Matrix
    COUNTERCLOCKWISE: Matrix
    TRUE: Matrix
    FALSE: Matrix
