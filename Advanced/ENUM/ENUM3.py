from enum import Enum,Flag, auto

class Color(Flag):
    RED: int = auto()
    GREEN: int = auto()
    BLUE: int = auto()
    YELLOW: int = auto()
    BLACK: int = auto()
    ALL: int  = RED | GREEN | BLACK | BLUE | YELLOW

## Iterate over flag
red_and_yellow: Color = Color.RED | Color.YELLOW
print(red_and_yellow)
print(Color.ALL.value)


## If we use Flag as parent class, auto will assign power of 2
## If we use Enum as parent class, auto will assign incremental numbers from 1,2,3 etc.