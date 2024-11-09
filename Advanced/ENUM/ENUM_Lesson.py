from enum import Enum

class Color(Enum): ## USed for constant
    RED: str = 'R'
    GREEN: str = 'G'
    BLUE: str = 'B'


def create_car(color: Color):
    match color:
        case Color.RED:
            print(f"We have created a {Color.RED.name} car")
        case Color.BLUE:
            print(f"We have created a {Color.BLUE.name} car")
        case Color.GREEN:
            print(f"We have created a {Color.GREEN.name} car")
        case _:
            print(f"We have not created any {color} ar")
print(Color('R'))
print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
create_car(Color.RED)