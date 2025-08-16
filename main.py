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
    print("="*40)
    print("Управление на книги")
    print("1. 📘 Добави нова книга")
    print("2. ✏️ Редактирай книга")
    print("3. ❌ Изтрий книга")
    print("4. 🔍 Покажи всички книги")
    
    print("\n Търсене и организация")
    
    print("5. 🔍 Търсене на книга")
    print("6. 🧮 Разширено филтриране")
   
    print("\n Анализ на колекцията")
    print("7. 📊 Статистика: общ брой и обща стойност")
    print("8. 📊 Разпределение на книгите по жанр")
    print("9. 📊 Съотношение прочетени спрямо непрочетени книги")
    print("10. 🚪 Изход")
    print("="*40)


def main():
    library = Library()
    library.load_from_file("./data/library.json")
    while True:
        show_menu()
        choice = input("\nВъведи опция: ")

        if choice == "1":
            
            while True:
                if input("Ще добавиш ли нова книга? (да/не): ").lower() != "да":
                    break
                else:
                    add_book_interactively(library)
        
        # относителен път до файла library.json
                    #library.save_to_file("c:/Users/Svetla/My_Python/Lab_project/my_library_project/data/library.json")
                    library.save_to_file("./data/library.json")


        elif choice == "2":
            interactive_edit_book(library)

        
        elif choice == "3":
            remove_book_interactively(library)
            library.save_to_file("./data/library.json")


        elif choice == "4":
            library.list_books()

        elif choice == "5":
            search_books_interactively(library)

       
        elif choice == "6":
            filter_books_interactively(library)

        elif choice == "7":
            library.generate_statistics()

        elif choice == "8":
            library.generate_statistics_genre()

        elif choice == "9":
            library.generate_statistics_read_unread()

        
        elif choice == "10":
            print("👋 Довиждане!")
            break

       
        else:
            print("⚠️ Невалидна опция. Опитай отново.")


if __name__ == "__main__":
     main()
  






