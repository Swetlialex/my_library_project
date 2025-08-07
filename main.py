import os

# Създава папката 'data', ако не съществува
os.makedirs("data", exist_ok=True)


from library import Library
from library_ui import add_book_interactively, interactive_edit_book, remove_book_interactively
from library_ui import search_books_interactively
from library_ui import filter_books_interactively

 # меню


def show_menu():
    print("\n📖 Библиотечна система")
    print("\n Управление на книги")
    print("1. 📘 Добави нова книга")
    print("2. ✏️ Редактирай книга")
    print("3. ❌ Изтрий книга")
    print("4. 🔍 Покажи всички книги")
    
    print("\n Търсене и организация")
    
    print("5. 🔍 Търсене на книга")
    print("6. 🧮 Разширено филтриране")
   
    print("\n Анализ на колекцията")

    print("7. 🚪 Изход")



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
            search_books_interactively(library)

        elif choice == "6":
            filter_books_interactively(library)

        elif choice == "7":
            print("👋 Довиждане!")
            break


        else:
            print("⚠️ Невалидна опция. Опитай отново.")


if __name__ == "__main__":
    main()
  






