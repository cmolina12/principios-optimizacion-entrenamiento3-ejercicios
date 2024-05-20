
#Enunciado

""""McDantzig es un restaurante de comida rápida ubicado en
la ciudad de Bogotá, el cual se especializa en la preparación
de deliciosas hamburguesas, perros calientes y sándwiches.
Debido a su gran éxito, el restaurante ha decidido
incursionar en el lanzamiento de nuevos productos que
complementen su menú y, recientemente, anunció la
inclusión de sus propias malteadas, las SimplexShakes.
El fundador del restaurante, el señor Jorge, ha determinado
que ofrecerá tres sabores de malteadas: vainilla, fresa y
chocolate. La receta de las malteadas es simple pues consta
únicamente del helado del sabor correspondiente batido durante unos minutos en una
máquina especial.
Por un lado, el señor Jorge ha contratado a un grupo de expertos para que le ayuden a
estimar la demanda mensual esperada de malteadas. Lo anterior para determinar los litros
de helado de cada sabor que se requiere como mínimo para satisfacer dicha demanda. Tras
recibir las estimaciones de los expertos y realizar algunos cálculos, el señor Jorge ha
resumido en la Tabla 1 el requerimiento mínimo de helado mensual (en litros) de cada sabor
para cumplir con la demanda esperada de malteadas.
Tabla 1. Requerimiento mínimo mensual (en litros) de cada sabor de helado.
Sabor de helado Requerimiento mínimo mensual de
helado (en litros)
Vainilla 70
Fresa 45
Chocolate 55
Por otro lado, el señor Jorge lo ha contratado a usted para que lo ayude en la logística de
abastecimiento de los tres sabores de helado. Él le ha comentado que, para ofrecer las
mejores malteadas, ha contactado a la mejor heladería de la ciudad, Popti, la cual cuenta
con cuatro puntos de venta diferentes en la ciudad. Dado que estos puntos manejan
distintos volúmenes de ventas, la gerente de Popti le ha informado al señor Jorge que cada
una de las cuatro sucursales está en capacidad de proveerle una cantidad máxima mensual
de litros de helado a McDantzig. Esta cantidad se muestra en la Tabla 2 y corresponde a la
suma de litros de helado de los tres sabores (vainilla, fresa y chocolate) que puede proveer
cada punto de venta.
Tabla 2. Cantidad máxima mensual de helado (en litros) que puede proveer cada sucursal.
Sucursal Cantidad máxima mensual (en litros)
Usaquén 45
Salitre 40
Chico 45
Titán 40
Finalmente, Popti le ha informado al señor Jorge que el costo de cada litro de helado que le
vende varía dependiendo del sabor y de la sucursal a la que se le pide. Esto debido a que
cada punto de venta maneja una estructura de costos diferente. La Tabla 3 muestra los
precios de un litro de helado de vainilla, fresa y chocolate en cada sucursal de Popti.
Tabla 3. Costo por litro de helado ($COP/litro).
Sabor de helado
Sucursal
Usaquén Salitre Chico Titán
Vainilla 30,000 31,000 32,000 29,000
Fresa 29,000 28,000 30,000 28,000
Chocolate 33,000 32,000 34,000 31,000
El señor Jorge se encuentra interesado en minimizar los costos de adquisición de los litros
de helado requeridos para sus malteadas. Por esta razón, como persona experta en
optimización, usted debe planificar la logística óptima de abastecimiento de cada sabor de
helado para que McDantzig logre satisfacer su demanda esperada de malteadas al menor
costo posible.
a. Formule un modelo de optimización lineal explícito (no indexado) para
determinar la logística de abastecimiento de helado, definiendo claramente las
variables de decisión, restricciones y función objetivo. Implemente el modelo
formulado utilizando Python-PuLP y reporte la solución óptima (función objetivo
y valor de las variables). Formulacion: Conjuntos
Sabores de helado – S={Vainilla,Fresa,Chocolate}
Puntos de venta (sucursales) – P={Usaquén,Salitre,Chicó,Titán}
Parámetros
D_vainilla=70∶Demanda minima mensual del sabor de helado vainilla ∈S
D_fresa=45∶Demanda minima mensual del sabor de helado fresa ∈S
D_chocolate=55∶Demanda minima mensual del sabor de helado chocolate ∈S
C_(vainilla,Usaquén)=30000∶Costo por litro del sabor vainilla ∈S en el punto de venta Usaquén ∈P
C_(vainilla,Salitre)=31000∶Costo por litro del sabor vainilla ∈S en el punto de venta Salitre ∈P
C_(vainilla,Chicó)=32000∶Costo por litro del sabor vainilla ∈S en el punto de venta Chicó ∈P
C_(vainilla,Titán)=29000∶Costo por litro del sabor vainilla ∈S en el punto de venta Titán ∈P
C_(fresa,Usaquén)=29000∶Costo por litro del sabor fresa ∈S en el punto de venta Usaquén ∈P
C_(fresa,Salitre)=28000∶Costo por litro del sabor fresa ∈S en el punto de venta Salitre ∈P
C_(fresa,Chicó)=30000∶Costo por litro del sabor fresa ∈S en el punto de venta Chicó ∈P
C_(fresa,Titán)=28000∶Costo por litro del sabor fresa ∈S en el punto de venta Titán ∈P
C_(chocolate,Usaquén)=33000:Costo por litro del sabor chocolate∈S en el punto de venta Usaquén∈P
C_(chocolate,Salitre)=32000∶Costo por litro del sabor chocolate ∈S en el punto de venta Salitre ∈P
C_(chocolate,Chicó)=34000∶Costo por litro del sabor chocolate ∈S en el punto de venta Chicó ∈P
C_(chocolate,Titán)=31000∶Costo por litro del sabor chocolate ∈S en el punto de venta Titán ∈P
M_Usaquén=45∶Capacidad maxima mensual en litros que puede proveer la sucursal Usaquén ∈P
M_Saitre=40∶Capacidad maxima mensual en litros que puede proveer la sucursal Salitre ∈P
M_Chicó=45∶Capacidad maxima mensual en litros que puede proveer la sucursal Chicó ∈P
M_Titán=40∶Capacidad maxima mensual en litros que puede proveer la sucursal Titán ∈P
Variables de decisión
a∶Litros de helado de vainilla comprados en Usaquén
b∶Litros de helado de vainilla comprados en Salitre
c∶Litros de helado de vainilla comprados en Chicó
d∶Litros de helado de vainilla comprados en Titán
e∶Litros de helado de fresa comprados en Usaquén
f∶Litros de helado de fresa comprados en Salitre
g∶Litros de helado de fresa comprados en Chicó
h∶Litros de helado de fresa comprados en Titán
i∶Litros de helado de chocolate comprados en Usaquén
j∶Litros de helado de chocolate comprados en Salitre
k∶Litros de helado de chocolate comprados en Chicó
l∶Litros de helado de chocolate comprados en Titán
Función objetivo
Minimizar Z=(C_(vainilla,Usaquén)*a)+(C_(vainilla,Salitre)*b)+(C_(vainilla,Chicó)*c)+(C_(vainilla,Titán)*d)+(C_(fresa,Usaquén)*e)+(C_(fresa,Salitre)*f)+(C_(fresa,Chicó)*g)+(C_(fresa,Titán)*h)+((C_(chocolate,Usaquén)*i)+(C_(chocolate,Salitre)*j)+(C_(chocolate,Chicó)*k)+(C_(chocolate,Titán)*l)
Restricciones
	Restricción de requerimiento mínimo mensual para helado de vainilla
a+b+c+d ≥D_vainilla
	Restricción de requerimiento mínimo mensual para helado de fresa
e+f+g+h ≥D_fresa
	Restricción de requerimiento mínimo mensual para helado de chocolate
i+j+k+l ≥D_chocolate
	Restricción de capacidad máxima mensual de helado para sucursal Usaquen
a+e+i ≤ M_Usaquén
	Restricción de capacidad máxima mensual de helado para sucursal Salitre
b+f+j ≤ M_Salitre
	Restricción de capacidad máxima mensual de helado para sucursal Chicó
c+g+k ≤ M_Chicó
	Restricción de capacidad máxima mensual de helado para sucursal Titán
d+h+l ≤ M_Chicó
	Naturaleza de las variables
a≥0
b≥0
c≥0
d≥0
e≥0
f≥0
g≥0
h≥0
i≥0
j≥0
k≥0
l≥0
"""

