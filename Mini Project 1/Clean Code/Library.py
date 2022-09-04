from User import User
from getpass import getpass

class Library:
    
    def __init__(self,name,books=list(),users=list()):
        '''
         class to represent a library.

        ...

        Attributes
        ----------
        name : str
            name of the library
        allBooks : list
            list of available books in the library
        users : list
            List of users accounts for the library
        lentBooks : dict
            dictionary of lent books and their users 
        user : User
            represent the current user
        '''
        self.name = name
        self.__allBooks = books
        self.__users = users
        self.__lentBooks = dict()
        self.__user = None
    
    def __getUser(self):
        username = input('Enter username: ')
        for user in self.__users:
            if username == str(user):
                return user
        return username
    
    def __getConfirmedNewPassword(self):
        newPassword = getpass('Enter new password: ')
        if newPassword == getpass('Confirm new password: '):
            return newPassword
        return None
    
    def __getNewUser(self):
        fullname = input('Enter Full Name: ')
        username = self.__getUser()
        if type(username) == str:
            password = self.__getConfirmedNewPassword()
            if password != None:
                return User(fullname,username,password)
        return None
    
    def __getNewAdmin(self):
        fullname = input('Enter Full Name: ')
        username = self.__getUser()
        if type(username) == str:
            password = self.__getConfirmedNewPassword()
            if password != None:
                return User(fullname,username,password,True)
        return None
    
    def __getBookName(self):
        return input('Enter book name: ')
    
    def __isBookExist(self,bookName):
        return bookName in self.__allBooks
    
    def __isBookBorrowed(self,bookName):
        return bookName in self.__lentBooks.keys()
    
    def __addBookToBooks(self,bookName):
        self.__allBooks.append(bookName)
        
    def __addBookToLentBooks(self,bookName):
        try:
            self.__lentBooks[bookName].append(str(self.__user))
        except:
            self.__lentBooks[bookName] = list()
            self.__lentBooks[bookName].append(str(self.__user))
    
    def __removeBookFromLentBooks(self,bookName):
        self.__lentBooks[bookName].remove(str(self.__user))
        if len(self.__lentBooks[bookName]) == 0:
            del self.__lentBooks[bookName]
    
    def __removeBookFromBooks(self,bookName):
        self.__allBooks.remove(bookName) 
    
    def signin(self):
        '''
        This function sign in user's account if exists.
        '''
        if self.__user == None:
            user = self.__getUser()
            if type(user) != str:
                if user.isCorrectPassword():
                    self.__user = user
                    return True
        return False
    
    def signup(self):
        '''
        This function creates a new user's account.
        '''
        if self.__user == None:
            user = self.__getNewUser()
            if user != None:
                self.__users.append(user)
                return True
        return False
    
    def signout(self):
        '''
        This function sign out from the current user account.
        '''
        if self.__user != None:
            self.__user = None
            return True
        return False
    
    def addBook(self):
        '''
        This function adds a new book to the library collection.
        '''
        if self.__user != None:
            if self.__user.isAdmin():
                bookName = self.__getBookName()
                if not self.__isBookExist(bookName):
                    self.__addBookToBooks(bookName)
                    return True
        return False
    
    def removeBook(self):
        '''
        This function removes a book from the library if and only if no user is borrowing it.
        '''
        if self.__user != None:
            if self.__user.isAdmin():
                bookName = self.__getBookName()
                if self.__isBookExist(bookName) and not self.__isBookBorrowed(bookName):
                    self.__removeBookFromBooks(bookName)
                    return True
        return False
    
    def borrowBook(self):
        '''
        This function lends a book from the library to the current user.
        '''
        if self.__user != None:
            bookName = self.__getBookName()
            if self.__isBookExist(bookName):
                if self.__user.borrowBook(bookName):
                    self.__addBookToLentBooks(bookName)
                    return True
        return False
    
    def returnBook(self):
        '''
        This function returns a borrowed book from the current user to the library.
        '''
        if self.__user != None:
            bookName = self.__getBookName()
            if self.__isBookBorrowed(bookName):
                if self.__user.returnBook(bookName):
                    self.__removeBookFromLentBooks(bookName)
                    return True
        return False
    
    def showProfile(self):
        '''
        This function displays all information about the current user.
        
        INFO: Full name, username, password, and already borrowed books.
        '''
        if self.__user != None:
            self.__user.profile()
            return True
        return False
    
    def showUserBooks(self):
        '''
        This function displays each book available in the user's collection.
        '''
        if self.__user != None:
            self.__user.displayMyBooks()
            return True
        return False
    
    def showAllBooks(self):
        '''
        This function displays each book available in the library.
        '''
        if len(self.__allBooks)  == 0:
            print('No books in Library')
        else:
            print('Library books: | ',end='')
            for book in self.__allBooks:
                print(f'{book} | ',end='')
    
    def showLentBooks(self):
        '''
        This function displays each lent book with users who lent.
        '''
        if self.__user != None:
            if self.__user.isAdmin():
                if len(self.__lentBooks)  == 0:
                    print('No lent books')
                else:
                    print('Lent books: | ',end='')
                    for book,users in self.__lentBooks.items():
                        print(f'{book} to {users} | ',end='')
                return True
        return False
    
    def addUser(self):
        '''
        This function adds a new user.
        '''
        if self.__user != None:
            if self.__user.isAdmin():
                user = self.__getNewUser()
                if user != None:
                    self.__users.append(user)
                    return True
        return False
    
    def addAdmin(self):
        '''
        This function adds a new user as an admin.
        '''
        if self.__user != None:
            if self.__user.isAdmin():
                user = self.__getNewAdmin()
                if user != None:
                    self.__users.append(user)
                    return True
        return False
    
    def updatePassword(self):
        '''
        This function updates the current user's password.
        '''
        return self.__user.updatePassword()
    
    def isAdmin(self):
        '''
        This function returns either if the current user is admin or not.
        '''
        if self.__user != None:
            return self.__user.isAdmin()
        return False