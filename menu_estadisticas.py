import pandas as pd

def imprimir_resultados_hiperimpulsores():
    data_hiperimpulsores = pd.read_csv('result_estad_hiperimpulsores.csv')
    print(data_hiperimpulsores)

def imprimir_resultados_MGLT():
    data_MGLT = pd.read_csv('result_estad_MGLT.csv')
    print(data_MGLT)

def imprimir_resultados_veloc_max_atm():
    data_veloc_max_atm = pd.read_csv('result_estad_veloc_max_atm.csv')
    print(data_veloc_max_atm)

def imprimir_resultados_costo_por_credito():
    data_costo_por_cred = pd.read_csv('result_estad_costo_por_cred.csv')
    print(data_costo_por_cred)
       


def mostrar_menu_estadisticas():
    while True:
        print("\nSelecciona una opción:")
        print("1. Clasificación de hiperimpulsor")
        print("2. MGLT (Modern Galactic Light Time)")
        print("3. Velocidad maxima en atmosfera ")
        print("4. Costo por credito ")
        print("5. Regresar al menu principal")

        opcion = input("Seleccione una opción: ")
    
        if opcion == "1":
            imprimir_resultados_hiperimpulsores()
        elif opcion == "2":
            imprimir_resultados_MGLT()
        elif opcion == "3":
            imprimir_resultados_veloc_max_atm()
        elif opcion == "4":
            imprimir_resultados_costo_por_credito()
        elif opcion == "5":
            print('Regresando al menu principal')
            break
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")
            opcion = input("Seleccione una opción: ")

