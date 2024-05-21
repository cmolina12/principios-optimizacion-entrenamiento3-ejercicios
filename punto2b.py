

#Importar librerias
import pulp as lp #Importar la libreria PuLP
import matplotlib.pyplot as plt #Importar la libreria matplotlib para graficar

# Modelo dual
modelo_dual = lp.LpProblem("Maximizar_costo", lp.LpMaximize) #Definir el modelo como un problema de maximización

# Variables de decision

w1 = lp.LpVariable("Variable dual correspondiente a la restricción de requerimiento mínimo mensual para helado de vainilla - 1", lowBound=0, cat='Continuous') #Definir variable de decisión w1
w2 = lp.LpVariable("Variable dual correspondiente a la restricción de requerimiento mínimo mensual para helado de fresa - 2", lowBound=0, cat='Continuous') #Definir variable de decisión w2
w3 = lp.LpVariable("Variable dual correspondiente a la restricción de requerimiento mínimo mensual para helado de chocolate - 3", lowBound=0, cat='Continuous') #Definir variable de decisión w3
w4 = lp.LpVariable("Variable dual correspondiente a la restricción de capacidad máxima mensual de helado para sucursal Usaquén - 4", lowBound=0, cat='Continuous') #Definir variable de decisión w4
w5 = lp.LpVariable("Variable dual correspondiente a la restricción de capacidad máxima mensual de helado para sucursal Salitre - 5", lowBound=0, cat='Continuous') #Definir variable de decisión w5
w6 = lp.LpVariable("Variable dual correspondiente a la restricción de capacidad máxima mensual de helado para sucursal Chicó - 6", lowBound=0, cat='Continuous') #Definir variable de decisión w6
w7 = lp.LpVariable("Variable dual correspondiente a la restricción de capacidad máxima mensual de helado para sucursal Titán - 7", lowBound=0, cat='Continuous') #Definir variable de decisión w7

# Función objetivo

modelo_dual += 70 * w1 + 45 * w2 + 55 * w3 - 45 * w4 - 40 * w5 - 45 * w6 - 40 * w7 #Definir la función objetivo

# Restricciones
modelo_dual += w1 - w4 <= 30000 #Restriccion helado de vainilla en Usaquén
modelo_dual += w1 - w5 <= 31000 #Restriccion helado de vainilla en Salitre
modelo_dual += w1 - w6 <= 32000 #Restriccion helado de vainilla en Chicó
modelo_dual += w1 - w7 <= 29000 #Restriccion helado de vainilla en Titán
modelo_dual += w2 - w4 <= 29000 #Restriccion helado de fresa en Usaquén
modelo_dual += w2 - w5 <= 28000 #Restriccion helado de fresa en Salitre
modelo_dual += w2 - w6 <= 30000 #Restriccion helado de fresa en Chicó 
modelo_dual += w2 - w7 <= 28000 #Restriccion helado de fresa en Titán
modelo_dual += w3 - w4 <= 33000 #Restriccion helado de chocolate en Usaquén
modelo_dual += w3 - w5 <= 32000 #Restriccion helado de chocolate en Salitre
modelo_dual += w3 - w6 <= 34000 #Restriccion helado de chocolate en Chicó 
modelo_dual += w3 - w7 <= 31000 #Restriccion helado de chocolate en Titán

# Resolver el modelo
modelo_dual.solve() #Resolver el modelo

# Impresión de resultados

print("Status:", lp.LpStatus[modelo_dual.status]) #Imprimir el estado de la solución
print("Valor objetivo: ", lp.value(modelo_dual.objective)) #Imprimir el valor objetivo
for variable in modelo_dual.variables(): #Iterar sobre las variables del modelo
    var_name = "W" + variable.name.split("_")[-1]  # Obtener el nombre de la variable
    print(f"{var_name} = {variable.varValue}")  # Imprimir el valor de la variable