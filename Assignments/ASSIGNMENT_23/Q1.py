class bookstore:
    NoOfBooks = 0
    def __init__(self,A,B):
        self.Name = A
        self.Author = B
        bookstore.NoOfBooks = bookstore.NoOfBooks + 1


    def Display(self):
        print(f"{self.Name} by {self.Author}.   No of books: {bookstore.NoOfBooks}")

obj1 = bookstore("Linux Sysytem programming", "Rober love")
obj1.Display()

obj2= bookstore("C Programming", "Dennis Richtie")
obj2.Display()

