import requests

class Species:
    def __init__(self, data):
        self.data = data
        self.get_homeworld_name()
        self.get_characters_names()
        self.get_episodes_names()

    @property
    def name(self):
        return self.data['name']

    def get_homeworld_name(self):
        if 'homeworld' in self.data and self.data['homeworld'] is not None:
            homeworld_url = self.data['homeworld']
            response = requests.get(homeworld_url)
            self.homeworld_name = response.json()['name']
        else:
            self.homeworld_name = 'Desconocido'

    def get_characters_names(self):
        self.characters_names = []
        if 'people' in self.data and self.data['people'] is not None:
            for person_url in self.data['people']:
                response = requests.get(person_url)
                self.characters_names.append(response.json()['name'])

    def get_episodes_names(self):
        self.episodes_names = []
        if 'films' in self.data and self.data['films'] is not None:
            for film_url in self.data['films']:
                response = requests.get(film_url)
                self.episodes_names.append(response.json()['title'])

    def __str__(self):
        characters_list = '\n'.join(f'    - {character_name}' for character_name in self.characters_names)
        episodes_list = '\n'.join(f'    - {episode_name}' for episode_name in self.episodes_names)

        return f'''
---------- {self.name} ----------
        
* Nombre: {self.name}
* Planeta de origen: {self.homeworld_name}
* Personajes:
{characters_list}
* Episodios:
{episodes_list}
'''