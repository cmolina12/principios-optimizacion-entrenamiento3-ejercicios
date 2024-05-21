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

prob = lp.LpProblem("Literal_h_p1", sense= lp.LpMaximize)

# -------------------------------------
# Variables
# -------------------------------------

x1= lp.LpVariable("x1", 0,None, lp.LpContinuous)
x2= lp.LpVariable("x2", 0,None, lp.LpContinuous)
x3= lp.LpVariable("x3", 0,None, lp.LpContinuous)
x4= lp.LpVariable("x4", 0,None, lp.LpContinuous)
x5= lp.LpVariable("x5", 0,None, lp.LpContinuous)


# -------------------------------------
# Restricciones
# -------------------------------------

prob += 7*x1 + 15*x3          <= 105, "R1"
prob += 2*x2 + 5*x3 +3*x4      <= 765, "R2"
prob += x1 + x2                <= 220, "R3"
prob += -x1 -2*x3 -x5          <= -120,  "R4"
prob += 3*x4 + x5              <=225, "R5"


# -------------------------------------
# Función objetivo
# -------------------------------------

prob += 17*x1 + 30*x2 - 4*x3 + 5*x4 - 10*x5


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
print("x1 =", lp.value(x1))
print("x2 =", lp.value(x2))
print("x3 =", lp.value(x3))
print("x4 =", lp.value(x4))
print("x5 =", lp.value(x5))

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
    print("s_"+str(v),"=",prob.constraints["R"+str(v)].slack)
# -------------------------------------
# Valores de las variables duales asociadas a las restricciones del problema
# -------------------------------------

print("\nVariables primales asociadas al dual:")

for v in range(1,6):
    print("W_"+str(v),"=",prob.constraints["R"+str(v)].pi)
