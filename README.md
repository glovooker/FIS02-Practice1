# Calculadora de Fuerza Eléctrica entre Cargas Puntuales

**Universidad CENFOTEC - Escuela de Fundamentos**  
**Curso:** Física II (FIS-02)  
**Sección:** FCV1 - Periodo C2-2025  
**Docente:** Andrés Castro Núñez  
**Estudiante:** Gabriel Lobo Ulloa  
**Fecha de Entrega:** 1 de Junio de 2025

## 📋 Descripción del Proyecto

Este programa calcula la fuerza eléctrica entre dos cargas puntuales utilizando la Ley de Coulomb. El sistema está configurado con:

-   **Q1:** Carga fija ubicada en el origen (0,0)
-   **Q2:** Carga variable que puede ubicarse en cualquier punto del plano cartesiano
-   **Salida:** Vector de fuerza que actúa sobre la carga Q2

El programa incluye una representación gráfica que muestra ambas cargas y el vector de fuerza calculado.

## 🔧 Requisitos e Instalación

### Prerrequisitos

-   Python 3.6 o superior
-   pip (gestor de paquetes de Python)

### Instalación de Dependencias

El programa requiere la librería `matplotlib` para generar las visualizaciones gráficas.

```bash
pip install matplotlib
```

**Alternativa con conda:**

```bash
conda install matplotlib
```

### Instalación usando requirements.txt

Si prefieres usar el archivo de dependencias incluido:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución del Programa

### Modo Interactivo

Para ejecutar el programa en modo interactivo donde se pueden ingresar diferentes valores:

```bash
python fuerza_electrica.py
```

El programa solicitará:

-   Valor de la carga Q1 (en Coulombs)
-   Valor de la carga Q2 (en Coulombs)
-   Coordenadas x e y de la posición de Q2 (en metros)

**Ejemplo de entrada:**

```
Carga Q1 en el origen [C]: 2e-9
Carga Q2 [C]: -3e-9
Coordenada x de Q2 [m]: 3
Coordenada y de Q2 [m]: 4
```

### Modo Demostración (Ejemplo Precargado)

El programa incluye una función `ejemplo_demostracion()` que contiene valores predefinidos para probar rápidamente el funcionamiento.

**Para activar el ejemplo:**

1. **Opción 1 - Editar el código:**
   Abrir el archivo `fuerza_electrica.py` y descomentar la línea:

    ```python
    # ejemplo_demostracion()  # Quita el #
    ```

2. **Opción 2 - Ejecutar desde Python:**
    ```bash
    python -c "from fuerza_electrica import ejemplo_demostracion; ejemplo_demostracion()"
    ```

**El ejemplo incluye:**

-   Q1 = 2×10⁻⁹ C (carga positiva en el origen)
-   Q2 = -3×10⁻⁹ C (carga negativa)
-   Posición de Q2: (3, 4) metros

## 📊 Salida del Programa

El programa proporciona:

1. **Resultados numéricos:**

    - Componentes del vector fuerza (Fx, Fy)
    - Magnitud de la fuerza
    - Ángulo de dirección
    - Tipo de fuerza (atracción o repulsión)

2. **Visualización gráfica:**
    - Representación de ambas cargas con colores distintivos
    - Vector de fuerza sobre Q2
    - Sistema de coordenadas y etiquetas

## 🧮 Fundamentos Físicos

El programa implementa la **Ley de Coulomb:**

```
F = k * |q₁ * q₂| / r²
```

Donde:

-   `F`: Magnitud de la fuerza eléctrica
-   `k`: Constante de Coulomb (8.99 × 10⁹ N⋅m²/C²)
-   `q₁, q₂`: Cargas eléctricas
-   `r`: Distancia entre las cargas

**Dirección de la fuerza:**

-   **Repulsión:** Cargas del mismo signo (ambas + o ambas -)
-   **Atracción:** Cargas de signo opuesto (+ y - o - y +)

## 📁 Estructura del Proyecto

```
FIS02-Practice1/
├── fuerza_electrica.py      # Código principal
├── requirements.txt         # Dependencias del proyecto
├── LICENSE                  # Licencia de MIT
└── README.md                # Este archivo
```

## 👨‍💻 Funciones Principales

-   `calcular_fuerza_electrica()`: Implementa la Ley de Coulomb
-   `graficar_sistema()`: Genera la visualización gráfica
-   `obtener_datos_usuario()`: Interfaz para entrada de datos
-   `ejemplo_demostracion()`: Ejemplo precargado para pruebas
-   `main()`: Función principal del programa
