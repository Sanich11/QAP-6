class User:
    def __init__(self, first_name = '', last_name = '', balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_balance(self, balance):
        self.balance = balance

    def get_info_user(self):
        return (f'Клиент "{self.first_name} {self.last_name}". '
                f'Баланс: {self.balance} руб')

r = User('Иван', 'Петров', 50)

print(r.get_info_user())
