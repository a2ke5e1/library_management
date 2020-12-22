version_code = 0.01
from db import Books

print(f"""
Library Management | v{version_code} 
====================================
1. View All Books.
""")

while True:
    x = str(input("$/> ")).strip()
    if x == "1":
        print(Books().get(10, formed=False))
    if x == "exit":
        break
