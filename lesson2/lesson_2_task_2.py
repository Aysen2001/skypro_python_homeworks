is_year_leap = input ('Введите год: ')
x = int(is_year_leap)
if x%4 == 0: print("год", x, ":", True)
else: print("год", x, ":", False)