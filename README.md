# Frog Jump Problem 🐸

Este repositorio contiene la solución al clásico problema de programación **Frog Jump**, resuelto mediante dos enfoques: **Divide and Conquer (DaC)** y **Programación Dinámica (DP)**.

## 📂 Estructura del proyecto

- `docs/`: Contiene la documentación detallada del problema, los algoritmos, análisis y comparativas, incluyendo referencias y explicaciones paso a paso.
- `code/`: Contiene el código fuente necesario para ejecutar y probar ambos enfoques.

## ⚙️ Instalación y ejecución

1. Clona el repositorio.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install -r ./code/requirements.txt
```

3. Ejecuta el script principal con:

```bash
python ./code/script.py
```

## 🧪 Modos de ejecución

Dentro del archivo `script.py`, puedes encontrar la función principal:

```python
comparar_algoritmos(modo_test=True)
```

- `modo_test=True`: Ejecuta ambos algoritmos y muestra una **gráfica comparativa de tiempos** de ejecución.
- `modo_test=False`: Muestra el **paso a paso detallado** y el **listado de configuraciones** utilizadas por los dos algoritmos (DaC y DP).

Modifica esta variable según el tipo de análisis que desees realizar.

## 📚 Documentación

Consulta los archivos dentro de la carpeta `docs/` para más información:

- `frog_jump_problem.md`: Introducción al problema.
- `divide_and_conquer.md`: Explicación del enfoque DaC.
- `demostracion_pd.md`: Explicación del enfoque DP.
- `divide_vs_dinamica.md`: Comparativa entre ambos enfoques.
- `analisis_de_resultados.md`: Análisis de resultados y conclusiones.
- `plantillas solución.md`: Plantillas base utilizadas.
