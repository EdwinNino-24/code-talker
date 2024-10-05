import matplotlib.pyplot as plt
import time


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


# Simulación de la rana en 3D
def simulate_frog_3d(steps, target_x, target_y, target_z, threshold=1 / 6):
    """
    Simula el movimiento de una rana en un espacio tridimensional hasta llegar a una posición objetivo.
    
    :param steps: Lista de números aleatorios para decidir la dirección de los saltos.
    :param target_x: Posición objetivo en el eje X.
    :param target_y: Posición objetivo en el eje Y.
    :param target_z: Posición objetivo en el eje Z.
    :param threshold: Umbral para decidir la dirección del salto.
    :return: Coordenadas x, y y z de la trayectoria de la rana, junto con el número de pasos.
    """
    x, y, z = 0, 0, 0
    x_coords = [x]
    y_coords = [y]
    z_coords = [z]
    
    for step in steps:
        if 0 < step <= threshold:  # Arriba
            y += 1
        elif threshold < step <= 2 * threshold:  # Abajo
            y -= 1
        elif 2 * threshold < step <= 3 * threshold:  # Derecha
            x += 1
        elif 3 * threshold < step <= 4 * threshold:  # Izquierda
            x -= 1
        elif 4 * threshold < step <= 5 * threshold:  # Adelante
            z += 1
        elif 5 * threshold < step <= 6 * threshold:  # Atrás
            z -= 1

        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)

        # Si se alcanza la posición objetivo, termina
        if x == target_x and y == target_y and z == target_z:
            break

    return x_coords, y_coords, z_coords, len(x_coords) - 1
    
    
def plot_frog_path_3d(x_coords, y_coords, z_coords):
    """
    Crea un gráfico de la trayectoria de la rana en 3D con el punto de inicio y la posición final resaltados.
    
    :param x_coords: Lista de coordenadas en el eje x.
    :param y_coords: Lista de coordenadas en el eje y.
    :param z_coords: Lista de coordenadas en el eje z.
    """
    # Crear figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficar la trayectoria
    ax.plot(x_coords, y_coords, z_coords, marker='o', color='blue', label='Path')

    # Resaltar el punto de partida
    ax.scatter(x_coords[0], y_coords[0], z_coords[0], color='green', s=100, label='Start Position', zorder=2)

    # Resaltar la posición final
    ax.scatter(x_coords[-1], y_coords[-1], z_coords[-1], color='red', s=100, label='End Position', zorder=2)

    # Etiquetas de los ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Título y leyenda
    ax.set_title('Frog Path in 3D')
    ax.legend()

    plt.show()


# Cargar los datos y simular el movimiento en 2D y 3D
file_path = "data.txt"
steps = read_steps(file_path)

# Simulación y medición de tiempo para 3D
start_time_3d = time.time()
x_coords_3d, y_coords_3d, z_coords_3d, steps_taken_3d = simulate_frog_3d(steps, target_x=45, target_y=23, target_z=17)
end_time_3d = time.time()

# Mostrar resultados
print(f"Steps taken in 3D: {steps_taken_3d}, Time taken: {end_time_3d - start_time_3d} seconds")

plot_frog_path_3d(x_coords_3d, y_coords_3d, z_coords_3d)
