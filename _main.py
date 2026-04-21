from add_books import add_books
from borrow_books import issued_books
from show_books import show_books
from return_books import return_books
def library():
    while True:
        print('menu')
        print('1. Add Books')
        print('2. Show Books')
        print('3. Borrow Books')
        print('4. Return Books')
        print('5. Exit')

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issued_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank you for using the library.")
            break
        else:
            print("Invalid choice. Please try again.")
library()
