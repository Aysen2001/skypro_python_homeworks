def month_to_season(m):
    if m in [12, 1, 2]: return print("Зима")
    elif m in [3, 4, 5]: return print("Весна")
    elif m in [6, 7, 8]: return print("Лето")
    elif m in [9, 10, 11]: return print("Осень")
    else: return print("Нет такого месяца")

month_to_season(12)