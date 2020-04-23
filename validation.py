import os


class Acces:
    def __str__(self):
        return "authentacion"

    @staticmethod
    def file_login():  # getting data from a acces.txt
        current_dir = os.getcwd()
        acces_file = 'acces.txt'
        acces_path = os.path.join(current_dir, acces_file)
        loaded_data = []
        with open(acces_path, 'r') as file:
            for line in file:
                line = line.strip()
                loaded_data.append(line)
            login = loaded_data[0]
            valid_login = login[login.find(':') + 2:]  # reads from text file password without 'Password: '
            password = loaded_data[1]
            valid_password = password[password.find(':') + 2:]
            tab = [valid_login, valid_password]

        return tab


    @classmethod
    def login(cls):  # gathers login and password from user
        login = input("Login: ")
        password = input("Password: ")
        return login.replace('\r', ''), password.replace('\r', '')


    @classmethod
    def is_valid(cls):
        tab = Acces.login()
        if tab[0] == Acces.file_login()[0] and tab[1] == Acces.file_login()[1]: # checks if login from file is == to user login
            return True
        else:
            return False


