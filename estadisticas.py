import pandas as pd
from statistics import mode

df = pd.read_csv('starwars/csv/sorted_starships.csv') 

#Para hiperimpulsores
hiperimpulsores_estad = df.groupby('starship_class')['hyperdrive_rating'].agg(['mean', mode ,'max', 'min'])
hiperimpulsores_estad.to_csv('result_estad_hiperimpulsores.csv')

#Para MGLT
MGLT_estad = df.groupby('starship_class')['MGLT'].agg(['mean', mode ,'max', 'min'])
MGLT_estad.to_csv('result_estad_MGLT.csv')

#Para velocidad máxima en atmósfera 
veloc_max_atm_estad = df.groupby('starship_class')['max_atmosphering_speed'].agg(['mean', mode ,'max', 'min'])
veloc_max_atm_estad.to_csv('result_estad_veloc_max_atm.csv')

#Para el costo en créditos
costo_en_cred_estad = df.groupby('starship_class')['cost_in_credits'].agg(['mean', mode ,'max', 'min'])
costo_en_cred_estad.to_csv('result_estad_costo_por_cred.csv')



