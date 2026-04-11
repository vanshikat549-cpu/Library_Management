from store import books
def add_books():
    name = input("Enter the name of the book: ")
    books.append(name)
    print(name , 'is added')
