def bank(x, y):
    bal = x
    for _ in range(y):
        bal = bal * 1.1
    return print(bal)


bank(100, 5)
