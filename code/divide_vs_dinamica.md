# Explicación: Divide and Conquer vs Programación Dinámica – Problema Frog Jump

Este documento complementa el análisis empírico del problema **Frog Jump**, detallando el **funcionamiento interno** de los dos enfoques aplicados: **Divide and Conquer (DaC)** y **Programación Dinámica (PD)**. Incluye ejemplos específicos del código donde se implementa cada parte de la lógica mencionada.

---

## ¿Qué es Divide and Conquer (DaC)?

### Descripción general

**Divide and Conquer** es una estrategia algorítmica que consiste en tres pasos:

1. **Dividir** el problema en subproblemas más pequeños.
2. **Resolver** cada subproblema de forma recursiva.
3. **Combinar** sus soluciones para formar la solución del problema original.

### 🐸 Aplicación en Frog Jump

En este problema, la rana puede llegar al escalón `n`:
- Desde el escalón `n-1` con un salto de 1.
- Desde el escalón `n-2` con un salto de 2.

Cada salto tiene un costo de energía:

\[E(n) = \min( E(n-1) + |h_n - h_{n-1}|,\; E(n-2) + |h_n - h_{n-2}| )\]

###  Código de ejemplo: Divide and Conquer puro
```python
def minEnergyFrogJumpDaC(heights, n):
    if n == 0:
        return 0  # caso base 1: está en el primer escalón
    if n == 1:
        return abs(heights[1] - heights[0])  # caso base 2

    # Divide: intenta dos caminos
    jump_one = minEnergyFrogJumpDaC(heights, n-1) + abs(heights[n] - heights[n-1])
    jump_two = minEnergyFrogJumpDaC(heights, n-2) + abs(heights[n] - heights[n-2])

    # Conquer: toma el mínimo de los dos
    return min(jump_one, jump_two)
```

### ❗ Desventaja
- Esta versión recalcula los mismos subproblemas muchas veces (por ejemplo, `E(3)`, `E(2)`...), lo que lleva a una complejidad **exponencial**:

\[ T(n) = O(2^n) \]

- No se almacena nada: **sin memorización**.

---

##  ¿Qué es Programación Dinámica (PD)?

###  Descripción general

La **Programación Dinámica** optimiza problemas que tienen:
- **Subproblemas traslapados**: el mismo cálculo ocurre muchas veces.
- **Subestructura óptima**: la solución óptima depende de las soluciones óptimas de subproblemas.

PD **almacena** los resultados ya calculados para no repetirlos.

###  Enfoque Bottom-Up (Tabulación)

En vez de usar recursión, se construye la solución desde abajo hacia arriba:
- Primero se calcula la energía para `E(0)`, `E(1)`...
- Luego `E(2)` se basa en esos dos valores anteriores.

###  Código de ejemplo: Programación Dinámica Bottom-Up
```python
def minEnergyFrogJumpDP(heights):
    n = len(heights)
    if n == 1:
        return 0  # caso base único

    prev2 = 0
    prev1 = abs(heights[1] - heights[0])

    # Construye solución iterativamente (Bottom-Up)
    for i in range(2, n):
        jump_one = prev1 + abs(heights[i] - heights[i - 1])
        jump_two = prev2 + abs(heights[i] - heights[i - 2])

        current = min(jump_one, jump_two)

        # Actualizar estado para la siguiente iteración
        prev2 = prev1
        prev1 = current

    return prev1  # energía mínima al llegar al último escalón
```

### ✅ Ventajas
- No hay llamadas recursivas.
- No se recalculan subproblemas.
- Complejidad temporal y espacial:

\[ T(n) = O(n),\quad\; S(n) = O(1) \]

---

## 🆚 Comparación entre DaC y PD

| Aspecto                        | Divide and Conquer          | Programación Dinámica (Bottom-Up) |
|-------------------------------|------------------------------|------------------------------------|
| Estructura                    | Recursiva                   | Iterativa                          |
| Cálculo repetido              | Sí                           | No                                 |
| Memoria adicional             | No                           | Sí, mínima (`prev1`, `prev2`)      |
| Complejidad temporal          | \(O(2^n)\)                   | \(O(n)\)                           |
| Escalabilidad                 | Mala                         | Excelente                          |
| Aplicación práctica           | Solo para tamaños pequeños   | Recomendado para casos grandes     |

---

##  Conclusión

- **Divide and Conquer** es útil para **entender la lógica del problema** de forma natural y recursiva.
- **Programación Dinámica**, en cambio, se basa en la **eficiencia**, evitando cálculos repetidos.
- En problemas con subproblemas traslapados como Frog Jump, **PD es superior**, especialmente en casos de entrada grandes.

> Para optimizar aún más DaC, se puede usar **memoización**: almacenar los resultados ya calculados. Esa técnica se conoce como **PD Top-Down**.

Este entendimiento es crucial para comparar enfoques algorítmicos y tomar decisiones basadas en rendimiento, legibilidad o complejidad del problema.

