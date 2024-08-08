class Person:
    def __init__(self, data, swapi_api):
        self.name = data['name']
        self.homeworld_url = data['homeworld']
        self.films_urls = data['films']
        self.gender = data['gender']
        self.species_url = None
        if data['species']:
            self.species_url = data['species'][0]
        self.starships_urls = data['starships']
        self.vehicles_urls = data['vehicles']
        self.swapi_api = swapi_api
        self.data = data
        self.homeworld_name = None
        self.films_names = None
        self.species_name = None
        self.starships_names = None
        self.vehicles_names = None
        self.get_homeworld_info()
        self.get_films_info()
        self.get_species_info()
        self.get_starships_info()
        self.get_vehicles_info()

    def get_homeworld_info(self):
        homeworld_id = self.homeworld_url.split('/')[-2]
        homeworld_data = self.swapi_api.get_data('planets', homeworld_id)
        self.homeworld_name = homeworld_data['name']

    def get_films_info(self):
        films_ids = [film_url.split('/')[-2] for film_url in self.films_urls]
        films_data = [self.swapi_api.get_data('films', film_id) for film_id in films_ids]
        self.films_names = [film['title'] for film in films_data]

    def get_species_info(self):
        if self.species_url:
            species_id = self.species_url.split('/')[-2]
            species_data = self.swapi_api.get_data('species', species_id)
            self.species_name = species_data['name']
        else:
            self.species_name = 'Desconocida'

    def get_starships_info(self):
        starships_ids = [starship_url.split('/')[-2] for starship_url in self.starships_urls]
        starships_data = [self.swapi_api.get_data('starships', starship_id) for starship_id in starships_ids]
        self.starships_names = [starship['name'] for starship in starships_data]

    def get_vehicles_info(self):
        vehicles_ids = [vehicle_url.split('/')[-2] for vehicle_url in self.vehicles_urls]
        vehicles_data = [self.swapi_api.get_data('vehicles', vehicle_id) for vehicle_id in vehicles_ids]
        self.vehicles_names = [vehicle['name'] for vehicle in vehicles_data]

    def __str__(self):
        films_list = '\n'.join(f'    - {films_name}' for films_name in self.films_names) if self.films_names else '    - Ninguno'
        starship_list = '\n'.join(f'    - {starships_names}' for starships_names in self.starships_names) if self.starships_names else '    - Ninguna'
        vehicles_list = '\n'.join(f'    - {vehicles_names}' for vehicles_names in self.vehicles_names) if self.vehicles_names else '    - Ninguno'

        return f'''
---------- {self.name} ----------
        
* Nombre: {self.name}
* Nombre del Planeta de origen: {self.homeworld_name}
* Títulos de los episodios en los que interviene:
{films_list}
* Género: {self.gender}
* Especie: {self.species_name}
* Nombre de las naves que utiliza:
{starship_list}
* Nombre de los vehículos que utiliza:
{vehicles_list}
'''