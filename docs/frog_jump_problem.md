# Frog Jump Problem (Minimización de energía en escaleras) 🐸

## 📝 Descripción del Problema

Existe una rana ubicada en el primer escalón de una escalera con **N** escalones. Cada escalón tiene una altura específica representada por un arreglo **`heights[]`**, donde **`heights[i]`** indica la altura del escalón **`i`**.

La rana desea llegar hasta el último escalón (escalón **`N`**). La rana puede dar saltos hacia adelante de **uno o dos escalones** por vez.

Cada salto consume energía, la cual depende de la diferencia absoluta entre las alturas de los escalones involucrados:

```markdown
Energía consumida = |heights[escalón_actual] - heights[escalón_destino]|
```

**Objetivo**: Encontrar la **cantidad mínima de energía** que la rana gastará para llegar desde el primer escalón hasta el último escalón.

## 📚 Ejemplos

### Ejemplo 1

```markdown
heights = [10, 20, 30, 10]

Salida: 20
```

**Explicación**:

- Salto del escalón 1 (altura 10) al escalón 2 (altura 20), energía = `|20-10| = 10`
- Salto del escalón 2 (altura 20) al escalón 4 (altura 10), energía = `|10-20| = 10`
- Energía total mínima = `10 + 10 = 20`

### Ejemplo 2

```markdown
heights = [30, 20, 50, 10, 40]

Salida: 30
```

**Explicación**:

- Salto escalón 1 → 3: `|50-30|=20`
- Salto escalón 3 → 5: `|40-50|=10`
- Energía total mínima = `20 + 10 = 30`

## 📐 Restricciones y Supuestos

- Número de casos de prueba: `T >= 30`
- Cantidad de escalones: `1 <= N <= 10^5`
- Altura de cada escalón: `0 <= heights[i] <= 10^4`
- La rana inicia siempre en el primer escalón.
- La rana puede avanzar sólo 1 o 2 escalones en cada salto.
- El objetivo es **minimizar la energía total consumida**.

## 📖 Referencias Documentales

La documentación que posees sobre este problema es la siguiente:

- [**Documentación 1 (Coding Ninjas, Frog Jump Energy minimization)**](https://www.naukri.com/code360/problems/frog-jump_3621012)
- [**Documentación 2 (GeeksForGeeks, Frog Jump – Min energy cost)**](https://www.geeksforgeeks.org/problems/geek-jump/0)
- [**Documentación 3 (TUFFrog Jump DP-3)**](https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/)
- [**Documentación 4 (GeeksForGeeks, Frog Jump - Climbing Stairs with Cost)**](https://www.geeksforgeeks.org/minimum-cost-for-hopping-frog-to-reach-stair-n/)
- [**Documentación 5 (Roshan Jha, Frog jumping problem with DP)**](https://medium.com/@Roshan-jha/frog-jumping-problem-and-its-dynamic-programming-solution-in-c-java-bef924aa2cd1)
