from borrow_books import issued_books
from store import issued_books_list, books
def return_books():
    name = input("Enter the name of the book to return: ")
    if name in issued_books_list:
        issued_books_list.remove(name)
        books.append(name)
        print(name , 'is returned')
    else:        
        print(name , 'book is not issued')

