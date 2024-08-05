import requests
from typing import List

class Swapi:
    def __init__(self):
        self.endpoints = {
            "films": "https://swapi.dev/api/films/",
            "people": "https://swapi.dev/api/people/",
            "planets": "https://swapi.dev/api/planets/",
            "species": "https://swapi.dev/api/species/",
            "starships": "https://swapi.dev/api/starships/",
            "vehicles": "https://swapi.dev/api/vehicles/"
        }
        self.factories = {
            "films": "movie.Movie",
            "people": "person.Person",
            "planets": "planet.Planet",
            "species": "species.Species",
            "starships": "starship.Starship",
            "vehicles": "vehicle.Vehicle"
        }

    def data(self, endpoint):
        response = requests.get(self.endpoints[endpoint])
        return response.json()["results"]

    def get_data(self, endpoint, id=None):
        if id:
            url = f"{self.endpoints[endpoint]}{id}/"
            response = requests.get(url)
            return response.json()
        else:
            data = self.data(endpoint)
            module_name, class_name = self.factories[endpoint].rsplit('.', 1)
            module = __import__(module_name)
            factory = getattr(module, class_name)
            if endpoint == "people":
                return [factory(item, self) for item in data]
            else:
                return [factory(item) for item in data]