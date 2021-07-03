# -*- coding: utf-8 -*-
"""pandas_2021_AR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hAFhbYOsdF62YdRiXmrYyzhZgX08E93C
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# xlrd
# openyl

contagios= pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Intro_Pandas_2021.xlsx', sheet_name='Lineal')
#print(contagios.head())
#print(contagios.tail())
#print(contagios)
#contagios.plot(kind='scatter',x='Tiempo',y='Contagios',title= 'CONTAGIOS CUCUTA',color='y')
def lineal(x,m,b):
  y=m*x+b
  return y

def regresion_lineal(x,y): # x= 'Tiempo'  y= 'Contagios'
  sumax=x.sum()
  sumay=y.sum()
  n=x.count()
  sumaxy=(x*y).sum()
  sumaal2 =sumax**2
  sumax2=(x**2).sum()
  num =sumax*sumay - n*sumaxy
  den = sumaal2 -n*sumax2
  m = num/den
  mediax= x.mean()
  mediay= y.mean()
  b=mediay-m*mediax
  # c(t)= 0.50766*t + 1.9391
  return m,b

def graficar_regresion_lineal():
  m,b= regresion_lineal(contagios['Tiempo'],contagios['Contagios'])
  ejex= np.linspace(0,30,20)
  ejey= lineal(ejex,m,b)
  contagios.plot(kind='scatter',x='Tiempo',y='Contagios',title= 'CONTAGIOS CUCUTA',color='y')
  plt.plot(ejex,ejey)
  plt.show()


graficar_regresion_lineal()
#regresion_lineal(contagios['Tiempo'],contagios['Contagios'])

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


clase= pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Intro_Pandas_2021.xlsx',
                      sheet_name='Grupo_DR',
                      #usecols=[1,3,4]
                     index_col='DOCUMENTO')
#print(clase)
#print(clase.iat[2,2]) # CAICEDO DUARTE SEBASTIAN
#print(clase.iloc[8]) # filtra una fila
#print(clase.iloc[3:7]) # filtra un rango de filas
#print(clase.iloc[[2,7,12]]) # filtra n filas n, m, k
#print(clase.iloc[[2,7,12],[1,3]])
# IDENTIFICADOR
#print(clase.at[1193141052,'NOMBRE'])# CAICEDO DUARTE SEBASTIAN
#print(clase.loc[1004808870])
#print(clase.loc[1007663593:1004808870]) 
#print(clase.loc[[1007663593,1115916911,1193443908],['NOMBRE']]) 
# MANIPULACION DE DATOS
# UTILIZANDO FUNCIONES ----> .apply (consultar)
#clase['ACUMULADO']=clase['QUIZ']*0.15+clase['PARCIAL']*0.2
# groupby() ---> AGRUPAMIENTO
valores=clase['PARCIAL'].value_counts()
valores.plot(kind='pie')

print(valores)
# PARCIAL 3 CORTE
# HORA INICIO: 1 JULIO 4 PM
# FECHA ENTREGA: LUNES 5 12 MEDIO DIA
# GRUPOS 2 ESTUDIANTES
# 2.5 --> MANIPULACION DATOS ARCHIVO EXCEL ----> SUSTENTAR EL DIA MIERCOLES - JUEVES 
# 1.5 REGRESION
# SYMPY 1.0
# 5.0