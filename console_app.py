from db import Books

version_code = 0.01


def console_page1():
    next_page = 10
    back = 0
    print(Books().get(10, formed=True))
    print("b-back     n-next")

    while True:

        inp = str(input("View All Books $/>")).strip().lower()
        if inp == "n":
            next_page = next_page + 10
            back = back + 10

        elif inp == "b":
            if back == 0:
                break
            else:
                back = back - 10
                next_page = next_page - 10

        elif inp == "bb":
            break

        print(Books().get_range(back, next_page, formed=True))
        print("b-back     n-next")


def console_page2():

    print("""
    Find Book : 
    1. By ID
    2. Book Name
    3. Book Author
    4. Book ISBN Nutmber
    
    """)

    while True:
        y = str(input("Find By $/> ")).strip().lower()


        if y == "b":
            break
        try:
            y = int(y)
            if y == 1:
                x = input("Enter ID $/>")
                print(Books().get_byId(x, formed=True))
            elif y == 2:
                x = input("Enter Book Name $/>")
                print(Books().get_byName(x, formed=True))
            elif y == 3:
                x = input("Enter Book Author $/>")
                print(Books().get_byAuthor(x, formed=True))
            elif y == 4:
                x = input("Enter Book ISBN $/>")
                print(Books().get_byISBN(x, formed=True))
        except ValueError:
            pass


def console_page3():
    book_name = str(input("Enter Book Name $/>"))
    book_author = str(input("Enter Book Author $/>"))
    book_isbn = str(input("Enter Book ISBN Number $/>"))
    Books().add(book_name, book_author, book_isbn)

    print(f"Added Records Successfully")


def console_page4():
    id = int(input("Enter Book Id $/> ").strip().lower())

    print(f"Selected - {Books().get_byId(id)}")

    book_name = str(input("Enter Book Name $/>"))
    book_author = str(input("Enter Book Author $/>"))
    book_isbn = str(input("Enter Book ISBN Number $/>"))
    Books().update_byId(id,book_name, book_author, book_isbn)

    print(f"Update Records Successfully")

def console_page5():
    id = int(input("Enter Book Id $/> ").strip().lower())

    print(f"Selected - {Books().get_byId(id)}")

    sure = (input("Are you sure? Yes(y) / No (n)").strip().lower())

    if sure == "y":
        Books().delete(id)
        print(f"Deleted Record With ID {id}")
    elif sure == "n":
        pass



def reset_console():
    Books().destroy_table()
    Books().create_database()
    Books().add_sample_data()
    print("Reset Successful.")


def help():
    print(f"""
       Library Management | v{version_code} 
       ====================================
       1. View All Books.
       2. Find Book.
       3. Add Book
       4. Update Book
       5. Delete Book 
       
       
       
       
       help - Get Help
       reset - Resets Database
       """)

def app_console():
    help()

    while True:
        x = str(input("$/> ")).strip().lower()
        if x == "1":
            console_page1()
        elif x == "2":
            console_page2()
        elif x == "3":
            console_page3()
        elif x == "4":
            console_page4()
        elif x == "5":
            console_page5()
        elif x == "reset":
            reset_console()
        elif x == "help":
            help()
        if x == "exit":
            break

if __name__ == "__main__" :
    app_console()