class User:
    def __init__(self, first_name, last_name):
        self.Fname = first_name
        self.Lname = last_name

    def sayName(self):
        print("Меня зовут,", self.Fname, self.Lname)

    def sayFirstame(self):
        print("Moe имя", self.Fname)

    def sayLastame(self):
        print("Моя фамилия", self.Lname)
