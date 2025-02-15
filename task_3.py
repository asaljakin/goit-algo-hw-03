# Завдання 3 (необов'язкове завдання). Ханойські башти

# Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, використовуючи стрижень В як допоміжний.
# Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.

# Правила:
# 1. За один крок можна перемістити тільки один диск.
# 2. Диск можна класти тільки на більший диск або на порожній стрижень.

# Вхідними даними програми має бути число n — кількість дисків на початковому стрижні.
# Вихідними даними — логування послідовності кроків для переміщення дисків зі стрижня А на стрижень С.

# Наведемо приклад виконання коду для кількості дисків n = 3. На початковому стрижні вони розміщені так: [3, 2, 1], де 3 — найбільший диск, а 1 — найменший.

# Початковий стан: {'A': [3, 2, 1], 'B': [], 'C': []}
# Перемістити диск з A на C: 1
# Проміжний стан: {'A': [3, 2], 'B': [], 'C': [1]}
# Перемістити диск з A на B: 2
# Проміжний стан: {'A': [3], 'B': [2], 'C': [1]}
# Перемістити диск з C на B: 1
# Проміжний стан: {'A': [3], 'B': [2, 1], 'C': []}
# Перемістити диск з A на C: 3
# Проміжний стан: {'A': [], 'B': [2, 1], 'C': [3]}
# Перемістити диск з B на A: 1
# Проміжний стан: {'A': [1], 'B': [2], 'C': [3]}
# Перемістити диск з B на C: 2
# Проміжний стан: {'A': [1], 'B': [], 'C': [3, 2]}
# Перемістити диск з A на C: 1
# Проміжний стан: {'A': [], 'B': [], 'C': [3, 2, 1]}
# Кінцевий стан: {'A': [], 'B': [], 'C': [3, 2, 1]}

def hanoi(n, src, dest, aux, rods):
    if n == 1:
        disk = rods[src].pop()
        rods[dest].append(disk)
        print(f"Перемістити диск з {src} на {dest}: {disk}")
        print(f"Проміжний стан: {rods}")
    else:
        hanoi(n-1, src, aux, dest, rods)
        disk = rods[src].pop()
        rods[dest].append(disk)
        print(f"Перемістити диск з {src} на {dest}: {disk}")
        print(f"Проміжний стан: {rods}")
        hanoi(n-1, aux, dest, src, rods)

if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {rods}")
    hanoi(n, 'A', 'C', 'B', rods)
    print(f"Кінцевий стан: {rods}")

