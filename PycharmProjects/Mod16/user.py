class User:
    def __init__(self, first_name = '', last_name = '', city = '', status = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.status = status

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_city(self, city):
        self.city = city

    def set_status(self, status):
        self.status = status

    def get_info_user(self):
        return (f'"{self.first_name} {self.last_name}, г. {self.city}, '
                f'статус "{self.status}"')
