import json

from books import Book

books = []


def menu():
    print('Выберете действие:')
    print('1.Загрузка БД из файла')
    print('2.Сохранение БД в файл')
    print('3.Просмотр всех записей')
    print('4.Добавление новой записи')
    print('5.Поиск записи')
    print('6.Редактирование записи')
    print('7.Удаление записи')
    print('8.Сортировка')
    print('9.Выход')

def print_all():
    if not books:
        print("Нет записей")
    else:
        for book in books:
            print(book)


def add_book():
    try:
        title = input('Введите название книги: ')
        author = input('Введите автора (Фамилия Имя): ')
        year = int(input('Введите год издания: '))
        isbn = input('Введите ISBN: ')
        genre = input('Введите жанр: ')
        pages = int(input('Введите количество страниц: '))

        book = Book(title, author, year, isbn, genre, pages)
        books.append(book) 
        print(f'Книга {title} успешно добавлена')
    except ValueError:
        raise ValueError('Год и кол-во страниц должны быть положительными числами')


def search(parametr):
        naideno = False
        if parametr == 1:
            user_title = input('Введите название книги:')
            for book in books:
                if user_title.lower() == book.title.lower():
                    print(book)
                    naideno = True
            if not naideno:
                print('Книга не найдена')

        elif parametr == 2:
            user_author = input('Введите автора книги:')
            for book in books:
                if user_author.lower() == book.author.lower():
                    print(book)
                    naideno = True
            if not naideno:
                print('Книга не найдена')        

        elif parametr == 3:
            user_year = int(input('Введите год издания книги:'))
            for book in books:
                if user_year == book.year:
                    print(book)
                    naideno = True
            if not naideno:
                print('Книга не найдена')      

        elif parametr == 4:
            user_isbn = input('Введите ISBN книги:')
            for book in books:
                if user_isbn == book.isbn:
                    print(book)
                    naideno = True
            if not naideno:
                print('Книга не найдена')

        elif parametr == 5:
            user_genre = input('Введите жанр книги:')
            for book in books:
                if user_genre.lower() == book.genre.lower():
                    print(book)
                    naideno = True
            if not naideno:
                print('Книга не найдена')  
        elif parametr == 6:
            user_pages = int(input('Введите кол-во страниц в книге:'))
            for book in books:
                if user_pages == book.pages:
                    print(book)
                    naideno = True
            if not naideno:
                print('Книга не найдена')      

        else:
            print('Неверный выбор')           

def edit_book():
    if books:
        print_all()
        user_id = int(input('Введите ID книги, которую вы хотите изменить: '))
        if 1 <= user_id <= len(books):
                print(books[user_id-1])
                print('Введите по какому параметру вы хотите изменить запись')
                print('1.По названию')
                print('2.По автору')
                print('3.По году')
                print('4.По ISBN')
                print('5.По жанру')
                print('6.По количеству страниц')
                editing = books[user_id-1]

                parametr = int(input())

                if parametr == 1:
                    user_title = input('Введите новое название книги: ')
                    editing.title = user_title
                    print('Успешное изменение')
                elif parametr == 2:
                    user_author = input('Введите нового автора книги: ')
                    editing.author = user_author
                    print('Успешное изменение')
                elif parametr == 3:
                    user_year = int(input('Введите новый год издания: '))
                    editing.year = user_year
                    print('Успешное изменение')
                elif parametr == 4:
                    user_isbn = input('Введите новый ISBN: ')
                    editing.isbn = user_isbn
                    print('Успешное изменение')
                elif parametr == 5:
                    user_genre = input('Введите новый жанр: ')
                    editing.genre = user_genre
                    print('Успешное изменение')
                elif parametr == 6:
                    user_pages = int(input('Введите новое количество страниц: '))
                    editing.pages = user_pages
                    print('Успешное изменение')
        else:
            print('Несуществующий параметр')
    else:
        print('Записей нет. Книга не может быть изменена') 


def delete_book():
    if books:
        print_all()
        user_id = int(input('Введите ID книги, которую вы хотите удалить: '))
        if 1 <= user_id <= len(books):
            del books[user_id-1]
            print(f'Книга с ID {user_id} успешно удалена')
        else:
            print('Несуществующий ID')
    else:
        print('Записей нет. Книга не может быть удалена')


def bubble_sort(unsorted):
    if books:
        print('Введите по какому параметру вы хотите сортировать книги: ')
        print('1.По названию')
        print('2.По автору')
        print('3.По году')
        print('4.По ISBN')
        print('5.По жанру')
        print('6.По количеству страниц')
        user_parametr = int(input())
        if user_parametr == 1:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].title.lower() > unsorted[j+1].title.lower():
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 2:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].author.lower() > unsorted[j+1].author.lower():
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 3:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].year > unsorted[j+1].year:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 4:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].isbn > unsorted[j+1].isbn:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 5:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].genre.lower() > unsorted[j+1].genre.lower():
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 6:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].pages > unsorted[j+1].pages:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        else:
            print('Неверный ввод')
    else:
        print('Записей нет. Книги не могут быть отсортированы') 
        

menu()
user_input = int(input())

while user_input != 9:
    if user_input == 1:
        filename = input('Введите название файла: ')
        filename += '.json'
        loaded = Book.read(filename)
        if loaded:
            print(f'Успешно загружено {len(loaded)} книг')
            books.extend(loaded)

    elif user_input == 2:
        filename = input('Введите название файла: ')
        filename += '.json'
        Book.save(books, filename)

    elif user_input == 3:
        print_all()

    elif user_input == 4:
        add_book()

    elif user_input == 5:
        if books:
            print('1.По названию')
            print('2.По автору')
            print('3.По году')
            print('4.По ISBN')
            print('5.По жанру')
            print('6.По количеству страниц')
            parametr = int(input())
            search(parametr)
        else:
            print('Записей нет. Книга не может быть найдена') 

    elif user_input == 6:
        edit_book()

    elif user_input == 7:
        delete_book()
    
    elif user_input == 8:
        bubble_sort(books)
        if books:
            print('Успешная сортировка')
            print_all()
    else:
        print('Неверный выбор')
    menu()
    user_input = int(input())

print('Программа завершена')