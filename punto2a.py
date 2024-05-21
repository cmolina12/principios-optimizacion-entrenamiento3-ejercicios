
#Enunciado


#Importar librerias
import pulp as lp #Importar libreria pulp para resolver problemas de programación lineal
import matplotlib.pyplot as plt #Importar libreria matplotlib para graficar

    # Conjuntos
S = ["Vainilla", "Fresa", "Chocolate"] #Sabores de helado
P = ["Usaquén", "Salitre", "Chicó", "Titán"] #Puntos de venta

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

modelo = lp.LpProblem("SimplexShakes", lp.LpMinimize) #Definir el modelo como un problema de minimización

    #Variables de decisión
    
a = lp.LpVariable("Litros de helado de vainilla comprados en Usaquén", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión a
b = lp.LpVariable("Litros de helado de vainilla comprados en Salitre", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión b
c = lp.LpVariable("Litros de helado de vainilla comprados en Chicó", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión c
d = lp.LpVariable("Litros de helado de vainilla comprados en Titán", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión d
e = lp.LpVariable("Litros de helado de fresa comprados en Usaquén", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión e
f = lp.LpVariable("Litros de helado de fresa comprados en Salitre", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión f
g = lp.LpVariable("Litros de helado de fresa comprados en Chicó", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión g
h = lp.LpVariable("Litros de helado de fresa comprados en Titán", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión h
i = lp.LpVariable("Litros de helado de chocolate comprados en Usaquén", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión i
j = lp.LpVariable("Litros de helado de chocolate comprados en Salitre", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión j 
k = lp.LpVariable("Litros de helado de chocolate comprados en Chicó", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión k
l = lp.LpVariable("Litros de helado de chocolate comprados en Titán", lowBound = 0, cat = lp.LpContinuous) #Definir variable de decisión l

    #Función objetivo
    
modelo += (C_vainilla_Usaquén * a) + (C_vainilla_Salitre * b) + (C_vainilla_Chicó * c) + (C_vainilla_Titán * d) + (C_fresa_Usaquén * e) + (C_fresa_Salitre * f) + (C_fresa_Chicó * g) + (C_fresa_Titán * h) + (C_chocolate_Usaquén * i) + (C_chocolate_Salitre * j) + (C_chocolate_Chicó * k) + (C_chocolate_Titán * l) #Definir la función objetivo

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
    
modelo.solve() #Resolver el modelo

    #Resultados
    
print("Estado: ", lp.LpStatus[modelo.status]) #Imprimir el estado de la solución
print("Costo mínimo: ", lp.value(modelo.objective)) #Imprimir el costo mínimo
 
print("Litros de helado de vainilla comprados en Usaquén: ", a.varValue) #Imprimir la cantidad de litros de helado de vainilla comprados en Usaquén
print("Litros de helado de vainilla comprados en Salitre: ", b.varValue) #Imprimir la cantidad de litros de helado de vainilla comprados en Salitre
print("Litros de helado de vainilla comprados en Chicó: ", c.varValue) #Imprimir la cantidad de litros de helado de vainilla comprados en Chicó
print("Litros de helado de vainilla comprados en Titán: ", d.varValue) #Imprimir la cantidad de litros de helado de vainilla comprados en Titán
print("Litros de helado de fresa comprados en Usaquén: ", e.varValue) #Imprimir la cantidad de litros de helado de fresa comprados en Usaquén
print("Litros de helado de fresa comprados en Salitre: ", f.varValue) #Imprimir la cantidad de litros de helado de fresa comprados en Salitre
print("Litros de helado de fresa comprados en Chicó: ", g.varValue) #Imprimir la cantidad de litros de helado de fresa comprados en Chicó
print("Litros de helado de fresa comprados en Titán: ", h.varValue) #Imprimir la cantidad de litros de helado de fresa comprados en Titán
print("Litros de helado de chocolate comprados en Usaquén: ", i.varValue) #Imprimir la cantidad de litros de helado de chocolate comprados en Usaquén
print("Litros de helado de chocolate comprados en Salitre: ", j.varValue) #Imprimir la cantidad de litros de helado de chocolate comprados en Salitre
print("Litros de helado de chocolate comprados en Chicó: ", k.varValue) #Imprimir la cantidad de litros de helado de chocolate comprados en Chicó
print("Litros de helado de chocolate comprados en Titán: ", l.varValue) #Imprimir la cantidad de litros de helado de chocolate comprados en Titán
print("")

#Mostrar datos en tabla tabulate
import pandas as pd #Importar libreria pandas
import tabulate as tb #Importar libreria tabulate
datos = { 
    'Sucursal': ['Usaquén', 'Salitre', 'Chicó', 'Titán'],
    'Vainilla': [a.varValue, b.varValue, c.varValue, d.varValue],
    'Fresa': [e.varValue, f.varValue, g.varValue, h.varValue],
    'Chocolate': [i.varValue, j.varValue, k.varValue, l.varValue]
} #Definir los datos a mostrar en la tabla

print(tb.tabulate(datos, headers='keys', tablefmt='fancy_grid')) #Imprimir los datos en una tabla

#Grafico de barras para cada sucursal


datos = {
        
        'Sabor': ['Vainilla', 'Fresa', 'Chocolate'],
        
        'Usaquén': [a.varValue, e.varValue, i.varValue],
        
        'Salitre': [b.varValue, f.varValue, j.varValue],
        
        'Chicó': [c.varValue, g.varValue, k.varValue],
        
        'Titán': [d.varValue, h.varValue, l.varValue]
        
    } #Definir los datos a mostrar en el gráfico

df = pd.DataFrame(datos) #Convertir los datos en un DataFrame

df.plot(x = 'Sabor', kind = 'bar', title = 'Litros de helado comprados por sabor y sucursal', color = ['blue', 'red', 'green', 'purple']) #Graficar los datos
 
plt.show() #Mostrar el gráfico

# -------------------------------------
# Valores de las holguras asociadas a las restricciones del problema
# -------------------------------------
print("\nVariables de holgura:") #Imprimir el título de la sección

for r in modelo.constraints: #Iterar sobre las restricciones del modelo
    print(f"La holgura de la restricción {r} es: {modelo.constraints[r].slack}") #Imprimir el valor de la holgura asociada a la restricción r
    
# -------------------------------------

# -------------------------------------

# Valores duales asociados a las restricciones del problema

# -------------------------------------

print("\nVariables duales:") #Imprimir el título de la sección
for r in modelo.constraints: #Iterar sobre las restricciones del modelo
    print(f"El valor dual de la restricción {r} es: {modelo.constraints[r].pi}") #Imprimir el valor dual asociado a la restricción r
    
# -------------------------------------

