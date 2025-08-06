import os

# Създава папката 'data', ако не съществува
os.makedirs("data", exist_ok=True)


from library import Library
from library_ui import add_book_interactively, interactive_edit_book, remove_book_interactively
# from library_ui import interactive_edit_book
# from library_ui import remove_book_interactively

 # меню


def show_menu():
    print("\n📖 Библиотечна система")
    print("1. 📘 Добави нова книга")
    print("2. ✏️ Редактирай книга")
    print("3. ❌ Изтрий книга")
    print("4. 🔍 Покажи всички книги")
    print("5. 🚪 Изход")


def main():
    library = Library()
    library.load_from_file("data/library.json")
    while True:
        show_menu()
        choice = input("\nВъведи опция: ")

        if choice == "1":
            
            while True:
                if input("Ще добавиш ли нова книга? (y/n): ").lower() != "y":
                    break
                else:
                    add_book_interactively(library)
        
        # абсолютен път до файла library.json
                    library.save_to_file("c:/Users/Svetla/My_Python/Lab_project/my_library_project/data/library.json")


        elif choice == "2":
            interactive_edit_book(library)

        elif choice == "3":
            isbn = input("Въведи ISBN за изтриване: ")
            library.remove_book(isbn)

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            print("👋 Довиждане!")
            break

        else:
            print("⚠️ Невалидна опция. Опитай отново.")


if __name__ == "__main__":
    main()
  






