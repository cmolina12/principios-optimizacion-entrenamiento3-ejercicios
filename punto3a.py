

#---------------- Zona de imports ----------------

import pulp as lp #Importar la libreria PuLP

#---------------- Implementacion ----------------

    #Conjuntos

#Productos

P = ["Coco", "Almendra"]

#Recursos

R = ["Agua", "Extracto de coco", "Pasta de almendra", "Tiempo"]

    #Parametros
    
a_coco_agua = 0.40 #Litros de agua por litro de coco 

a_almendra_agua = 0.47 #Litros de agua por litro de almendra

a_coco_extracto = 0.35 #Litros de extracto de coco por litro de coco

a_almendra_pasta = 0.37 #Litros de pasta de almendra por litro de almendra

t_coco = 3.4 #Minutos por litro de coco

t_almendra = 2.6 #Minutos por litro de almendra

U_coco = 12000 #Utilidad por litro de coco

U_almendra = 9500 #Utilidad por litro de almendra

D_agua = 42 #Litros de agua disponibles

D_extracto = 17.8 #Litros de extracto de coco disponibles

D_pasta = 15.2 #Litros de pasta de almendra disponibles

D_tiempo = 720 #Minutos disponibles

c = 75 #Capacidad de produccion

    #Modelo
    
modelo = lp.LpProblem("VeggieDrinks", lp.LpMaximize) #Definir el modelo como un problema de maximización

    #Variables de decision
    
x = lp.LpVariable("Litros de bebida de coco", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión x
y = lp.LpVariable("Litros de bebida de almendra", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión y

    #Funcion objetivo
    
modelo += (U_coco*x) + (U_almendra*y) #Definir la función objetivo

    #Restricciones
    
#1. Restriccion de disponibilidad de extracto de coco para bebida de coco

modelo += a_coco_extracto*x <= D_extracto

#2. Restriccion de disponibilidad de pasta de almendra para bebida de almendra

modelo += a_almendra_pasta*y <= D_pasta

#3. Restriccion de disponibilidad de agua para ambas bebidas

modelo += a_coco_agua*x + a_almendra_agua*y <= D_agua

#4. Restriccion de tiempo de produccion para ambas bebidas

modelo += t_coco*x + t_almendra*y <= D_tiempo

#5. Restriccion de capacidad de produccion

modelo += x + y <= c

    #Solucion
    
modelo.solve() #Resolver el modelo

    #Resultados
print("Estado: ", lp.LpStatus[modelo.status]) #Imprimir el estado de la solución
print("Utilidad máxima: ", lp.value(modelo.objective)) #Imprimir la utilidad máxima
print("Litros de bebida de coco: ", x.varValue) #Imprimir los litros de bebida de coco
print("Litros de bebida de almendra: ", y.varValue) #Imprimir los litros de bebida de almendra

#Restricciones activas

for r in modelo.constraints: #Iterar sobre las restricciones del modelo
    if modelo.constraints[r].pi != 0: #Si el valor dual de la restricción es diferente de cero
        print("Restriccion activa: ", r) #Imprimir el nombre de la restricción
        
# Imprimir los valores duales de todas las restricciones
for nombre, restriccion in modelo.constraints.items(): #Iterar sobre las restricciones del modelo
    print(f"El valor dual de la restricción {nombre} es: {restriccion.pi}") #Imprimir el valor dual de la restricción

#Graficas

import matplotlib.pyplot as plt #Importar la libreria matplotlib para graficar

#Datos

productos = ["Coco", "Almendra"] #Productos

utilidad = [U_coco, U_almendra] #Utilidad

#Grafica

#Produccion de bebidas 

plt.bar(productos, utilidad, color = "blue") #Graficar barras

plt.xlabel("Productos") #Etiqueta eje x

plt.ylabel("Utilidad") #Etiqueta eje y

plt.title("Utilidad de productos") #Titulo

plt.show() #Mostrar grafico
