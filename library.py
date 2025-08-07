import json

class Library:
    def __init__(self):
        self.books = {}


    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.books = json.load(f)
            print(f"Заредени книги от {filename}")
        except FileNotFoundError:
            print(f"Файлът {filename} не съществува. Започваме с празна библиотека.")
        except json.JSONDecodeError:
            print(f"Грешка при четене на {filename}. Проверете формата на JSON.")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)
        print(f"Записани книги в {filename}")


    def add_book(self, **kwargs):
        isbn = kwargs.get("ISBN")
        if not isbn:
            raise ValueError("ISBN е задължително поле.")
        self.books[isbn] = {
            "Title": kwargs.get("Title", ""),
            "Author_s": kwargs.get("Author_s", []),
            "Publication_Year": kwargs.get("Publication_Year", None),
            "Publisher": kwargs.get("Publisher", ""),
            "Genre": kwargs.get("Genre", ""),
            "Page_Count": kwargs.get("Page_Count", 0),
            "Format": kwargs.get("Format", ""),
            "Price": kwargs.get("Price", 0.0),
            "Purchase_Date": kwargs.get("Purchase_Date", ""),
            "Personal_Rating": kwargs.get("Personal_Rating", None),
            "Read_Status": kwargs.get("Read_Status", "unread"),
            "Tags_Notes": kwargs.get("Tags_Notes", "")
        }

    def list_books(self):
        if not self.books:
            print("Библиотеката е празна.")
            return

        for isbn, book in self.books.items():
            print(f"Title: {book['Title']}")
            print(f"Author(s): {', '.join(book['Author_s'])}")
            print(f"ISBN: {isbn}")
            print(f"Year: {book['Publication_Year']}")
            print(f"Publisher: {book['Publisher']}")
            print(f"Genre: {book['Genre']}")
            print(f"Pages: {book['Page_Count']}")
            print(f"Format: {book['Format']}")
            print(f"Price: {book['Price']} лв")
            print(f"Purchase Date: {book['Purchase_Date']}")
            print(f"Rating: {book['Personal_Rating']}/5")
            print(f"Status: {book['Read_Status']}")
            print(f"Notes: {book['Tags_Notes']}")
            print("—" * 40)

    def find_book(self, isbn):
        return self.books.get(isbn, None)
    
    # проверка дали книгата вече съществува в библиотеката
    def find_book_by_title(self, title):
        title = title.lower()
        for isbn, book in self.books.items():
            if book["Title"].lower() == title:
                return book
        return None


    def edit_book(self, isbn, **kwargs):
        if isbn not in self.books:
            print(f"Няма книга с ISBN: {isbn}")
            return

        for key, value in kwargs.items():
            if key in self.books[isbn]:
                self.books[isbn][key] = value
                print(f"Обновено: {key} → {value}")
            else:
                print(f"Полето '{key}' не съществува.")

    def remove_book(self, isbn):
            if isbn in self.books:
                confirm = input(f"Сигурни ли сте, че искате да изтриете книгата с ISBN {isbn}? (y/n): ")
                if confirm.lower() == "y":
                    del self.books[isbn]
                    print("Книгата беше изтрита.")
                else:
                    print("Операцията беше отменена.")
            else:
                print("Няма такава книга.")

    # търсене 
    def search_books(self, query):
        query = query.lower()
        results = []
        for isbn, book in self.books.items():
            if (
                query in book["Title"].lower()
                or any(query in author.lower() for author in book["Author_s"])
                or query in isbn.lower()
            ):
                results.append((isbn, book))
        return results


    # разширено филтриране по жанр, статус, година, рейтинг, тагове
    def filter_books(self, genres=None, status=None, year_range=None, rating_range=None, tags=None):
        results = []
        for isbn, book in self.books.items():
            if genres and book["Genre"] not in genres:
                continue
            if status and book["Read_Status"].lower() != status.lower():
                continue
            if year_range:
                year = book["Publication_Year"]
                if not (year_range[0] <= year <= year_range[1]):
                    continue
            if rating_range:
                rating = book["Personal_Rating"]
                if rating is None or not (rating_range[0] <= rating <= rating_range[1]):
                    continue
            if tags:
                if not any(tag.lower() in book["Tags_Notes"].lower() for tag in tags):
                    continue
            results.append((isbn, book))
        return results
