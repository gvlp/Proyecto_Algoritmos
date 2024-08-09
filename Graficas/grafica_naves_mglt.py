import pandas as pd
from matplotlib import pyplot as plt
import random
data = pd.read_csv('starwars/csv/starships.csv')

def mostrar_grafica_naves_MGLT():
    starships = data['name']
    lenghs = data['MGLT']
    labels_num = len(starships)
    #Para definir los colores de cada barra
    def gen_random_colors():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02X}{g:02X}{b:02X}"
    elements_number = len(starships)
    colors = [gen_random_colors() for _ in range(elements_number)]

    plt.bar(starships,lenghs,color=colors)
    plt.xlabel('Naves')
    plt.ylabel('MGLT')
    plt.title('Comparacion de MGLT de cada nave')
    plt.xticks(rotation=90)
    #plt.xlim(-0.5, len(starships)-0.5)
    plt.tick_params(axis='x',which='major',labelsize=7)
