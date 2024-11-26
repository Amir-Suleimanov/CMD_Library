import json

def func_prefix(s: str) -> list:
    """
    Fills Pi-function array
    :param str: lookip string
    :return: result
    """
    l = len(s)
    P = [0]*l
    i, j = 0, 1
    while j < l :
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        # s[i] != s[j]:
        elif i:         # i > 0
            i = P[i - 1]
        else:           # i == 0
            P[j] = 0
            j += 1
    return P

def kmp(text: str, sub: str) -> list:
    sub_len = len(sub)
    text_len = len(text)
    if not text_len or sub_len > text_len:
        return []
    P = func_prefix(sub)
    entries = []
    i = j = 0
    while i < text_len and j < sub_len:
        if text[i] == sub[j]:
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        # text[i] 1= sub[j]
        elif j:     # j > 0
            j = P[j-1]
        else:
            i += 1
    return entries

class Book:
    def __init__(self: str, title: str, author: str, year: str, status: str='В наличии'):
        self.title: str = title
        self.author: str = author
        self.year: str = year
        self.status: str = status

        with open('library.json', 'r') as books:
            book_data = json.load(books)
            self.id = book_data['books_count'] + 1
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
    
    def add_book(title, author, year, status='В наличии'):
        new_book = Book(title, author, year, status)
        
        with open('library.json', 'r', encoding='utf-8') as books:
            book_data = json.load(books)
        
        book_data['books'].append(new_book.to_dict())
        books_count = book_data['books_count'] + 1

        json_books = {
            "books_count": books_count,
            "books": book_data['books']
        }

        with open('library.json', 'w', encoding='utf-8') as books:
            json.dump(json_books, books, indent=4, ensure_ascii=False)
        
        print("\nКнига была успешно создана")

    def delete_book(id: int):
        with open('library.json', 'r', encoding='utf-8') as books:
            book_data = json.load(books)
            books_count = book_data['books_count']
            books: list = book_data['books']
        for i in books:
            if i['id'] == id:
                books.remove(i)
                json_books = {
                    'books_count': books_count,
                    'books': books
                    }
                with open('library.json', 'w', encoding='utf-8') as books:
                    json.dump(json_books, books, indent=4, ensure_ascii=False)
                print("\nКнига была успешно удалена")
                return
        print("Такой книги нет")
        
    def search_book(search_title: str = None, search_author: str = None, search_year: int = None):
        with open('library.json', 'r', encoding='utf-8') as books:
            book_data = json.load(books)
            books = book_data['books']
        right_books = []

        if search_title != None:
            for i in books:
                if kmp(i['title'], search_title):
                    right_books.append(i)

        if search_author != None:
            for i in books:
                if kmp(i['author'], search_author):
                    right_books.append(i)

        if search_year != None:
            for i in books:
                if kmp(i['year'], search_year):
                    right_books.append(i)
        if not right_books:
            return "\nТаких книг нет в библиотеке"
        else:
            print("Список найденных книг: ")
            return right_books

    def get_all_books():
        with open('library.json', 'r', encoding='utf-8') as books:
            book_data = json.load(books)
            books = book_data['books']
        for i in books:
            print(f"ID: {i['id']}, Название: {i['title']}, Автор: {i['author']}, Год издания: {i['year']}, Статус: {i['status']}")
        
    def take_book(title):
        with open('library.json', 'r', encoding='utf-8') as books:
            book_data = json.load(books)
            books = book_data['books']
            books_count = book_data['books_count']
        
        for i in books:
            if i['title'] == title:
                if i['status'] == 'В наличии':
                    i['status'] = 'Выдана'
                    json_books = {
                        "books_count": books_count,
                        "books": books
                    }
                    with open('library.json', 'w', encoding='utf-8') as books:
                        json.dump(json_books, books, indent=4, ensure_ascii=False)
                    
                    print(f"\nКнига '{title}' была успешно выдана")
                    return True
                else:
                    print(f"\nКниги '{title}' нет в наличии")
                    return False
        print(f"\nКнига '{title}' не найдена в библиотеке")
        return False
    
    def return_book(title):
        with open('library.json', 'r', encoding='utf-8') as books:
            book_data = json.load(books)
            books = book_data['books']
            books_count = book_data['books_count']
        
        for i in books:
            if i['title'] == title:
                if i['status'] == 'Выдана':
                    i['status'] = 'В наличии'
                    json_books = {
                        "books_count": books_count,
                        "books": books
                    }
                    with open('library.json', 'w', encoding='utf-8') as books:
                        json.dump(json_books, books, indent=4, ensure_ascii=False)
                    
                    print(f"\nКнига '{title}' была успешно возвращена")
                    return True
                else:
                    print(f"\nКнига '{title}' уже была в наличии")
                    return False