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
sizes_dac = list(range(5, 35, 5))  # Tamaños pequeños para DaC
sizes_dp = list(range(100, 10001, 300))  # Tamaños grandes para DP

times_dac = []
times_dp = []

# Pruebas para Divide and Conquer
for size in sizes_dac:
    heights = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    minEnergyFrogJumpDaC(heights, len(heights) - 1)
    end = time.perf_counter()
    times_dac.append(end - start)

# Pruebas para Programación Dinámica
for size in sizes_dp:
    heights = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    minEnergyFrogJumpDP(heights)
    end = time.perf_counter()
    times_dp.append(end - start)

# ---------------- Graficar resultados ----------------
plt.figure(figsize=(12, 6))

# Gráfica para DP
plt.subplot(1, 2, 1)
plt.plot(sizes_dp, times_dp, marker='o', label='DP (Bottom-Up)')
plt.title('Programación Dinámica - Tiempo vs N')
plt.xlabel('Tamaño de entrada (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.grid(True)
plt.legend()

# Gráfica para DaC
plt.subplot(1, 2, 2)
plt.plot(sizes_dac, times_dac, marker='o', color='red', label='Divide and Conquer')
plt.title('Divide and Conquer - Tiempo vs N')
plt.xlabel('Tamaño de entrada (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
