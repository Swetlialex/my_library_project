# library_ui.py 
# функция, която добавя книга към библиотеката
# Извън класа (глобална)
# Тя се занимава с потребителски интерфейс – не е част от самата библиотека

def add_book_interactively(library):
    print("\nДобавяне на нова книга:")
    title = input("Заглавие: ")
    authors = input("Автор/и (разделени със запетая): ").split(",")
    isbn = input("ISBN: ")
    pub_year = int(input("Година на публикуване: "))
    publisher = input("Издателство: ")
    genre = input("Жанр: ")
    page_count = int(input("Брой страници: "))
    format_ = input("Формат: ")
    price = float(input("Цена: "))
    purchase_date = input("Дата на покупка (гггг-мм-дд): ")
    rating = int(input("Оценка (1-5): "))
    read_status = input("Статус на четене: ")
    notes = input("Бележки/тагове: ")

    library.add_book(
        Title=title,
        Author_s=[a.strip() for a in authors],
        ISBN=isbn,
        Publication_Year=pub_year,
        Publisher=publisher,
        Genre=genre,
        Page_Count=page_count,
        Format=format_,
        Price=price,
        Purchase_Date=purchase_date,
        Personal_Rating=rating,
        Read_Status=read_status,
        Tags_Notes=notes
    )

# нова глобална функция за редактиране на данни за книга
def interactive_edit_book(library):
    if not library.books:
        print("Няма книги за редактиране.")
        return

    print("\nНалични книги:")
    for i, (isbn, book) in enumerate(library.books.items(), start=1):
        print(f"{i}. {book['Title']} — ISBN: {isbn}")
    
    try:
        choice = int(input("\nВъведи номера на книгата за редактиране: "))
        selected_isbn = list(library.books.keys())[choice - 1]
    except (ValueError, IndexError):
        print("Невалиден избор.")
        return

    print(f"\nРедакция на: {library.books[selected_isbn]['Title']} (ISBN: {selected_isbn})")
    print("Натисни Enter, ако не искаш да променяш дадено поле.")

    new_title = input("Новото заглавие: ")
    new_price = input("Нова цена: ")
    new_notes = input("Нови бележки/тагове: ")

    kwargs = {}
    if new_title: kwargs["Title"] = new_title
    if new_price:
        try:
            kwargs["Price"] = float(new_price)
        except ValueError:
            print("Цената не беше валидна и няма да бъде променена.")
    if new_notes: kwargs["Tags_Notes"] = new_notes

    # Извикване на метода за редактиране
    library.edit_book(selected_isbn, **kwargs)

# нова глобална функция за изтриване на книга
def remove_book_interactively(library):
    if not library.books:
        print("Няма книги за изтриване.")
        return

    print("\nНалични книги:")
    for i, (isbn, book) in enumerate(library.books.items(), start=1):
        print(f"{i}. {book['Title']} — ISBN: {isbn}")

    try:
        choice = int(input("\nВъведи номер на книга за изтриване: "))
        selected_isbn = list(library.books.keys())[choice - 1]
    except (ValueError, IndexError):
        print("Невалиден избор.")
        return

    # Извикване на метода за изтриване
    library.remove_book(selected_isbn)


