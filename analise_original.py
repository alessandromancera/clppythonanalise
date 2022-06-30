import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from urllib.request import urlopen
from datetime import datetime
import json

plt.style.use('classic')
sb.set(rc={'figure.figsize':(15,8)})
#plt.rcParams["figure.figsize"] = (15,10)

#----------------------------------------------------------------------
# IMPORTA OS DADOS DAS ESTEIRAS EM UM DICT JSON
#----------------------------------------------------------------------
def Carrega_Esteira(num_esteira):
    url = "https://dry-plateau-13546.herokuapp.com/esteira/" + str(num_esteira)
    response = urlopen(url)

    dict_json = json.loads(response.read())
    return dict_json

#----------------------------------------------------------------------
# SALVA OS DADOS DO DICT JSON EM UM ARQUIVO JSON
#----------------------------------------------------------------------
def Salva_json(num_esteira,dict_1):
    n_json = "esteira_" + str(num_esteira) + ".json"
    s_json = json.dumps(dict_1)
    fjson = open(n_json, "w")
    fjson.write(s_json)
    fjson.close()
    json_pd = pd.read_json(n_json)
    #print("Arquivo json salvo")
    return json_pd
    
#----------------------------------------------------------------------
# SALVA O DICT JSON EM UM ARQUIVO CSV
#----------------------------------------------------------------------
def Salva_csv(num_esteira,json_pd):
    n_csv = "esteira_" + str(num_esteira) + ".csv"
    json_pd.to_csv(n_csv,index=None)
    #print("Arquivo csv salvo")
    
#----------------------------------------------------------------------
# ROTINA PRINCIPAL
#----------------------------------------------------------------------
num_esteira = 1
dict_json = Carrega_Esteira(num_esteira)
json_pd = Salva_json(num_esteira,dict_json)
Salva_csv(num_esteira,json_pd)

#json_pd.info()
#print("Numero de linhas = ",len(dict_json))
#print(dict_json)
print('-----------------------------------------------')
print('DADOS DA ESTEIRA N.' + str(num_esteira))
print('-----------------------------------------------')
print('Velocidade | Velocidade | Horario de registro  ')
print(' do  rolo  | da esteira |                      ')
print('-----------------------------------------------')
v_rolo = dict_json['velocidade_rolo']
v_esteira = dict_json['velocidade_esteira']
data = datetime.strptime(dict_json['timestamp'][0:10], '%Y-%m-%d').date()
hora = datetime.strptime(dict_json['timestamp'][11:19], '%H:%M:%S').time()
print(f'{v_rolo: >10.2f} | {v_esteira: >10.2f} | {data: %d/%m/%Y} {hora: %H:%M:%S}')
#print("--------------------------------------------------------------")
#print(dict_json['detalhes'][1]['velocidade_rolo'])
print("------------------------------------------------------")
print("                    Detalhes")
print('------------------------------------------------------')
print(' ID  | Velocidade | Velocidade | Horario de registro  ')
print('     |  do  rolo  | da esteira |                      ')
print('------------------------------------------------------')
i = 0
for elemento in dict_json['detalhes']:
    i = i + 1
    v_rolo = elemento['velocidade_rolo']
    v_esteira = elemento['velocidade_esteira']
    data = datetime.strptime(elemento['timestamp'][0:10], '%Y-%m-%d').date()
    hora = datetime.strptime(elemento['timestamp'][11:19], '%H:%M:%S').time()
    print(f'{i:>4} | {v_rolo: >10.2f} | {v_esteira: >10.2f} | {data: %d/%m/%Y} {hora: %H:%M:%S}')

#arq_csv = pd.read_csv(fcsv)
#print(arq_csv[3:])

#sb.displot(arq_csv['velocidade_rolo'])
#plt.show()

#arq_csv.head(10)
#arq_csv.info()
#arq_csv.head(10)

#print(s_json)