#Importar librerias
import pulp as lp
import matplotlib.pyplot as plt

    # Conjuntos
S = ["Vainilla", "Fresa", "Chocolate"]
P = ["Usaquén", "Salitre", "Chicó", "Titán"]

    # Parámetros
D_vainilla = 70 #Demanda minima mensual del sabor de helado vainilla ∈ S
D_fresa = 45  #Demanda minima mensual del sabor de helado fresa ∈ S
D_chocolate = 55 #Demanda minima mensual del sabor de helado chocolate ∈ S
C_vainilla_Usaquén = 30000 #Costo por litro del sabor vainilla ∈ S en el punto de venta Usaquén ∈ P
C_vainilla_Salitre = 31000 #Costo por litro del sabor vainilla ∈ S en el punto de venta Salitre ∈ P
C_vainilla_Chicó = 32000 #Costo por litro del sabor vainilla ∈ S en el punto de venta Chicó ∈ P
C_vainilla_Titán = 29000 #Costo por litro del sabor vainilla ∈ S en el punto de venta Titán ∈ P
C_fresa_Usaquén = 29000 #Costo por litro del sabor fresa ∈ S en el punto de venta Usaquén ∈ P
C_fresa_Salitre = 28000 #Costo por litro del sabor fresa ∈ S en el punto de venta Salitre ∈ P
C_fresa_Chicó = 30000 #Costo por litro del sabor fresa ∈ S en el punto de venta Chicó ∈ P
C_fresa_Titán = 28000 #Costo por litro del sabor fresa ∈ S en el punto de venta Titán ∈ P	
C_chocolate_Usaquén = 33000 #Costo por litro del sabor chocolate ∈ S en el punto de venta Usaquén ∈ P
C_chocolate_Salitre = 32000 #Costo por litro del sabor chocolate ∈ S en el punto de venta Salitre ∈ P
C_chocolate_Chicó = 34000 #Costo por litro del sabor chocolate ∈ S en el punto de venta Chicó ∈ P
C_chocolate_Titán = 31000 #Costo por litro del sabor chocolate ∈ S en el punto de venta Titán ∈ P
M_Usaquén = 45 #Capacidad maxima mensual en litros que puede proveer la sucursal Usaquén ∈ P
M_Salitre = 40 #Capacidad maxima mensual en litros que puede proveer la sucursal Salitre ∈ P
M_Chicó = 45 #Capacidad maxima mensual en litros que puede proveer la sucursal Chicó ∈ P
M_Titán = 40 #Capacidad maxima mensual en litros que puede proveer la sucursal Titán ∈ P

    #Modelo

