from enum import Enum, Flag

class Color(Flag):
    RED: int = 1
    GREEN: int = 2
    BLUE: int = 4
    YELLOW: int = 8
    BLACK: int = 16

## Iterate over flag
red_and_yellow: Color = Color.RED | Color.YELLOW
for c in red_and_yellow:
    print(c)

### USe membership
cool_colors: Color = Color.RED | Color.YELLOW | Color.BLACK
my_car_color: Color = Color.BLACK

if my_car_color in cool_colors:
    print("My car is cool")
else:
    print("My car is not cool")