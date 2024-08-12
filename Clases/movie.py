import textwrap

class Movie:

    def __init__(self, movie_data):
        self.title = movie_data["title"]
        self.episode_id = movie_data["episode_id"]
        self.release_date = movie_data["release_date"]
        self.opening_crawl = movie_data["opening_crawl"]
        self.director = movie_data["director"]

    def __str__(self):

        opening_crawl = textwrap.dedent(self.opening_crawl).strip()
        wrapped_crawl = textwrap.fill(opening_crawl, width=80)

        return f'''

---------- {self.title} ----------

* Título: {self.title}
* Número de Episodio: {self.episode_id}
* Fecha de Lanzamiento: {self.release_date}
* Nombre del Director: {self.director}
* Texto al inicio de la película (Opening Crawl): 

{self.opening_crawl}
 '''

    def get_full_opening_crawl(self):
        return self.opening_crawl