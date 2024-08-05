from swapi_api import Swapi

class Planet:
    def __init__(self, data):
        self.name = data["name"]
        self.orbital_period = data["orbital_period"]
        self.rotation_period = data["rotation_period"]
        self.population = data["population"]
        self.climate = data["climate"]
        self.films = data["films"]
        self.residents = data["residents"]
        self.films_names = self.get_films_names()
        self.residents_names = self.get_residents_names()

    def get_films_names(self):
       
        swapi = Swapi()
        films_names = []
        for film_url in self.films:
            film_id = film_url.split("/")[-2]
            film_data = swapi.get_data("films", film_id)
            films_names.append(film_data["title"])
        return films_names

    def get_residents_names(self):
    
        swapi = Swapi()
        residents_names = []
        for resident_url in self.residents:
            resident_id = resident_url.split("/")[-2]
            resident_data = swapi.get_data("people", resident_id)
            residents_names.append(resident_data["name"])
        return residents_names

    def __str__(self):
        return f'''
        --- Planeta ---
        
        * Nombre: {self.name}
        * Periodo orbital: {self.orbital_period}
        * Periodo de rotación: {self.rotation_period}
        * Población: {self.population}
        * Clima: {self.climate}
        * Películas en las que aparece: {self.films_names}
        * Residentes: {self.residents_names}

        '''