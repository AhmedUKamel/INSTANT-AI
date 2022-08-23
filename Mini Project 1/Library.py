from getpass import getpass
from User import *
class Library:
    def __init__(self,name):
        self.name = name
        self.__all_books = list()
        self.__borrowed_books = dict()
        self.__users = set()
    def __init__(self,books,name,users=set()):
        self.name = name
        self.__all_books = books
        self.__borrowed_books = dict()
        self.__users = users
    def add_book(self,book_name):
        if book_name in self.__all_books:
            print(f'{book_name} already exist')
            return False
        else:
            self.__all_books.append(book_name)
            print(f'{book_name} added successfully')
            return True
    def remove_book(self,book_name):
        if book_name not in self.__all_books:
            print(f'{book_name} is not exist')
            return False
        else:
            if book_name in self.__borrowed_books.keys():
                print('Can\'t remove already lent book')
                return False
            self.__all_books.remove(book_name)
            print(f'{book_name} removed successfully')
            return True
    def display_books(self):
        print('| ',end='')
        for book in self.__all_books:
            print(book,end=' | ')
    def borrowed_books(self):
        print('| ',end='')
        for book,user in self.__borrowed_books.items():
            print(f'{book} to {user}',end=' | ')
    def lend_book(self,book_name,user):
        if book_name in self.__all_books:
            if user.borrow_book(book_name):
                try:
                    self.__borrowed_books[book_name].append(str(user))
                    return True
                except:
                    self.__borrowed_books[book_name] = list()
                    self.__borrowed_books[book_name].append(str(user))
                    return True
        else:
            print(f'{book_name} is not in library')
            return False
    def return_book(self,book_name,user):
        if user.return_book(book_name):
            self.__borrowed_books[book_name].remove(str(user))
            if not len(self.__borrowed_books[book_name]):
                del self.__borrowed_books[book_name]
            return True
        else: return False
    def signup(self):
        un = input('Enter username: ')
        for _ in self.__users:
            if un == _.username:
                print(f'{un} already exist')
                return False
        fn = input('Enter full name: ')
        pw = getpass('Enter password: ')
        if getpass('Confirm password: ') != pw:
            print('Incorrect confirmation')
            return False
        self.__users.append(User(fn,un,pw))
        return True
    def signin(self):
        un = input('Enter username: ')
        user = None
        for _ in self.__users:
            if un == _.username:
                user = _
        if user == None:
            print(f'{un} is not exist')
            return False
        pw = getpass('Enter password: ')
        if user.login(pw):
            return user
        else: 
            print('Incorrect password')
            return False