# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:28:47 2024

@author: cesar
"""

# Se importa la libreria PulP
import pulp as lp

# -------------------------------------
# Creación del objeto problema en PuLP
# -------------------------------------

prob = lp.LpProblem("Literal_f_p1", sense= lp.LpMinimize)

# -------------------------------------
# Variables
# -------------------------------------

w1 = lp.LpVariable("w1", lowBound=0)
w2 = lp.LpVariable("w2", lowBound=0)
w3 = lp.LpVariable("w3", lowBound=0)
w4 = lp.LpVariable("w4", lowBound=0)
w4 = lp.LpVariable("w4", lowBound=0)
w5 = lp.LpVariable("w5", lowBound=0)

# -------------------------------------
# Restricciones
# -------------------------------------

prob += 7 * w1 + w3 - w4 >= 17, "R1"
prob += 2 * w2 + w3 >= 30, "R2"
prob += 15 * w1 + 5 * w2 - 2 * w4 >= -4, "R3"
prob += 3 * w2 + 3 * w5 >= 5, "R4"
prob += -w4 + w5 >= -10, "R5"

# -------------------------------------
# Función objetivo
# -------------------------------------

prob += 105 * w1 + 765 * w2 + 220 * w3 - 120 * w4 + 225 * w5

# -------------------------------------
# Resolver el problema
# -------------------------------------

prob.solve()

# -------------------------------------
# Impresión de resultados
# -------------------------------------

print("Estado:", lp.LpStatus[prob.status])
print("El valor de la F.O. es:", lp.value(prob.objective))

# -------------------------------------
# Valores de las variables
# -------------------------------------

print("\nVariables:")
print("w1 =", lp.value(w1))
print("w2 =", lp.value(w2))
print("w3 =", lp.value(w3))
print("w4 =", lp.value(w4))
print("w5 =", lp.value(w5))

"""
Se puede utilizar la función de PuLp para llamar a las restricciones
directamente por el nombre dado y luego obtener la dual asociada 

print(prob.constraints["R1"])
print(prob.constraints["R1"].pi)
"""

# -------------------------------------
# Valores de las holguras asociadas a las restricciones del problema
# -------------------------------------
print("\nVariables de holgura:")

for v in range(1,6):
    print("r_"+str(v),"=",prob.constraints["R"+str(v)].slack)
# -------------------------------------
# Valores de las variables duales asociadas a las restricciones del problema
# -------------------------------------

print("\nVariables primales asociadas al dual:")

for v in range(1,6):
    print("x_"+str(v),"=",prob.constraints["R"+str(v)].pi)