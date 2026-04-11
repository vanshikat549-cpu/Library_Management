from store import books, issued_books_list
def issued_books():
    name = input("Enter the name of the book to borrow: ")
    if name in books:
        issued_books_list.append(name)
        print(name , 'is issued')
    else:
        print(name , 'book is not available')

