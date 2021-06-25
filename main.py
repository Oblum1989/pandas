import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

contagios = pd.read_excel('Intro2021.xlsx', sheet_name ='Lineal')
contagios_logaritmica = pd.read_excel('Intro2021.xlsx', sheet_name='Logaritmica')
contagios_exponencial = pd.read_excel('Intro2021.xlsx', sheet_name='Exponencial')
def lineal(x,m,b):
  y=m*x+b
  return y

def logaritmica(x,a,b):
  y = (a * (np.log(x))) + b
  return y

def exponencial(x,a,b):
  y = a * np.exp(b * x)
  return y

def regresion_lineal(x,y): # x= 'Tiempo'  y= 'Contagios'
  sumax = x.sum()
  sumay = y.sum()
  n = x.count()
  sumaxy = (x*y).sum()
  sumaal2 = sumax**2
  sumax2 = (x**2).sum()
  num = sumax*sumay - n*sumaxy
  den = sumaal2 - n*sumax2
  m = num/den
  mediax = x.mean()
  mediay = y.mean()
  b = mediay-m*mediax
  # c(t)= 0.50766*t + 1.9391
  return m,b

def regresion_logaritmica(x,y): # x= 'Tiempo'  y= 'Contagios'
  sumalogx = (np.log(x)).sum()
  sumay = y.sum()
  n = x.count()
  sumalogxy = (np.log(x)*y).sum()
  
  sumalogal2 = sumalogx**2
  sumalogx2 = (np.log(x)**2).sum()

  num = sumalogx*sumay - n*sumalogxy
  den = sumalogal2 - n*sumalogx2

  a = num/den

  mediay = y.mean()
  mediax = (np.log(x)).mean()
  b = mediay-a*mediax
  return a,b

def regresion_exponencial(x,y): # x= 'Tiempo'  y= 'Contagios'
  sumax = x.sum()
  sumalogy = (np.log(y)).sum()
  n = x.count()
  sumalogyx = (np.log(y)*x).sum()
  
  sumaxal2 = sumax**2
  sumax2 = (x**2).sum()

  num = sumax*sumalogy - n*sumalogyx
  den = sumaxal2 - n*sumax2

  b = num/den

  mediay = (np.log(y)).mean()
  mediax = (x).mean()
  a = mediay-b*mediax
  return a,b

def graficar_regresion_lineal():
  m,b= regresion_lineal(contagios['Tiempo'],contagios['Contagios'])
  ejex= np.linspace(0,30,20)
  ejey= lineal(ejex,m,b)
  contagios.plot(kind='scatter',x='Tiempo',y='Contagios',title= 'CONTAGIOS CUCUTA',color='y')
  plt.plot(ejex,ejey)
  plt.show()

def graficar_regresion_logaritmica():
  a,b= regresion_logaritmica(contagios_logaritmica['TIEMPO'],contagios_logaritmica['CONTAGIOS'])
  ejex= np.linspace(0,30,20)
  ejey= logaritmica(ejex,a,b)
  contagios.plot(kind='scatter',x='Tiempo',y='Contagios',title= 'CONTAGIOS CUCUTA',color='y')
  plt.plot(ejex,ejey)
  plt.show()

def graficar_regresion_exponencial():
  a,b= regresion_exponencial(contagios_exponencial['TIEMPO'],contagios_exponencial['CONTAGIOS'])
  ejex= np.linspace(0,30,20)
  ejey= exponencial(ejex,a,b)
  contagios.plot(kind='scatter',x='Tiempo',y='Contagios',title= 'CONTAGIOS CUCUTA',color='y')
  plt.plot(ejex,ejey)
  plt.show()


#graficar_regresion_lineal()
#graficar_regresion_logaritmica()
graficar_regresion_exponencial()