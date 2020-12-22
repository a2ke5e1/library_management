version_code = 0.01
from db import Books

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
        print(Books().get(10, formed=True))
    elif x == "2":
        y = int(str(input("Book ID $/> ")).strip())
        print(Books().get_byId(y, formed=True))

    elif x == "reset":
        Books().destroy_table()
        Books().create_database()
        Books().add_sample_data()
        print("Reset Successful.")
    if x == "exit":
        break
