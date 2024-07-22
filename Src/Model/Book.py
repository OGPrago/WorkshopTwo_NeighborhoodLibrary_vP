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
        
    