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
        films_list = '\n'.join(f'    - {films_name}' for films_name in self.films_names) if self.films_names else '    - Ninguno'
        resident_list = '\n'.join(f'    - {residents_names}' for residents_names in self.residents_names) if self.residents_names else '    - Ninguno'

        return f'''
---------- {self.name} ----------
        
* Nombre: {self.name}
* Período orbital: {"Desconocido" if self.orbital_period == "unknown" else self.orbital_period}
* Período de rotación: {"Desconocido" if self.rotation_period == "unknown" else self.rotation_period}
* Población: {"Desconocida" if self.population == "unknown" else self.population}
* Clima: {"Desconocido" if self.climate == "unknown" else self.climate}
* Películas en las que aparece: 
{films_list}
* Residentes: 
{resident_list}
        '''