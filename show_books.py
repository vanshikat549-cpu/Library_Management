from store import books
def show_books():
    if len(books) == 0 :
        print("No books in the list.")
    else:
        print("Books in the list:")
        for b in books:
            print(b)

