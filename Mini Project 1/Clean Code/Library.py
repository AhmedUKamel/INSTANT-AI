from User import User
from getpass import getpass

class Library:
    
    def __init__(self,name,books=list(),users=list()):
        self.name = name
        self.__allBooks = books
        self.__lentBooks = dict()
        self.__users = users
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
        if self.__user == None:
            user = self.__getUser()
            if type(user) != str:
                if user.isCorrectPassword():
                    self.__user = user
                    return True
        return False
    
    def signup(self):
        if self.__user == None:
            user = self.__getNewUser()
            if user != None:
                self.__users.append(user)
                return True
        return False
    
    def signout(self):
        if self.__user != None:
            self.__user = None
            return True
        return False
    
    def addBook(self):
        if self.__user != None:
            if self.__user.isAdmin():
                bookName = self.__getBookName()
                if not self.__isBookExist(bookName):
                    self.__addBookToBooks(bookName)
                    return True
        return False
    
    def removeBook(self):
        if self.__user != None:
            if self.__user.isAdmin():
                bookName = self.__getBookName()
                if self.__isBookExist(bookName) and not self.__isBookBorrowed(bookName):
                    self.__removeBookFromBooks(bookName)
                    return True
        return False
    
    def borrowBook(self):
        if self.__user != None:
            bookName = self.__getBookName()
            if self.__isBookExist(bookName):
                if self.__user.borrowBook(bookName):
                    self.__addBookToLentBooks(bookName)
                    return True
        return False
    
    def returnBook(self):
        if self.__user != None:
            bookName = self.__getBookName()
            if self.__isBookBorrowed(bookName):
                if self.__user.returnBook(bookName):
                    self.__removeBookFromLentBooks(bookName)
                    return True
        return False
    
    def showProfile(self):
        if self.__user != None:
            self.__user.profile()
            return True
        return False
    
    def showUserBooks(self):
        if self.__user != None:
            self.__user.displayMyBooks()
            return True
        return False
    
    def showAllBooks(self):
        if len(self.__allBooks)  == 0:
            print('No books in Library')
        else:
            print('Library books: | ',end='')
            for book in self.__allBooks:
                print(f'{book} | ',end='')
    
    def showLentBooks(self):
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
        if self.__user != None:
            if self.__user.isAdmin():
                user = self.__getNewUser()
                if user != None:
                    self.__users.append(user)
                    return True
        return False
    
    def addAdmin(self):
        if self.__user != None:
            if self.__user.isAdmin():
                user = self.__getNewAdmin()
                if user != None:
                    self.__users.append(user)
                    return True
        return False
    
    def updatePassword(self):
        return self.__user.updatePassword()
    
    def isAdmin(self):
        if self.__user != None:
            return self.__user.isAdmin()
        return False