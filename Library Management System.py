library = []

def add_book(title):
    library.append({"title": title, "borrowed": False})
    print(f"Book '{title}' added.")

def display_books():
    print("
Library Books:")
    for idx, book in enumerate(library):
        status = "Borrowed" if book["borrowed"] else "Available"
        print(f"{idx + 1}. {book['title']} - {status}")

def borrow_book(index):
    if not library[index]["borrowed"]:
        library[index]["borrowed"] = True
        print(f"You have borrowed '{library[index]['title']}'.")
    else:
        print("Book already borrowed.")

def return_book(index):
    if library[index]["borrowed"]:
        library[index]["borrowed"] = False
        print(f"You have returned '{library[index]['title']}'.")
    else:
        print("Book was not borrowed.")

