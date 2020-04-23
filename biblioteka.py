import os
import validation # another self-made file is used for log-in purposes


class Book:  # outer class

    class Date:  # borrowing date # inner class
        def __init__(self):
            self.year = 0
            self.month = 0
            self.day = 0

        # method used to fill inner class Date with data
        def borrow_date(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    def __init__(self, id, title, category, a_name, a_surname):
        # 'a' means author
        # 'bd means borrower details'
        self.id = id
        self.title = title
        self.category = category
        self.a_name = a_name
        self.a_surname = a_surname
        # basic settings because book is not borrowed
        self.borrowed = False
        self.bd_name = 'none'
        self.bd_surname = 'none'
        # inner class inicialization
        self.date = self.Date()

    def is_borrowed(self):
        self.borrowed = True

    def borrower_details(self, bd_name, bd_surname):
        self.bd_name = bd_name
        self.bd_surname = bd_surname


# main book container
book_list = []

book_id = 1


# 1

def add_book():
    global book_id
    print('''Press 'x' anywhere to exit''')
    title = input("Type title: ")
    if title == 'x':
        menu()
    category = input("Type category: ")
    if category == 'x':
        menu()
    a_name = input("Type author name: ")
    if a_name == 'x':
        menu()
    a_surname = input("Type author surname: ")
    if a_surname == 'x':
        menu()
    new_book = Book(book_id, category, title, a_name, a_surname)
    book_list.append(new_book)
    print("Book have been added sucessifly, book ID: %s \n" % book_id)
    book_id += 1


def delete_book():
    if len(book_list) > 0:  # checks if list is not empty
        is_found = False
        search_key = input("1. Delete by ID\n"
                           "2. Delete by title\n"
                           "3. Exit\n"
                           "Your choice: ")
        if search_key == '1':
            search_id = input("ID: ")
            for book in book_list:
                if int(search_id) == int(book.id):
                    book_list.remove(book)
                    is_found = True
            if not is_found:
                print("No match results for ID: %s" % search_id)

        elif search_key == '2':
            search_title = input("Title: ")
            for book in book_list:
                if str(search_title) == str(book.title):
                    book_list.remove(book)
                    is_found = True
            if not is_found:
                print("No match results for title: %s" % search_title)

        elif search_key == '3':
            menu()

        else:
            print("You typed wrong value")
            delete_book()

    else:
        print("There is no books in library")


def search_books_by_id():
    is_found = False
    search_id = input("Select ID: ")
    for book in book_list:
        if str(book.id) == str(search_id):
            print("\nResults: ")
            print("___________________")
            print("ID: %s" % book.id)
            print("___________________")
            print("Title: %s" % book.title)
            print("Author name: %s" % book.a_name)
            print("Author surname: %s" % book.a_surname)
            print("___________________")
            is_found = True

    if not is_found:
        print("There is no search results for ID: %s" % search_id)


def search_books_by_title():
    is_found = False
    search_title = input("Select Title: ")
    for book in book_list:
        if str(book.id) == str(search_title):
            print("\nResults: ")
            print("___________________")
            print("Title: %s" % book.title)
            print("___________________")
            print("ID: %s" % book.id)
            print("Author name: %s" % book.a_name)
            print("Author surname: %s" % book.a_surname)
            print("___________________")
            is_found = True
    if not is_found:
        print("There is no search results for title: %s" % search_title)


# 4
def change_status():
    if len(book_list) > 0:
        is_found = False
        search_id = input("Select ID of borrowed book: ")
        for book in book_list:
            if int(search_id) == int(book.id):
                is_found = True
                print("Borrower details ")
                bd_name = input("Name: ")
                bd_surname = input("Surname: ")
                book.borrower_details(bd_name, bd_surname)
                print("Type date ")
                year = input("Year : ")
                month = input("Month : ")
                day = input("Day : ")
                book.date.borrow_date(year, month, day)
                book.is_borrowed()
                print("Status changed successfully !")
        if not is_found:
            print("No search results for ID: %s" % search_id)
    else:
        print("\nYou cannot change the status if library database is empty\n")


# 5
def show_all_borrowed():
    if len(book_list) > 0:
        is_found = False
        print("Borrowed books: ")
        for book in book_list:
            if book.borrowed:
                print("___________________")
                print("Title: %s" % book.title)
                print("ID: %s" % book.id)
                print("___________________")
                print("Borrowed by: ")
                print("Borrower name: %s" % book.bd_name)
                print("Borrower surname: %s" % book.bd_surname)
                print("On date: ")
                print("Year: %s Month: %s Day: %s" % (book.date.year, book.date.month, book.date.day))
                print("___________________")
                is_found = True
        if not is_found:
            print("There is no books borrowed")
    else:
        print("Library database is empty !")


# def load_file():
#     line_nr = 1  # used to count line lines
#     filename = input("Type filename: ")
#     book_list.clear()  # clears book list before loading new list
#     current_dir = os.getcwd()
#     filepath = os.path.join(current_dir, filename)
#     if os.path.exists(filepath):
#         with open(filepath, "r") as file:
#             for line in file:
#                 print(file.readlines()[1])
#                 # new_book = Book
#                 # for line in file.split('\n'):
#                 #     print(line)

def save_file():
    filename = input("Type filename: ")
    current_dir = os.getcwd()
    filepath = os.path.join(current_dir, filename)
    file = open(filename, "w")
    for f in book_list:
        file.write(str(f.id) + '\n')
        file.write(str(f.title) + '\n')
        file.write(str(f.category) + '\n')
        file.write(str(f.a_name) + '\n')
        file.write(str(f.a_surname) + '\n')
        file.write(str(f.borrowed) + '\n')
        file.write(str(f.bd_name) + '\n')
        file.write(str(f.bd_surname) + '\n')
        file.write(str(f.date.year) + '\n')
        file.write(str(f.date.month) + '\n')
        file.write(str(f.date.day) + '\n')
    file.close()


def load_file():
    filename = input("Type filename: ")
    current_dir = os.getcwd()
    filepath = os.path.join(current_dir, filename)
    loaded_data = []  # creates a copy of file as a list
    with open(filepath, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            loaded_data.append(line)

    while True:
        new_book = Book((str(loaded_data[0])), loaded_data[1], loaded_data[2], loaded_data[3], loaded_data[4])
        new_book.borrowed = loaded_data[5]
        new_book.bd_name = loaded_data[6]
        new_book.bd_surname = loaded_data[7]
        new_book.date.year = loaded_data[8]
        new_book.date.month = loaded_data[9]
        new_book.date.day = loaded_data[10]
        book_list.append(new_book)
        del loaded_data[:11]  # if book is loaded, it reset index of loaded_data.
        if len(loaded_data) <= 0:
            break
            menu()
        else:
            continue


def menu():
    print("---Welcome to library management system---")
    menu_choice = input("1. Add book\n"
                        "2. Delete book\n"
                        "3. Search book\n"
                        "4. Change status of the book\n"
                        "5. View all borrowed books\n"
                        "6. Save data to a file\n"
                        "7. Load data from file\n"
                        "Your choice: ")

    if menu_choice == '1':
        add_book()
        menu()

    elif menu_choice == '2':
        delete_book()
        menu()

    elif menu_choice == '3':
        while len(book_list) > 0:  # checks if list is not empty
            temp_choice = input("1. By ID\n"
                                "2. By title\n"
                                "3. Exit\n"
                                "Your choice: ")
            if temp_choice == '1':
                search_books_by_id()
                menu()
                break
            elif temp_choice == '2':
                search_books_by_title()
                menu()
                break
            elif temp_choice == '3':
                menu()
                break
            else:
                print("You typed incorrect value !")
                continue
        else:
            print("\nYou cannot do search, the library database is empty\n")
            menu()

    elif menu_choice == '4':
        change_status()
        menu()

    elif menu_choice == '5':
        show_all_borrowed()
        menu()

    elif menu_choice == '6':
        save_file()
        menu()

    elif menu_choice == '7':
        load_file()
        menu()


while True:

    if validation.Acces.is_valid():
        menu()
        break
    else:
        print("Wrong validation !, no acces grainted")
        continue