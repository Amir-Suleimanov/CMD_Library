from models import Book

while True:
    print("\nСистема управления библиотекой")
    print("1. Создать книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Список всех книг")
    print("5. Взять/вернуть книгу")
    
    choice = input("\nВведите действие: ")

    if choice == "1":
        title = input("Название книги: ")
        author = input("Автор: ")
        year = -1
        while year == -1:
            try: 
                year = int(input("Год издания: "))
            except ValueError:
                print("Некорректный ввод года. Пожалуйста, введите число.")
        
        Book.add_book(title, author, year)
        
    elif choice == "2":
        id = -1
        id = int(input("\nВведите ID книги для удаления: "))
        while id == -1:
            id = int(input("Некорректный ввод ID. Пожалуйста, введите число."))
        
        Book.delete_book(id)
            
    elif choice == "3":
        context = -1
        while context == -1:
            try:
                context = int(input('Выберите параметр по которому будете искать:\n1. Название\n2. Автор\n3. Год издания\n0. Отменить дейтвие\n\nДействие:'))
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

        if context == 1:
            title = input("Введите название книги для поиска: ").strip()
            
            found_books = Book.search_book(search_title=title)
            for i in found_books:
                print(f"ID: {i['id']}, Название: {i['title']}, Автор: {i['author']}, Год издания: {i['year']}, Статус: {i['status']}")
        elif context == 2:
            author = input("Введите автора книги для поиска: ").strip()
            
            found_books = Book.search_book(search_author=author)
            for i in found_books:
                print(f"ID: {i['id']}, Название: {i['title']}, Автор: {i['author']}, Год издания: {i['year']}, Статус: {i['status']}")

        elif context == 3:
            year = -1
            while year == -1:
                try: 
                    year = int(input("Введите год издания для поиска: "))
                except ValueError:
                    print("Некорректный ввод года. Пожалуйста, введите число.")
            found_books =  Book.search_book(search_year=year)
            for i in found_books:
                print(f"ID: {i['id']}, Название: {i['title']}, Автор: {i['author']}, Год издания: {i['year']}, Статус: {i['status']}")
        elif context == 0:
            print("Действие отменено.")
            continue
    
    elif choice == "4":
        print("Список всех книг:\n")
        Book.get_all_books()
        continue
    
    elif choice == "5":
        title = input("Введите название книги, которую вы хотите взять/вернуть: ").strip()
        user_action = input(
        '''
        Выберите действие:
        1. Взять
        2. Вернуть
        '''
        )
        
        if user_action == "1":
            Book.take_book(title)
        elif user_action == "2":
            Book.return_book(title)
        else:
            print("Некорректное действие.")