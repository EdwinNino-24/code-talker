import random

# Genera un archivo con 1,000,000 de números aleatorios entre 0 y 1 truncados a 5 decimales
def generate_random_numbers(file_name, amount):
    with open(file_name, 'w') as file:
        for _ in range(amount):
            number = f"{random.uniform(0, 1):.5f}"  # Genera un número y truncar a 5 decimales
            file.write(f"{number}\n")

# Genera el archivo con 1,000,000 de números
generate_random_numbers('data.txt', 1000000)
