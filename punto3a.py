
#Enunciado

"""VeggieDrinks es una empresa innovadora que ofrece bebidas
vegetales diseñadas para promover una mejor nutrición y
adaptarse a diversos estilos de vida. Actualmente, la
empresa produce dos bebidas: de coco y de almendra.
Para producir un litro (𝐿) de bebida de coco se requieren
0.40 𝐿 de agua y 0.35 𝐿 de extracto de coco; mientras que
para producir un litro de bebida de almendra se requieren
0.47 𝐿 de agua y 0.37 𝐿 de pasta de almendra. Cabe
mencionar que la cantidad faltante para completar un litro de
los dos tipos de bebidas corresponde a saborizantes
naturales, azúcares añadidos y vitaminas que la empresa tiene en abundancia, por lo que
no es necesario considerarlos al planear la producción. Por ejemplo, para producir un (1)
litro de bebida de coco, se requieren 0.40 𝐿 de agua y 0.35 𝐿 de extracto de coco. Esto
significa que los 0.25 𝐿 restantes para completar un litro corresponden a saborizantes
naturales, azúcares añadidos y vitaminas, que no son considerados en la planeación de la
producción. Finalmente, el tiempo de producción de un litro de bebida de coco es de 3.4
minutos y de bebida de almendra es de 2.6 minutos.
Al inicio de cada semana, el proveedor de VeggieDrinks le proporciona los insumos
necesarios para la producción de sus bebidas. Adicionalmente, la maquinaria con la que
cuenta la empresa está en capacidad de producir semanalmente, máximo, 75 litros de
bebidas de cualquier tipo (en total). Debido al mal estado de la maquinaria, esta solo puede
operar, a lo sumo, durante 4 horas al día. Es decir, y dado que la producción solo se lleva a
cabo jueves, viernes y sábados, el tiempo disponible para la producción semanal es de 12
horas. La Tabla 1 muestra la información sobre la disponibilidad semanal de todos los
insumos.
Tabla 1. Disponibilidad semanal de insumos.
Insumo Cantidad disponible
Extracto de coco 17.8 𝐿
Pasta de almendra 15.2 𝐿
Agua 42 𝐿
Capacidad de producción 75 𝐿
Tiempo de producción 12 horas
Teniendo en cuenta el precio de venta, los costos de los insumos y los costos de producción,
la empresa tiene una utilidad de $12,000 COP y de $9,500 COP por cada litro que venda de
bebida de coco y de bebida de almendra, respectivamente. Debido a la creciente
popularidad de VeggieDrinks, la empresa vende todo lo que produce.
"""

#---------------- Zona de imports ----------------

import pulp as lp
import matplotlib.pyplot as plt

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
    
modelo = lp.LpProblem("VeggieDrinks", lp.LpMaximize)

    #Variables de decision
    
x = lp.LpVariable("Litros de bebida de coco", lowBound = 0, cat = lp.LpContinuous)
y = lp.LpVariable("Litros de bebida de almendra", lowBound = 0, cat = lp.LpContinuous)

    #Funcion objetivo
    
modelo += (U_coco*x) + (U_almendra*y)

    #Restricciones
    
#1. Restriccion de disponibilidad de extracto de coco para bebida de coco

modelo += a_coco_extracto*x <= D_extracto

#2. Restriccion de disponibilidad de pasta de almendra para bebida de almendra

modelo += a_almendra_pasta*y <= D_pasta

#3. Restriccion de disponibilidad de agua para bebida de coco

modelo += a_coco_agua*x <= D_agua

#4. Restriccion de disponibilidad de agua para bebida de almendra

modelo += a_almendra_agua*y <= D_agua

#5. Restriccion de tiempo de produccion para bebida de coco

modelo += t_coco*x <= D_tiempo

#6. Restriccion de tiempo de produccion para bebida de almendra

modelo += t_almendra*y <= D_tiempo

#7. Restriccion de capacidad de produccion

modelo += x + y <= c

    #Solucion
    
modelo.solve()

    #Resultados
print("Estado: ", lp.LpStatus[modelo.status])
print("Utilidad máxima: ", lp.value(modelo.objective))
print("Litros de bebida de coco: ", x.varValue)
print("Litros de bebida de almendra: ", y.varValue)


