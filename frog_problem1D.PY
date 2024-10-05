import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import time


def read_steps(file_path):
    """
    Lee números del archivo de texto y los devuelve como una lista de floats.
    
    :param file_path: Ruta del archivo con los datos de los pasos.
    :return: Lista de números flotantes extraídos del archivo.
    """
    with open(file_path, 'r') as file:
        steps = [float(line.strip()) for line in file]
    return steps


def simulate_frog_path(steps, threshold=0.5):
    """
    Simula el movimiento de una rana en un espacio unidimensional basado en pasos aleatorios.
    
    :param steps: Lista de números aleatorios que determinan los movimientos.
    :param threshold: Límite para determinar si el paso es hacia adelante o hacia atrás.
    :return: Coordenadas x e y de la trayectoria de la rana.
    """
    position = 0
    x_coords = [0]
    y_coords = [0]

    for i, step in enumerate(steps, start=1):
        if step <= threshold:
            position += 1  # Movimiento hacia adelante
        else:
            position -= 1  # Movimiento hacia atrás

        x_coords.append(i)
        y_coords.append(position)

    return x_coords, y_coords


def plot_frog_path_and_frequencies(x_coords, y_coords, processing_time):
    """
    Crea dos gráficos en subplots:
    1. La trayectoria de la rana en 1D.
    2. Un histograma de las frecuencias de posiciones de la rana.
    
    :param x_coords: Coordenadas en el eje x (número de pasos).
    :param y_coords: Coordenadas en el eje y (posición en 1D).
    :param processing_time: Tiempo de procesamiento para mostrar en la etiqueta del gráfico.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Gráfico 1: Trayectoria de la rana en 1D
    ax1.plot(x_coords, y_coords, marker='o', label='Path')
    ax1.scatter(x_coords[0], y_coords[0], color='green', s=100, label='Start', zorder=2)
    ax1.scatter(x_coords[-1], y_coords[-1], color='red', s=100, label='End', zorder=2)
    ax1.set_xlabel('Steps')
    ax1.set_ylabel('Position on X-axis')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.set_title('Frog Path in 1D')
    ax1.legend()

    # Etiqueta del tiempo de procesamiento
    ax1.text(0.95, 0.05, f'Time: {processing_time:.4f} sec',
             verticalalignment='bottom', horizontalalignment='right',
             transform=ax1.transAxes, color='blue', fontsize=12)

    # Gráfico 2: Histograma de frecuencias de posiciones
    ax2.hist(y_coords, bins=20, edgecolor='black', alpha=0.7)
    ax2.set_xlabel('Position')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Frequency of Frog Positions')

    # Ajustar el espacio entre subplots
    plt.tight_layout()

    # Mostrar los gráficos
    plt.show()


# Ruta del archivo de texto con los datos de los pasos
file_path = "data1D.txt"

# Medir el tiempo de procesamiento
start_time = time.time()

# Leer los números desde el archivo
steps = read_steps(file_path)

# Simular el recorrido de la rana en 1D
x_coords, y_coords = simulate_frog_path(steps)

# Calcular el tiempo de procesamiento
processing_time = time.time() - start_time

# Graficar la trayectoria de la rana y las frecuencias
plot_frog_path_and_frequencies(x_coords, y_coords, processing_time)
