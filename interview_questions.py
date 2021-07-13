# class Books:
#
# find book()
# find number of copies
# sort authors using sold books
books={
    "alchemist":{"book_name":"alchemist","author":"paulo","price":200,"copies":200},
     "alch":{"book_name":"alch","author":"paul","price":250,"copies":0}
 }
#     def find_book(self,book_name):
#         name=book_name["book_name"]
#
#         books=self.find_book(book_name)
#         if name in books:

res=sorted(books.items(),key=lambda x:x[1]["copies"],reverse=True)
# print(res)
for val in res:
    print(val[1]["author"])

# ex: persons={"id":100,"name":"ram","age":25}
# for key,value in persons.items():
#     print(key,value)