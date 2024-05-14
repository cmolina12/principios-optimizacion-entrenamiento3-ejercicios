# Importar las librerías necesarias
import pulp as lp
import matplotlib.pyplot as plt

# Definir conjuntos
P = ["Coco", "Almendra"]
R = ["Agua", "Extracto de coco", "Pasta de almendra", "Tiempo"]

# Definir parámetros
a_coco_agua = 0.40
a_almendra_agua = 0.47
a_coco_extracto = 0.35
a_almendra_pasta = 0.37
t_coco = 3.4
t_almendra = 2.6
U_coco = 12000
U_almendra = 9500
D_agua = 42
D_extracto = 17.8
D_pasta = 15.2
D_tiempo = 720

# Listas para guardar los resultados
capacidades = list(range(0, 101, 5))
valores_optimos = []

# Iterar sobre diferentes valores de capacidad de producción
for c in capacidades:
    # Crear el modelo
    modelo = lp.LpProblem("VeggieDrinks", lp.LpMaximize)
    
    # Definir las variables de decisión
    x = lp.LpVariable("Litros de bebida de coco", lowBound=0, cat=lp.LpContinuous)
    y = lp.LpVariable("Litros de bebida de almendra", lowBound=0, cat=lp.LpContinuous)
    
    # Definir la función objetivo
    modelo += (U_coco * x) + (U_almendra * y)
    
    # Definir las restricciones
    modelo += a_coco_extracto * x <= D_extracto
    modelo += a_almendra_pasta * y <= D_pasta
    modelo += a_coco_agua * x + a_almendra_agua * y <= D_agua
    modelo += t_coco * x + t_almendra * y <= D_tiempo
    modelo += x + y <= c
    
    # Resolver el problema
    modelo.solve()
    
    # Guardar el valor óptimo de la función objetivo
    valores_optimos.append(lp.value(modelo.objective))

# Graficar la capacidad de producción vs. el valor óptimo de la función objetivo
plt.figure(figsize=(10, 6))
plt.plot(capacidades, valores_optimos, marker='o', linestyle='-', color='b')
plt.title('Valor Óptimo de la Función Objetivo en Función de la Capacidad de Producción')
plt.xlabel('Capacidad de Producción (litros)')
plt.ylabel('Valor Óptimo de la Función Objetivo (COP)')
plt.grid(True)
plt.show()


pendiente = (valores_optimos[-1] - valores_optimos[0]) / (capacidades[-1] - capacidades[0])

print(f'La pendiente de la recta es: {pendiente:.2f} COP/litro')