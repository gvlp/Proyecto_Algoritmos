import requests # type: ignore

# CLASE SWAPI

class swapi:
    def __init__(self):
        self.endpoints = {
            "films": "https://swapi.dev/api/films/",
            "people": "https://swapi.dev/api/people/",
            "planets": "https://swapi.dev/api/planets/",
            "species": "https://swapi.dev/api/species/",
            "starships": "https://swapi.dev/api/starships/",
            "vehicles": "https://swapi.dev/api/vehicles/"
        }

def data(self, endpoint):
    response = requests.get(self.endpoints[endpoint])
    return response.json()["results"]

def get_movies(self):
    return [Movie(movie_data) for movie_data in self.data("films")]

def get_people(self):
    return [Person(person_data) for person_data in self.data("people")]

def get_planets(self):
    return [Planet(planet_data) for planet_data in self.data("planets")]

def get_characters(self):
    return [Character(character_data, self) for character_data in self.data("people")]

def get_starships(self):
    return [Starship(starship_data) for starship_data in self.data("starships")]

def get_vehicles(self):
    return [Vehicle(vehicle_data) for vehicle_data in self.data("vehicles")]

# CLASE PELICULAS:

class Movie:
    def __init__(self, movie_data):
        self.title = movie_data["title"]
        self.episode_id = movie_data["episode_id"]
        self.release_date = movie_data["release_date"]
        self.opening_crawl = movie_data["opening_crawl"]
        self.director = movie_data["director"]

        def __str__(self):
            return f'''
        Título: {self.title}
        Número de Episodio: {self.episode_id}
        Fecha de Lanzamiento: {self.release_date}
        Texto al inicio de la película (Opening Crawl): {self.opening_crawl}
        Nombre del Director: {self.director}
        
        '''

# CLASE SERES VIVOS:

class Person:
    def __init__(self, person_data, swapi):
        self.name = person_data["name"]
        self.height = person_data["height"]
        self.species = person_data["species"]
        self.homeworld = person_data["homeworld"]
        self.language = self.get_language(swapi)
        self.species_name = self.get_species_name(swapi)
        self.species_characters = self.get_species_characters(swapi)
        self.films_names = self.get_films_names(swapi)

    def get_language(self, swapi):
        homeworld_data = swapi.data("planets")
        for planet in homeworld_data:
            if planet["url"] == self.homeworld:
                return planet["languages"][0]
        return "No es posible identificarlo"

    def get_species_name(self, swapi):
        species_data = swapi.data("species")
        for species in species_data:
            if species["url"] == self.species:
                return species["name"]
        return "No es posible identificarlo"

    def get_species_characters(self, swapi):
        people_data = swapi.data("people")
        characters = []
        for person in people_data:
            if person["species"] == self.species:
                characters.append(person["name"])
        return ", ".join(characters)
    
    def get_films_names(self, swapi):
        films_data = swapi.data("films")
        films_names = []
        for film in films_data:
            for film_url in self.films:
                if film["url"] == film_url:
                    films_names.append(film["title"])
        return ", ".join(films_names)

    def __str__(self):
        return f'''
        Nombre: {self.name}
        Altura: {self.height}
        Clasificación de la Especie: {self.species_name}
        Nombre del planeta de origen: {self.get_homeworld_name(swapi)}
        Lengua materna: {self.language}
        Nombre de los personajes que pertenecen a la especie: {self.species_characters}
        Nombre de los episodios en los que aparecen: {self.films_names}

        '''

# CLASE PLANETAS:

class Planet:
    def __init__(self, planet_data, swapi):
        self.name = planet_data["name"]
        self.orbital_period = planet_data["orbital_period"]
        self.rotation_period = planet_data["rotation_period"]
        self.population = planet_data["population"]
        self.climate = planet_data["climate"]
        self.films = planet_data["films"]
        self.residents = planet_data["residents"]
        self.films_names = self.get_films_names(swapi)
        self.residents_names = self.get_residents_names(swapi)

    def get_films_names(self, swapi):
        films_data = swapi.data("films")
        films_names = []
        for film in films_data:
            for film_url in self.films:
                if film["url"] == film_url:
                    films_names.append(film["title"])
        return ", ".join(films_names)

    def get_residents_names(self, swapi):
        people_data = swapi.data("people")
        residents_names = []
        for person in people_data:
            for resident_url in self.residents:
                if person["url"] == resident_url:
                    residents_names.append(person["name"])
        return ", ".join(residents_names)

    def __str__(self):
        return f'''
        Nombre: {self.name}
        Período orbital: {self.orbital_period}
        Período de rotación: {self.rotation_period}
        Cantidad de Habitantes: {self.population}
        Tipo de Clima: {self.climate}
        Episodios en los que aparece: {self.films_names}
        Personajes originarios del planeta: {self.residents_names}

        '''

# CLASE PERSONAJES:

class Character:
    def __init__(self, character_data, swapi):
        self.name = character_data["name"]
        self.homeworld = character_data["homeworld"]
        self.films = character_data["films"]
        self.gender = character_data["gender"]
        self.species = character_data["species"]
        self.starships = character_data["starships"]
        self.vehicles = character_data["vehicles"]
        self.homeworld_name = self.get_homeworld_name(swapi)
        self.films_names = self.get_films_names(swapi)
        self.species_name = self.get_species_name(swapi)
        self.starships_names = self.get_starships_names(swapi)
        self.vehicles_names = self.get_vehicles_names(swapi)

    def get_homeworld_name(self, swapi):
        planet_data = swapi.data("planets")
        for planet in planet_data:
            if planet["url"] == self.homeworld:
                return planet["name"]
        return "Desconocido"

    def get_films_names(self, swapi):
        films_data = swapi.data("films")
        films_names = []
        for film in films_data:
            for film_url in self.films:
                if film["url"] == film_url:
                    films_names.append(film["title"])
        return ", ".join(films_names)

    def get_species_name(self, swapi):
        species_data = swapi.data("species")
        for species in species_data:
            if species["url"] == self.species:
                return species["name"]
        return "Desconocido"

    def get_starships_names(self, swapi):
        starships_data = swapi.data("starships")
        starships_names = []
        for starship in starships_data:
            for starship_url in self.starships:
                if starship["url"] == starship_url:
                    starships_names.append(starship["name"])
        return ", ".join(starships_names)

    def get_vehicles_names(self, swapi):
        vehicles_data = swapi.data("vehicles")
        vehicles_names = []
        for vehicle in vehicles_data:
            for vehicle_url in self.vehicles:
                if vehicle["url"] == vehicle_url:
                    vehicles_names.append(vehicle["name"])
        return ", ".join(vehicles_names)

    def __str__(self):
        return f'''
        a. Nombre: {self.name}
        b. Nombre del Planeta de origen: {self.homeworld_name}
        c. Títulos de los episodios en los que interviene: {self.films_names}
        d. Género: {self.gender}
        e. Especie: {self.species_name}
        f. Nombre de las naves que utiliza: {self.starships_names}
        g. Nombre de los vehículos que utiliza: {self.vehicles_names}

        '''

# CLASE NAVES:

class Starship:
    def __init__(self, starship_data):
        self.name = starship_data["name"]
        self.model = starship_data["model"]
        self.manufacturer = starship_data["manufacturer"]
        self.cost_in_credits = starship_data["cost_in_credits"]
        self.length = starship_data["length"]
        self.max_atmosphering_speed = starship_data["max_atmosphering_speed"]
        self.crew = starship_data["crew"]
        self.passengers = starship_data["passengers"]

# CLASE VEHÍCULOS:

class Vehicle:
    def __init__(self, vehicle_data):
        self.name = vehicle_data["name"]
        self.model = vehicle_data["model"]
        self.manufacturer = vehicle_data["manufacturer"]
        self.cost_in_credits = vehicle_data["cost_in_credits"]
        self.length = vehicle_data["length"]
        self.max_atmosphering_speed = vehicle_data["max_atmosphering_speed"]
        self.crew = vehicle_data["crew"]
        self.passengers = vehicle_data["passengers"]
