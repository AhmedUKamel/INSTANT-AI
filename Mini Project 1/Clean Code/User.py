from getpass import getpass

class User:
    
    def __init__(self,fullName,username,password,isAdmin=False):
        self.__fullName = fullName
        self.__username = username
        self.__password = password
        self.__isAdmin  = isAdmin
        self.__books    = list()
        print(f'{self.__username}\'s account created successfully')
    
    def __del__(self):
        print(f'{self.__username}\'s account deleted successfully')
    
    def __str__(self):
        return self.__username
    
    def __isBookBorrowed(self,bookName):
        return bookName in self.__books
    
    def __addBookToBorrowed(self,bookName):
        self.__books.append(bookName)
    
    def __removeBookfromBorrowed(self,bookName):
        self.__books.remove(bookName)
    
    def __getConfirmedNewPassword(self):
        newPassword = getpass('Enter new password: ')
        if newPassword == getpass('Confirm new password: '):
            return newPassword
        del newPassword
        return None
    def isCorrectPassword(self):
        return getpass('Enter password: ') == self.__password
    
    def updatePassword(self):
        if self.isCorrectPassword():
            newPassword = self.__getConfirmedNewPassword()
            if newPassword != None:
                self.__password = newPassword
                return True
        return False

    def borrowBook(self,bookName):
        if self.__isBookBorrowed(bookName):
            return False
        else:
            self.__addBookToBorrowed(bookName)
            return True
    
    def returnBook(self,bookName):
        if self.__isBookBorrowed(bookName):
            self.__removeBookfromBorrowed(bookName)
            return True
        else:
            return False
    
    def displayMyBooks(self):
        if len(self.__books) == 0:
            print('No books found')
        else:
            print('My books:\t| ',end='')
            for book in self.__books:
                print(f'{book} | ',end='')

    def profile(self):
        print(f'Full Name:\t{self.__fullName}\nUsername:\t{self.__username}\nPassword:\t{self.__password}')
        if self.__isAdmin:
            print('Is admin:\tYes')
        else:
            print('Is admin:\tNo')
        self.displayMyBooks()
    
    def isAdmin(self):
        return self.__isAdmin == True