class Library:
    def __init__(self):
        self.noBooks = 0;
        self.book = [];
        #  yaha se me add karunga books
    def addBook(self , bookname):
        self.book.append(bookname);
        self.noBooks = len(self.book)
        #  ye to m print karva diya 
    def show(self):
        print(f"the number of books are {self.noBooks} and the name of book is ")
        for b in self.book:
            print(b)
l1 = Library();
l1.addBook("prabhat")
l1.addBook("prabhat")
l1.addBook("prabhat")


l1.addBook("prabhat")
l1.show()