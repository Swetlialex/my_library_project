# library_ui.py 
# функция, която добавя книга към библиотеката
# Извън класа (глобална)
# Тя се занимава с потребителски интерфейс – не е част от самата библиотека

# добавя книга в библиотеката
def add_book_interactively(library):
    print("\nДобавяне на нова книга:")
    title = input("Заглавие: ")
# 


    authors = input("Автор/и (разделени със запетая): ").split(",")
    isbn = input("ISBN: ")
    pub_year = int(input("Година на публикуване: "))
    publisher = input("Издателство: ")
    genre = input("Жанр (проза или поезия): ")
    page_count = int(input("Брой страници: "))
    format_ = input("Формат (твърди корици, меки корици, електронна книга): ")
    price = float(input("Цена: "))
    purchase_date = input("Дата на покупка (гггг-мм-дд): ")
    rating = int(input("Оценка (1-5): "))
    read_status = input("Статус на четене (прочетена, непрочетена, в процес на четене): ")
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
    print(f"✅ Книгата „{title}“ беше добавена успешно.")

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

    # търсене на книга
def search_books_interactively(library):
    query = input("🔍 Въведи заглавие, автор или ISBN: ")
    results = library.search_books(query)
    if results:
        print(f"\n📚 Намерени книги ({len(results)}):")
        for isbn, book in results:
            print(f"{book['Title']} — {', '.join(book['Author_s'])} (ISBN: {isbn})")
    else:
        print("❌ Няма съвпадения.")


    # разширено филтриране по жанр, статус, година, рейтинг, тагове
def filter_books_interactively(library):
    print("\n🔎 Разширено филтриране:")
    genres = input("Жанрове (проза или поезия / разделени със запетая, или празно): ").split(",") if input("Филтрирай по жанр? (y/n): ").lower() == "y" else None
    status = input("Статус на четене (read/unread/in progress): ") if input("Филтрирай по статус? (y/n): ").lower() == "y" else None
    year_range = None
    if input("Филтрирай по година? (да/не): ").lower() == "да":
        try:
            start = int(input("От година: "))
            end = int(input("До година: "))
            year_range = (start, end)
        except ValueError:
            print("⚠️ Невалиден диапазон.")
    rating_range = None
    if input("Филтрирай по рейтинг? (да/не): ").lower() == "да":
        try:
            min_r = int(input("Минимален рейтинг: "))
            max_r = int(input("Максимален рейтинг: "))
            rating_range = (min_r, max_r)
        except ValueError:
            print("⚠️ Невалиден рейтинг.")
    tags = input("Тагове/ключови думи: ").split(",") if input("Филтрирай по тагове? (да/не): ").lower() == "да" else None

    results = library.filter_books(
        genres=[g.strip() for g in genres] if genres else None,
        status=status,
        year_range=year_range,
        rating_range=rating_range,
        tags=[t.strip() for t in tags] if tags else None
    )

    if results:
        print(f"\n📚 Намерени книги ({len(results)}):")
        for isbn, book in results:
            print(f"{book['Title']} — {', '.join(book['Author_s'])} (ISBN: {isbn})")
    else:
        print("❌ Няма съвпадения.")

    


