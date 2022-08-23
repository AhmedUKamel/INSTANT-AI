from getpass import getpass
class User:
    # Constructor
    def __init__(self,full_name,username,password):
        self.full_name = full_name
        self.username = username
        self.__password = password
        self.__borrowed_books = set()
        print(f'{self.username}\'s account created successfully')
    # Destructor
    def __del__(self):
        print(f'{self.username}\'s account deleted successfully')
    # Description
    def __str__(self):
        return self.username
    # Add book to user
    def borrow_book(self,book_name):
        if book_name in self.__borrowed_books:
            print(f'{book_name} already borrowed')
            return False
        else:
            self.__borrowed_books.add(book_name)
            print(f'{book_name} borrowed successfully')
            return True
    # Remove book from user
    def return_book(self,book_name):
        if book_name not in self.__borrowed_books:
            print(f'{book_name} is not borrowed')
            return False
        else:
            self.__borrowed_books.discard(book_name)
            print(f'{book_name} returned successfully')
            return True
    # Change password
    def update_password(self):
        if getpass('Enter old password: ') == self.__password:
            new = getpass('Enter new password: ')
            if getpass('Confirm new password: ') == new:
                self.__password = new
                print('Password changed seccessfully')
                return True
            else:
                print('Incorrect confirmation')
                return False
        else:
            print('Incorrect password')
            return False
    # Log-In
    def login(self,password):
        return password == self.__password
    # Display borrowed books
    def display_books(self):
        print('| ',end='')
        for _ in self.__borrowed_books:
            print(_,end=' | ')