modelo = lp.LpProblem("SimplexShakes", lp.LpMinimize)

    #Variables de decisión
    
a = lp.LpVariable("Litros de helado de vainilla comprados en Usaquén", lowBound = 0, cat = lp.LpContinuous)
b = lp.LpVariable("Litros de helado de vainilla comprados en Salitre", lowBound = 0, cat = lp.LpContinuous)
c = lp.LpVariable("Litros de helado de vainilla comprados en Chicó", lowBound = 0, cat = lp.LpContinuous)
d = lp.LpVariable("Litros de helado de vainilla comprados en Titán", lowBound = 0, cat = lp.LpContinuous)
e = lp.LpVariable("Litros de helado de fresa comprados en Usaquén", lowBound = 0, cat = lp.LpContinuous)
f = lp.LpVariable("Litros de helado de fresa comprados en Salitre", lowBound = 0, cat = lp.LpContinuous)
g = lp.LpVariable("Litros de helado de fresa comprados en Chicó", lowBound = 0, cat = lp.LpContinuous)
h = lp.LpVariable("Litros de helado de fresa comprados en Titán", lowBound = 0, cat = lp.LpContinuous)
i = lp.LpVariable("Litros de helado de chocolate comprados en Usaquén", lowBound = 0, cat = lp.LpContinuous)
j = lp.LpVariable("Litros de helado de chocolate comprados en Salitre", lowBound = 0, cat = lp.LpContinuous)
k = lp.LpVariable("Litros de helado de chocolate comprados en Chicó", lowBound = 0, cat = lp.LpContinuous)
l = lp.LpVariable("Litros de helado de chocolate comprados en Titán", lowBound = 0, cat = lp.LpContinuous)

    #Función objetivo
    
