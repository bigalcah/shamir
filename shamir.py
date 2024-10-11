import random

# Definir la función para crear un polinomio con un secreto
def crear_polinomio(secreto, k, n, primo):
    # Crear un polinomio con coeficientes aleatorios y el secreto como término constante
    coeficientes = [secreto] + [random.randint(1, primo - 1) for _ in range(k - 1)]
    print("Coeficientes del polinomio:", coeficientes)
    
    # Crear las partes evaluando el polinomio en diferentes puntos
    partes = [(x, evaluar_polinomio(coeficientes, x, primo)) for x in range(1, n + 1)]
    return partes

# Evaluar el polinomio en x
def evaluar_polinomio(coeficientes, x, primo):
    y = 0
    for i, coef in enumerate(coeficientes):
        y += coef * (x ** i)
    return y % primo

# Función para reconstruir el secreto usando la interpolación de Lagrange
def reconstruir_secreto(partes, primo):
    def lagrange_interpolacion(x, puntos):
        total = 0
        for i, (xi, yi) in enumerate(puntos):
            xi_yi = yi
            for j, (xj, _) in enumerate(puntos):
                if i != j:
                    xi_yi *= (x - xj) * pow(xi - xj, -1, primo)
            total += xi_yi
        return total % primo

    secreto = lagrange_interpolacion(0, partes)
    return secreto

def main():
    secreto = int(input("Introduce el secreto: "))
    k = int(input("Introduce el número mínimo de partes necesarias para reconstruir el secreto: "))
    n = int(input("Introduce el número total de partes que se generarán: "))
    primo = 2089  # Un número primo mayor al secreto para el campo

    partes = crear_polinomio(secreto, k, n, primo)
    print("Partes generadas:", partes)

    partes_para_reconstruir = partes[:k]
    secreto_reconstruido = reconstruir_secreto(partes_para_reconstruir, primo)
    print("Secreto reconstruido:", secreto_reconstruido)

if __name__ == "__main__":
    main()
