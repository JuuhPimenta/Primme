import pandas as pd
import numpy as np



#Projeto teste 1 - Prime

#1 Importar dados prime

tabela = pd.read_csv ("priming.csv")
print(tabela.head())


#2 Variaveis
time = tabela ["tempo"]

item = tabela ["item"]

part = tabela ["particpante"]

prime = tabela ["prime"]

soa = tabela ["SOA"]

resp = tabela ["resposta"]


#criar laço de repetição 
a = 1

line = tabela.loc[a]

#3 Analise
def freq (time, prime):
 return time * prime 

freq in tabela ()
print(freq)