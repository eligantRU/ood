from enum import Enum, auto


class Color(Enum):
    GREEN = auto()
    RED = auto()
    BLUE = auto()
    YELLOW = auto()
    PINK = auto()
    BLACK = auto()


def str2color(color: str) -> Color:
    if color == "green":
        return Color.GREEN
    elif color == "red":
        return Color.RED
    elif color == "blue":
        return Color.BLUE
    elif color == "yellow":
        return Color.YELLOW
    elif color == "pink":
        return Color.PINK
    elif color == "black":
        return Color.BLACK
    else:
        raise ValueError(f"Unknown color: {color}")
