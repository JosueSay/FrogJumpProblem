# Referencia: https://dpythoncodenemesis.medium.com/frog-jump-1d-dp-aa57fe7ec096

import random
import time
import matplotlib.pyplot as plt

# ---------------- Divide and Conquer ----------------
def minEnergyFrogJumpDaC(heights, n):
    if n == 0:
        return 0
    if n == 1:
        return abs(heights[1] - heights[0])
    return min(
        minEnergyFrogJumpDaC(heights, n-1) + abs(heights[n] - heights[n-1]),
        minEnergyFrogJumpDaC(heights, n-2) + abs(heights[n] - heights[n-2])
    )

# ---------------- Programación Dinámica (Bottom-Up) ----------------
def minEnergyFrogJumpDP(heights):
    n = len(heights)
    if n == 1:
        return 0
    prev2 = 0
    prev1 = abs(heights[1] - heights[0])
    for i in range(2, n):
        current = min(
            prev1 + abs(heights[i] - heights[i - 1]),
            prev2 + abs(heights[i] - heights[i - 2])
        )
        prev2 = prev1
        prev1 = current
    return prev1

# ---------------- Pruebas y medición de tiempos ----------------
def comparar_algoritmos(modo_test=True):
    if modo_test:
        sizes_dac = list(range(5, 35, 5))
        sizes_dp = list(range(100, 10001, 300))
        times_dac = []
        times_dp = []

        # DaC
        for size in sizes_dac:
            heights = [random.randint(0, 10000) for _ in range(size)]
            start = time.perf_counter()
            minEnergyFrogJumpDaC(heights, len(heights) - 1)
            end = time.perf_counter()
            times_dac.append(end - start)

        # DP
        for size in sizes_dp:
            heights = [random.randint(0, 10000) for _ in range(size)]
            start = time.perf_counter()
            minEnergyFrogJumpDP(heights)
            end = time.perf_counter()
            times_dp.append(end - start)

        # Gráficas
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(sizes_dp, times_dp, marker='o', label='DP (Bottom-Up)')
        plt.title('Programación Dinámica - Tiempo vs N')
        plt.xlabel('Tamaño de entrada (N)')
        plt.ylabel('Tiempo de ejecución (segundos)')
        plt.grid(True)
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(sizes_dac, times_dac, marker='o', color='red', label='Divide and Conquer')
        plt.title('Divide and Conquer - Tiempo vs N')
        plt.xlabel('Tamaño de entrada (N)')
        plt.ylabel('Tiempo de ejecución (segundos)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    else:
        # ---------- Validación de resultados + trazas para el primer caso ----------
        print("Comparando resultados DaC vs DP...\n")
        casos = [
            [1000, 100, 10000, 500, 1000],
            [10, 20, 30, 10],
            [30, 20, 50, 10, 40],
            [100, 90, 80, 70, 60, 50],
            [3, 1, 4, 1, 5, 9]
        ]

        # Función DaC con trazas visuales
        def minEnergyFrogJumpDaC_Paso_Paso(heights, n, nivel=0):
            indent = "  " * nivel
            if n == 0:
                print(f"{indent}E(0) = 0 (inicio)")
                return 0
            if n == 1:
                cost = abs(heights[1] - heights[0])
                print(f"{indent}E(1) = |{heights[1]} - {heights[0]}| = {cost}")
                return cost

            print(f"{indent}Evaluando E({n}):")
            salto1 = minEnergyFrogJumpDaC_Paso_Paso(heights, n - 1, nivel + 1)
            costo1 = salto1 + abs(heights[n] - heights[n - 1])
            print(f"{indent}  Salto desde {n-1} a {n}: {salto1} + |{heights[n]} - {heights[n-1]}| = {costo1}")

            salto2 = minEnergyFrogJumpDaC_Paso_Paso(heights, n - 2, nivel + 1)
            costo2 = salto2 + abs(heights[n] - heights[n - 2])
            print(f"{indent}  Salto desde {n-2} a {n}: {salto2} + |{heights[n]} - {heights[n-2]}| = {costo2}")

            resultado = min(costo1, costo2)
            print(f"{indent}E({n}) = min({costo1}, {costo2}) = {resultado}\n")
            return resultado

        # Función DP con trazas visuales
        def minEnergyFrogJumpDP_Paso_Paso(heights):
            n = len(heights)
            if n == 1:
                print("E(0) = 0 (solo un escalón)")
                return 0

            print("E(0) = 0")
            print(f"E(1) = |{heights[1]} - {heights[0]}| = {abs(heights[1] - heights[0])}")

            prev2 = 0
            prev1 = abs(heights[1] - heights[0])

            for i in range(2, n):
                cost1 = prev1 + abs(heights[i] - heights[i - 1])
                cost2 = prev2 + abs(heights[i] - heights[i - 2])
                current = min(cost1, cost2)
                print(f"E({i}) = min({cost1} (desde {i-1}), {cost2} (desde {i-2})) = {current}")
                prev2 = prev1
                prev1 = current

            return prev1

        for i, heights in enumerate(casos):
            print(f"Caso {i+1}:")
            print(f"  heights = {heights}")
            if i == 0:
                print("\n Trazado del algoritmo Divide and Conquer (caso 1):\n")
                res_dac = minEnergyFrogJumpDaC_Paso_Paso(heights, len(heights) - 1)

                print("\n Trazado del algoritmo Programación Dinámica (caso 1):\n")
                res_dp = minEnergyFrogJumpDP_Paso_Paso(heights)
            else:
                res_dac = minEnergyFrogJumpDaC(heights, len(heights) - 1)
                res_dp = minEnergyFrogJumpDP(heights)

            print(f"\n  DaC → {res_dac}")
            print(f"  DP  → {res_dp}")
            print(f"  Si Coinciden: {res_dac == res_dp}\n")




comparar_algoritmos(modo_test=False) # Cambia a False para validar resultados
