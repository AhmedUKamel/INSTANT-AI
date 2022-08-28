from Library import Library

class Website:
    
    def __init__(self,library):
        self.__library = library      
        
    def mainPage(self):
        print(f'Welcome in {self.__library.name}')
        message = '''\t1.Sign In
        2.Sign Up
        3.Show library books
        4.Exit website
        Answer: '''
        while True:
            ans = input(message).strip()
            if ans == '1':
                if self.__library.signin():
                    self.__dashboard()
                else:
                    print('Invalid username or password')
            elif ans == '2':
                if not self.__library.signup():
                    print('Username is already exist or password not confirmed')
            elif ans == '3':
                self.__library.showAllBooks()
            elif ans == '4':
                return
            else:
                print('Invalid input, please try again')
    
    def __dashboard(self):
        message = '''\t1.Profile
        2.Update my password
        3.Show library books
        4.Show my books
        5.Show lent books (only admins)
        6.Add/remove - books/users (only admins)
        7.Borrow a book
        8.Return a book
        9.Log out
        Answer: '''
        while True:
            ans = input(message).strip()
            if ans == '1': self.__library.showProfile()
            elif ans == '2':
                if self.__library.updatePassword():
                    print('Password has been updated successfully')
                else:
                    print('Incorrect password')
            elif ans == '3': self.__library.showAllBooks()
            elif ans == '4': self.__library.showUserBooks()
            elif ans == '5':
                if not self.__library.showLentBooks():
                    print('You have no admin permissions')
            elif ans == '6':
                if self.__library.isAdmin():
                    self.__adminsPage()
                else:
                    print('You have no admin permissions')
            elif ans == '7':
                if self.__library.borrowBook():
                    print('Book has been borrowed successfully')
                else:
                    print('Book is not exist or you already borrowed before')
            elif ans == '8':
                if self.__library.returnBook():
                    print('Book has been returned successfully')
                else:
                    print('Book is not borrowed')
            elif ans == '9': 
                if self.__library.signout(): return
            else: print('Invalid input, please try again')
    
    def __adminsPage(self):
        message = '''\t1.Add new user
        2.Add new admin
        3.Add new book
        4.Remove a book
        5.Go back
        Answer: '''
        while True:
            ans = input(message).strip()
            if ans == '1':
                if self.__library.addUser():
                    print('User has been added successfully')
                else:
                    print('Username already exist or incorrect password')
            elif ans == '2':
                if self.__library.addAdmin():
                    print('Admin has been added successfully')
                else:
                    print('Username already exist or incorrect password')
            elif ans == '3':
                if self.__library.addBook():
                    print('Book has been added successfully')
                else:
                    print('Book already exist')
            elif ans == '4':
                if self.__library.removeBook():
                    print('Book has been removed successfully')
                else:
                    print('Book is not exist or borrowed by some users')
            elif ans == '5': return
            else: print('Invalid input, please try again')