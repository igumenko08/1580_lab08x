import json



class Book:
    _counter = 0

    def __init__(self, title, author, year, isbn, genre, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.pages = pages
        Book._counter += 1
        self._id = Book._counter
        print(f"ID {self._id} для книги {self.title} успешно создан")



    @property
    def book_id(self):
        return self._id

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not (isinstance(value, str)) or len(value.strip()) == 0:
            raise ValueError('Название книги должно быть непустой строкой')
        self.__title = value.strip()
    
                                                                            
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, str) or len(value.strip().split()) != 2:
            raise ValueError('Вы не ввели фамилию и имя автора или ввели с ошибкой')
        self.__author= value
    
    
    @property
    def year(self):
        return self.__year
    

    @year.setter
    def year(self, value):
        if not (isinstance(value, (int, float))) or not(1450 <= value <= 2026):
            raise ValueError('Год должен быть положительным целым числом от 1450 до 2026')
        self.__year= value
    

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str) or '-' not in value or len(value)!=17 or len(value.strip().split('-')) != 5 or len(value.strip().split('-')[0]) != 3:
            raise ValueError('ISBN неверный (в начале должно быть 3 цифры, всего 13 цифр, 5 блоков разделенных "-" )')
        self.__isbn= value.strip()

    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, value):
        if not (isinstance(value, str)) or len(value.strip()) == 0:
            raise ValueError('Жанр не должен быть пустой строкой')
        self.__genre= value.strip()
    
    @property
    def pages(self):
        return self.__pages
    
    @pages.setter
    def pages(self, value):
        if not (isinstance(value, (int, float))) or value <= 0:
            raise ValueError('Кол-во страниц должно быть положительным числом')
        self.__pages= value


    def __str__(self):
        return f"Книга (ID: {self.book_id}), название: {self.title}, автор: {self.author}, год: {self.year}, ISBN: {self.isbn}, жанр: {self.genre}, стр: {self.pages}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.isbn}', '{self.genre}', {self.pages})"

    def __copy__(self):
        new_book = Book(self.title, self.author, self.year, self.isbn, self.genre, self.pages)
        return new_book
    

    def __del__(self):
        print(f"Удаление ID {self._id} для книги {self.title}")


    def __lt__(self, other):
        return self.year < other.year
    
    
    def __eq__(self, other):
        return self.title.lower() == other.title.lower()
    
    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn,
            'genre': self.genre,
            'pages': self.pages
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            isbn=data['isbn'],
            genre=data['genre'],
            pages=data['pages']
        )


    @classmethod
    def save(cls, books_list, filename):
        data = [book.to_dict() for book in books_list]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print('Книги успешно сохранены')

    
    @classmethod
    def read(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                temp = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return print('Файл отсутствует или он пустой')
        data = []
        for tempik in temp:
            book = cls.from_dict(tempik)
            data.append(book)
        print(f'Загружено {len(data)} книг')
        return data

