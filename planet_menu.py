import json

from planet import Planet

planets = []


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
    if not planets:
        print("Нет записей")
    else:
        for planet in planets:
            print(planet)


def add_planet():
    try:
        name = input('Введите название планеты: ')
        radius = int(input('Введите радиус планеты: '))
        massa = int(input('Введите массу планеты: '))
        distance = int(input('Введите расстояние планеты от солнца: '))
        type_planet = input(f'Введите один из типов планеты {Planet.variants_types}: ')

        planet = Planet(name, radius, massa, distance, type_planet)
        planets.append(planet)
        print(f'Планета {name} успешно добавлена')
    except ValueError:
        raise ValueError('Радиус, масса и дистанция должны быть положительными целыми числами')


def search(parametr):
        naideno = False
        if parametr == 1:
            user_name = input('Введите название планеты:')
            for planet in planets:
                if user_name.lower() == planet.name.lower():
                    print(planet)
                    naideno = True
            if not naideno:
                print('Планета не найдена')

        elif parametr == 2:
            user_massa = int(input('Введите массу планеты:'))
            for planet in planets:
                if user_massa == planet.massa:
                    print(planet)
                    naideno = True
            if not naideno:
                print('Планета не найдена')        

        elif parametr == 3:
            user_radius = int(input('Введите радиус планеты:'))
            for planet in planets:
                if user_radius == planet.radius:
                    print(planet)
                    naideno = True
            if not naideno:
                print('Планета не найдена')      

        elif parametr == 4:
            user_distance = int(input('Введите расстояние планеты от солнца:'))
            for planet in planets:
                if user_distance == planet.distance:
                    print(planet)
                    naideno = True
            if not naideno:
                print('Планета не найдена')

        elif parametr == 5:
            user_type_planet = input(f'Введите тип планеты {Planet.variants_types}:')
            for planet in planets:
                if user_type_planet.lower() == planet.type_planet.lower():
                    print(planet)
                    naideno = True
            if not naideno:
                print('Планета не найдена')  
        else:
            print('Неверный выбор')            


def edit_planet():
    if planets:
        print_all()
        user_id = int(input('Введите ID планеты, которую вы хотите изменить: '))

        if 1 <= user_id <= len(planets):
            print(planets[user_id-1])
            print('Введите по какому параметру вы хотите изменить запись')
            print('1.По названию')
            print('2.По массе')
            print('3.По радиусу')
            print('4.По расстоянию от солнца')
            print('5.По типу')
            editing = planets[user_id-1]

            parametr = int(input())

            if parametr == 1:
                user_name = input('Введите новое название планеты: ')
                editing.name = user_name
                print('Успешное изменение')
            elif parametr == 2:
                user_massa = int(input('Введите новую массу планеты: '))
                editing.massa = user_massa
                print('Успешное изменение')
            elif parametr == 3:
                user_radius = int(input('Введите новый радиус планеты: '))
                editing.radius = user_radius
                print('Успешное изменение')
            elif parametr == 4:
                user_distance = int(input('Введите новую дистанцию планеты от солнца: '))
                editing.distance = user_distance
                print('Успешное изменение')
            elif parametr == 5:
                user_type_planet = input(f'Выберите новый тип планеты из {Planet.variants_types}: ')
                editing.type_planet = user_type_planet
                print('Успешное изменение')
        else:
            print('Несуществующий параметр')
    else:
        print('Записей нет. Планета не может быть изменена') 


def delete_planet():
    if planets:
        print_all()
        user_id = int(input('Введите ID планеты, которую вы хотите удалить: '))
        if 1 <= user_id <= len(planets):
            del planets[user_id-1]
            print(f'Планета с ID {user_id} успешно удалена')
        else:
            print('Несуществующий ID')
    else:
        print('Записей нет. Планета не может быть удалена') 


def bubble_sort(unsorted):
    if planets:
        print('Введите по какому параметру вы хотите найти сортировать планеты: ')
        print('1.По названию')
        print('2.По массе')
        print('3.По радиусу')
        print('4.По расстоянию от солнца')
        print('5.По типу')
        user_parametr = int(input())
        if user_parametr == 1:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].name.lower() > unsorted[j+1].name.lower():
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 2:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].massa > unsorted[j+1].massa:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 3:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].radius > unsorted[j+1].radius:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 4:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].distance > unsorted[j+1].distance:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        
        elif user_parametr == 5:
            length = len(unsorted)
            for i in range (length):
                for j in range (length-1-i):
                    if unsorted[j].type_planet > unsorted[j+1].type_planet:
                        unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            return unsorted
        else:
            print('Неверный ввод')
    else:
        print('Записей нет. Планеты не могут быть отсортированы') 
        

menu()
user_input = int(input())

while user_input != 9:
    if user_input == 1:
        filename = input('Введите название файла: ')
        filename += '.json'
        loaded = Planet.read(filename)
        if loaded:
            print(f'Успешно загружено {len(loaded)} планет')
            planets.extend(loaded)

    elif user_input == 2:
        filename = input('Введите название файла: ')
        filename += '.json'
        Planet.save(planets, filename)

    elif user_input == 3:
        print_all()

    elif user_input == 4:
        add_planet()

    elif user_input == 5:
        if planets:
            print('Введите по какому параметру вы хотите найти запись: ')
            print('1.По названию')
            print('2.По массе')
            print('3.По радиусу')
            print('4.По расстоянию от солнца')
            print('5.По типу')
            parametr = int(input())
            search(parametr)
        else:
            print('Записей нет. Планета не может быть найдена') 

    elif user_input == 6:
        edit_planet()

    elif user_input == 7:
        delete_planet()
    
    elif user_input == 8:
        bubble_sort(planets)
        print('Успешная сортировка')
        print_all()

    menu()
    user_input = int(input())

print('Программа завершена')