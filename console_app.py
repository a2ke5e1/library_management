version_code = 0.01
from db import Books


def console_page1():
    next = 10
    back = 0
    print(Books().get(10, formed=True))
    print("b-back     n-next")

    while True:

        x = str(input("View All Books $/>")).strip().lower()
        if x == "n":
            next = next + 10
            back = back + 10

        elif x == "b":
            if back == 0:
                break
            else:
                back = back - 10
                next = next - 10

        elif x == "bb":
            break

        print(Books().get_range(back, next, formed=True))
        print("b-back     n-next")


def console_page2():
    while True:
        y = str(input("Book ID $/> ")).strip().lower()
        if y == "b":
            break
        try:
            y = int(y)
            print(Books().get_byId(y, formed=True))
        except ValueError:
            pass


def reset_console():
    Books().destroy_table()
    Books().create_database()
    Books().add_sample_data()
    print("Reset Successful.")


print(f"""
Library Management | v{version_code} 
====================================
1. View All Books.
2. Find Book By ID.

reset - Resets Database
""")

while True:
    x = str(input("$/> ")).strip().lower()
    if x == "1":
        console_page1()
    elif x == "2":
        console_page2()
    elif x == "reset":
        reset_console()
    if x == "exit":
        break
