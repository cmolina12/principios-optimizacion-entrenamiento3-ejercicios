#---------------- Zona de imports ----------------

import pulp as lp

#---------------- Implementacion ----------------

    #Conjuntos

#Productos

P = ["Coco", "Almendra", "VeggieFusion"]

#Recursos

R = ["Agua", "Extracto de coco", "Pasta de almendra", "Tiempo"]

    #Parametros
    
a_coco_agua = 0.40 #Litros de agua por litro de coco

a_almendra_agua = 0.47 #Litros de agua por litro de almendra

a_coco_extracto = 0.35 #Litros de extracto de coco por litro de coco

a_almendra_pasta = 0.37 #Litros de pasta de almendra por litro de almendra

a_veggiefusion_extracto = 0.06 #Litros de extracto de coco por litro de VeggieFusion

a_veggiefusion_pasta = 0.05 #Litros de pasta de almendra por litro de VeggieFusion

a_veggiefusion_agua = 0.09 #Litros de agua por litro de VeggieFusion

t_coco = 3.4 #Minutos por litro de coco

t_almendra = 2.6 #Minutos por litro de almendra

t_veggiefusion = 5.5 #Minutos por litro de VeggieFusion

U_coco = 12000 #Utilidad por litro de coco

U_almendra = 9500 #Utilidad por litro de almendra

U_veggiefusion = 10500 #Utilidad por litro de VeggieFusion

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
z = lp.LpVariable("Litros de VeggieFusion", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión z

    #Funcion objetivo
    
modelo += (U_coco*x) + (U_almendra*y) + (U_veggiefusion*z) #Definir la función objetivo

    #Restricciones
    
#1. Restriccion de disponibilidad de extracto de coco para bebida de coco y VeggieFusion

modelo += a_coco_extracto*x + a_veggiefusion_extracto*z <= D_extracto

#2. Restriccion de disponibilidad de pasta de almendra para bebida de almendra y VeggieFusion

modelo += a_almendra_pasta*y + a_veggiefusion_pasta*z <= D_pasta

#3. Restriccion de disponibilidad de agua para las tres bebidas

modelo += a_coco_agua*x + a_almendra_agua*y + a_veggiefusion_agua*z <= D_agua

#4. Restriccion de tiempo de produccion para las tres bebidas

modelo += t_coco*x + t_almendra*y + t_veggiefusion*z <= D_tiempo

#5. Restriccion de capacidad de produccion

modelo += x + y + z <= c 

    #Solucion
    
modelo.solve()

    #Resultados
print("Estado: ", lp.LpStatus[modelo.status]) #Imprimir el estado de la solución
print("Utilidad máxima: ", lp.value(modelo.objective)) #Imprimir la utilidad máxima
print("Litros de bebida de coco: ", x.varValue) #Imprimir los litros de bebida de coco
print("Litros de bebida de almendra: ", y.varValue) #Imprimir los litros de bebida de almendra
print("Litros de VeggieFusion: ", z.varValue) #Imprimir los litros de VeggieFusion

#Restricciones activas

for r in modelo.constraints: #Iterar sobre las restricciones del modelo
    if modelo.constraints[r].pi != 0: #Si el multiplicador de Lagrange es diferente de cero
        print("Restriccion activa: ", r) #Imprimir el nombre de la restricción