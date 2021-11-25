# importando o pacote pandas
import pandas as pd

# essa função permite colocar o titulo das colunas minusculo e também tirar os espaços das colunas
def nomes_colunas_oceanpy(dataset):
  nino = dataset
  nino = nino[nino.columns[:]].set_axis([nome.lower() for nome in nino.columns[:]], axis=1, inplace=False)
  nino = nino[nino.columns[:]].set_axis([nome.strip() for nome in nino.columns[:]], axis=1, inplace=False)
  return nino

# Essa função me permite colocar o índice em datetime
def datas_indices_oceanpy(dataset, colunas):
  nino = dataset
  nino.index = pd.to_datetime(nino[nino.columns[colunas[0]]].astype(str)+'-'+nino[nino.columns[colunas[1]]].astype(str)+'-'+nino[nino.columns[colunas[2]]].astype(str))
  nino.drop([nomes for nomes in nino.columns[colunas]], axis=1, inplace=True)
  return nino

# Essa função me permite analisar as colunas e cortar aquelas que tem mais de 50% dos dados faltando
def analise_colunas(dataset):
  for nome in dataset.columns[:]:
    if dataset[nome].isnull().sum()/len(dataset[nome]) > 0.5: 
      dataset.drop(nome, axis=1,inplace=True)
  return dataset