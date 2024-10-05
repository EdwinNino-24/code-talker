import matplotlib.pyplot as plt
import time
from matplotlib.ticker import MaxNLocator

# Función para leer los números desde un archivo txt
def read_steps(file_path):
    """
    Lee números del archivo de texto y los devuelve como una lista de floats.
    
    :param file_path: Ruta del archivo con los datos de los pasos
    :return: Lista de números flotantes extraídos del archivo
    """
    with open(file_path, 'r') as file:
        steps = [float(line.strip()) for line in file]
    return steps

# Simulación de la rana en 2D
def simulate_frog_2d(steps, target_x, target_y, threshold=0.25):
    """
    Simula el movimiento de una rana en un plano bidimensional hasta llegar a una posición objetivo.
    
    :param steps: Lista de números aleatorios para decidir la dirección de los saltos.
    :param target_x: Posición objetivo en el eje X.
    :param target_y: Posición objetivo en el eje Y.
    :param threshold: Umbral para decidir la dirección del salto.
    :return: Coordenadas x e y de la trayectoria de la rana, junto con el número de pasos.
    """
    x, y = 0, 0
    x_coords = [x]
    y_coords = [y]
    
    for step in steps:
        if 0 < step <= threshold:  # Arriba
            y += 1
        elif threshold < step <= 2 * threshold:  # Abajo
            y -= 1
        elif 2 * threshold < step <= 3 * threshold:  # Derecha
            x += 1
        elif 3 * threshold < step <= 4 * threshold:  # Izquierda
            x -= 1

        x_coords.append(x)
        y_coords.append(y)

        # Si se alcanza la posición objetivo, registrar el número de pasos
        if x == target_x and y == target_y:
            break

    return x_coords, y_coords, len(x_coords) - 1

def plot_frog_path_2d(x_coords, y_coords, steps_taken, time_taken):
    """
    Crea un gráfico de la trayectoria de la rana en 2D con el punto de inicio y la posición final resaltados,
    y muestra el número de saltos realizados y el tiempo tomado.
    
    :param x_coords: Lista de coordenadas en el eje x.
    :param y_coords: Lista de coordenadas en el eje y.
    :param steps_taken: Cantidad de saltos realizados para llegar al objetivo.
    :param time_taken: Tiempo tomado para completar la trayectoria.
    """
    
    # Graficar la trayectoria
    plt.plot(x_coords, y_coords, marker='o', color='blue', label='Path')

    # Resaltar el punto de partida
    plt.scatter(x_coords[0], y_coords[0], color='green', marker='o', s=100, label='Start Position', zorder=2)

    # Resaltar la posición final
    plt.scatter(x_coords[-1], y_coords[-1], color='red', marker='o', s=100, label='End Position', zorder=2)

    # Etiquetas de los ejes
    plt.xlabel('Axis X')
    plt.ylabel('Axis Y')

    # Alinear los ejes a números enteros
    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # Mostrar leyenda y gráfico
    plt.legend()

    # Agregar información de los saltos y el tiempo
    plt.title(f'Frog Path in 2D\nSteps: {steps_taken}, Time: {time_taken:.4f} seconds')

    plt.grid(True)
    plt.show()


# Cargar los datos y simular el movimiento en 2D
file_path = "data2D.txt"
steps = read_steps(file_path)

# Simulación y medición de tiempo para 2D
start_time_2d = time.time()
x_coords_2d, y_coords_2d, steps_taken_2d = simulate_frog_2d(steps, target_x=250, target_y=300)
end_time_2d = time.time()

# Mostrar resultados
time_taken_2d = end_time_2d - start_time_2d
print(f"Steps taken in 2D: {steps_taken_2d}, Time taken: {time_taken_2d} seconds")

# Graficar la trayectoria en 2D con información adicional
plot_frog_path_2d(x_coords_2d, y_coords_2d, steps_taken_2d, time_taken_2d)