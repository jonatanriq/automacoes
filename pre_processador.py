
import pandas as pd

def nomes_colunas_oceanpy(dataset):
  nino = dataset
  # colocando o titulo das colunas para minusculo
  nino = nino[nino.columns[:]].set_axis([nome.lower() for nome in nino.columns[:]], axis=1, inplace=False)
  # tirando os espaços dos nomes das colunas
  nino = nino[nino.columns[:]].set_axis([nome.strip() for nome in nino.columns[:]], axis=1, inplace=False)

  return nino

def datas_indices_oceanpy(dataset, colunas):
  # colocando o índice em datetime
  nino = dataset
  nino.index = pd.to_datetime(nino[nino.columns[colunas[0]]].astype(str)+'-'+nino[nino.columns[colunas[1]]].astype(str)+'-'+nino[nino.columns[colunas[2]]].astype(str))
  nino.drop([nomes for nomes in nino.columns[colunas]], axis=1, inplace=True)
  return nino
