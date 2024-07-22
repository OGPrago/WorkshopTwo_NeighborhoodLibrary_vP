class Book:
    def __init__(self, id, isbn, title, isCheckedOut = False, checkdOutTo = ""):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.isCheckedOut = isCheckedOut
        self.checkedOutTo = checkdOutTo
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
        
    def getIsbn(self):
        return self.isbn
    
    def setIsbn(self, isbn):
        self.isbn = isbn
        
    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        self.title = title
        
    def getIsCheckedOut(self):
        return self.isCheckedOut
    
    def setIsCheckedOut(self, isCheckedOut):
        self.isCheckedOut = isCheckedOut
        
    def getCheckedOutTo(self):
        return self.checkedOutTo
    
    def setCheckedOutTo(self, checkedOutTo):
        self.checkedOutTo = checkedOutTo
        
    def checkOut(self, borrowerName):
        if not self.isCheckedOut:
            self.isCheckedOut = True
            self.checkedOutTo = borrowerName
            return True
        else:
            return False
        
    def checkIn(self):
        if self.isCheckedOut:
            self.isCheckedOut = False
            self.checkedOutTo = ""
            return True
        else:
            return False