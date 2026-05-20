import json



class Planet:
    _counter = 0
    variants_types = ["каменная", "газовый гигант", "ледяной гигант"]

    def __init__(self, name, radius, massa, distance, type_planet):
        self.name = name
        self.radius = radius    
        self.massa = massa 
        self.distance = distance 
        self.type_planet = type_planet
        Planet._counter += 1
        self._id = Planet._counter
        print(f"ID {self._id} для планеты {self.name} успешно создан")



    @property
    def planet_id(self):
        return self._id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not (isinstance(value, str)) or len(value.strip()) == 0:
            raise ValueError('Название планеты должно быть непустой строкой')
        self.__name = value.strip()
    

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if not (isinstance(value, (int, float))) or value <= 0:
            raise ValueError('Радиус должен быть положительным целым числом')
        self.__radius= value
    
    
    @property
    def massa(self):
        return self.__massa
    

    @massa.setter
    def massa(self, value):
        if not (isinstance(value, (int, float))) or value <= 0:
            raise ValueError('Масса должна быть положительным целым числом')
        self.__massa= value
    

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, value):
        if not (isinstance(value, (int, float))) or value <= 0:
            raise ValueError('Расстояние от Солнца должно быть положительным целым числом')
        self.__distance= value

    
    @property
    def type_planet(self):
        return self.__type_planet
    
    @type_planet.setter
    def type_planet(self, value):
        if not (isinstance(value, str)) or len(value.strip()) == 0:
            raise ValueError('Тип планеты должен быть непустой строкой')
        
        if value.strip() not in self.variants_types:
            raise ValueError(f"Тип планеты должен быть один из ниже перечисленных {self.variants_types}")
        self.__type_planet = value.strip()


    def __str__(self):
        return f"Планета (ID: {self.planet_id}): {self.name}, радиус: {self.radius}, масса: {self.massa}, расстояние от Солнца: {self.distance}, тип: {self.type_planet}"

    def __repr__(self):
        return (f"Planet(name='{self.name}', radius={self.radius}, "
                f"massa={self.massa}, distance={self.distance}, "
                f"type_planet='{self.type_planet}')")
    

    def __copy__(self):
        new_planet = Planet(self.name, self.radius, self.massa, self.distance, self.type_planet)
        return new_planet
    

    def __del__(self):
        print(f"Удаление ID {self._id}")


    def __lt__(self, other):
        return self.distance < other.distance
    
    
    def __eq__(self, other):
        return self.name.lower() == other.name.lower()
    
    def to_dict(self):
        return {
            'name': self.name,
            'radius' : self.radius,
            'massa': self.massa,
            'distance': self.distance,
            'type': self.type_planet
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data['name'],
            radius = data['radius'],
            massa = data['massa'],
            distance = data['distance'],
            type_planet = data['type'] 
        )



    @classmethod
    def save(cls, planets_list, filename):
        data = [planet.to_dict() for planet in planets_list]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print('Планеты успешно сохранены')

    
    @classmethod
    def read(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                temp = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return print('Файл отсутствует или он пустой')
        data = []
        for tempik in temp:
            planet = cls.from_dict(tempik)
            data.append(planet)
        return data