modelo += (C_vainilla_Usaquén * a) + (C_vainilla_Salitre * b) + (C_vainilla_Chicó * c) + (C_vainilla_Titán * d) + (C_fresa_Usaquén * e) + (C_fresa_Salitre * f) + (C_fresa_Chicó * g) + (C_fresa_Titán * h) + (C_chocolate_Usaquén * i) + (C_chocolate_Salitre * j) + (C_chocolate_Chicó * k) + (C_chocolate_Titán * l)

    #Restricciones
    
#1. Restricción de requerimiento mínimo mensual para helado de vainilla

modelo += a + b + c + d >= D_vainilla

#2. Restricción de requerimiento mínimo mensual para helado de fresa

modelo += e + f + g + h >= D_fresa

#3. Restricción de requerimiento mínimo mensual para helado de chocolate

modelo += i + j + k + l >= D_chocolate

#4. Restricción de capacidad máxima mensual de helado para sucursal Usaquén

modelo += a + e + i <= M_Usaquén

#5. Restricción de capacidad máxima mensual de helado para sucursal Salitre

modelo += b + f + j <= M_Salitre

#6. Restricción de capacidad máxima mensual de helado para sucursal Chicó

modelo += c + g + k <= M_Chicó

#7. Restricción de capacidad máxima mensual de helado para sucursal Titán

modelo += d + h + l <= M_Titán

    #Solución del modelo
    
modelo.solve()

    #Resultados
    
print("Estado: ", lp.LpStatus[modelo.status])
print("Costo mínimo: ", lp.value(modelo.objective))

print("Litros de helado de vainilla comprados en Usaquén: ", a.varValue)
print("Litros de helado de vainilla comprados en Salitre: ", b.varValue)
print("Litros de helado de vainilla comprados en Chicó: ", c.varValue)
print("Litros de helado de vainilla comprados en Titán: ", d.varValue)
print("Litros de helado de fresa comprados en Usaquén: ", e.varValue)
print("Litros de helado de fresa comprados en Salitre: ", f.varValue)
print("Litros de helado de fresa comprados en Chicó: ", g.varValue)
print("Litros de helado de fresa comprados en Titán: ", h.varValue)
print("Litros de helado de chocolate comprados en Usaquén: ", i.varValue)
print("Litros de helado de chocolate comprados en Salitre: ", j.varValue)
print("Litros de helado de chocolate comprados en Chicó: ", k.varValue)
print("Litros de helado de chocolate comprados en Titán: ", l.varValue)
print("")
#Mostrar datos en tabla tabulate

import pandas as pd
import tabulate as tb
datos = {
    'Sucursal': ['Usaquén', 'Salitre', 'Chicó', 'Titán'],
    'Vainilla': [a.varValue, b.varValue, c.varValue, d.varValue],
    'Fresa': [e.varValue, f.varValue, g.varValue, h.varValue],
    'Chocolate': [i.varValue, j.varValue, k.varValue, l.varValue]
}

print(tb.tabulate(datos, headers='keys', tablefmt='fancy_grid'))


