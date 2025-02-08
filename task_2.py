# Завдання 2

# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» 
# за умови, що користувач повинен мати можливість вказати рівень рекурсії.

import turtle

def koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)
        turtle.right(120)
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)

def draw_snowflake(length, depth):
    for _ in range(3):
        koch_snowflake(length, depth)
        turtle.right(120)

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    length = 300
    turtle.speed(0)
    draw_snowflake(length, level)
    turtle.done()

