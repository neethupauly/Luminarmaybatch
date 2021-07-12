# 3. Create a Book class with instance Library_name, book_name, author, pages?

class Book:

    def setval(self, Library_name, book_name, author, pages):
        self.Library_name = Library_name
        self.book_name = book_name
        self.author = author
        self.pages = pages

    def printval(self):
        print(self.Library_name, self.book_name, self.author, self.pages)


bk = Book()
l = input("enter Library name")
b = input("enter book name")
a = input("enter author name")
p = int(input("enter pages"))
bk.setval(l, b, a, p)
bk.printval()