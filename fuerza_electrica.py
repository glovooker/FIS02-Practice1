"""
Universidad CENFOTEC - Física II
Proyecto: Cálculo de Fuerza Eléctrica entre Cargas Puntuales
Estudiante: Gabriel Lobo Ulloa
Fecha: Mayo 2025

Descripción:
Este programa calcula la fuerza eléctrica entre dos cargas puntuales:
- Q1: Carga fija en el origen (0,0)
- Q2: Carga variable que puede ubicarse en cualquier punto del plano cartesiano
- Retorna el vector de fuerza que actúa sobre Q2
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# Constante de Coulomb (N⋅m²/C²)
K_COULOMB = 8.99e9

def calcular_fuerza_electrica(q1, q2, x2, y2):
    """
    Calcula la fuerza eléctrica sobre la carga Q2 debido a Q1.
    
    Parámetros:
    q1 (float): Carga Q1 en Coulombs (fija en el origen)
    q2 (float): Carga Q2 en Coulombs 
    x2 (float): Coordenada x de Q2
    y2 (float): Coordenada y de Q2
    
    Retorna:
    tuple: (Fx, Fy, magnitud, dirección) donde:
        - Fx, Fy: componentes del vector fuerza en N
        - magnitud: magnitud del vector fuerza en N
        - dirección: ángulo en grados
    """
    
    # Verificar que Q2 no esté en el origen
    if x2 == 0 and y2 == 0:
        raise ValueError("Q2 no puede estar en el origen (misma posición que Q1)")
    
    # Calcular la distancia entre las cargas
    r = math.sqrt(x2**2 + y2**2)
    
    # Calcular la magnitud de la fuerza usando la Ley de Coulomb
    # F = k * |q1 * q2| / r²
    magnitud_fuerza = K_COULOMB * abs(q1 * q2) / (r**2)
    
    # Calcular el vector unitario de Q1 hacia Q2
    r_unitario_x = x2 / r
    r_unitario_y = y2 / r
    
    # Determinar la dirección de la fuerza (atracción o repulsión)
    if q1 * q2 > 0:  # Cargas del mismo signo -> repulsión
        signo = 1
        tipo_fuerza = "repulsión"
    else:  # Cargas de signo opuesto -> atracción
        signo = -1
        tipo_fuerza = "atracción"
    
    # Calcular las componentes del vector fuerza
    Fx = signo * magnitud_fuerza * r_unitario_x
    Fy = signo * magnitud_fuerza * r_unitario_y
    
    # Calcular el ángulo de dirección
    angulo_rad = math.atan2(Fy, Fx)
    angulo_grados = math.degrees(angulo_rad)
    
    return Fx, Fy, magnitud_fuerza, angulo_grados, tipo_fuerza

def graficar_sistema(q1, q2, x2, y2, Fx, Fy, tipo_fuerza):
    """
    Crea una representación gráfica del sistema de cargas y el vector fuerza.
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Configurar el rango del gráfico
    max_coord = max(abs(x2), abs(y2)) + 2
    ax.set_xlim(-max_coord, max_coord)
    ax.set_ylim(-max_coord, max_coord)
    
    # Dibujar las cargas
    # Q1 en el origen
    color_q1 = 'red' if q1 > 0 else 'blue'
    ax.scatter(0, 0, s=200, c=color_q1, marker='o', edgecolors='black', linewidth=2)
    ax.annotate(f'Q1 = {q1:.2e} C', (0, 0), xytext=(0.2, 0.2), 
                fontsize=10, ha='left')
    
    # Q2 en su posición
    color_q2 = 'red' if q2 > 0 else 'blue'
    ax.scatter(x2, y2, s=200, c=color_q2, marker='o', edgecolors='black', linewidth=2)
    ax.annotate(f'Q2 = {q2:.2e} C', (x2, y2), xytext=(x2+0.2, y2+0.2), 
                fontsize=10, ha='left')
    
    # Dibujar el vector fuerza sobre Q2
    # Escalar el vector para visualización
    escala = max_coord / max(abs(Fx), abs(Fy)) * 0.3 if max(abs(Fx), abs(Fy)) > 0 else 1
    Fx_grafico = Fx * escala
    Fy_grafico = Fy * escala
    
    ax.quiver(x2, y2, Fx_grafico, Fy_grafico, 
              angles='xy', scale_units='xy', scale=1, 
              color='green', width=0.006, headwidth=3, headlength=4)
    
    # Etiqueta del vector fuerza
    ax.annotate('F⃗', (x2 + Fx_grafico/2, y2 + Fy_grafico/2), 
                fontsize=14, color='green', weight='bold')
    
    # Línea punteada entre las cargas
    ax.plot([0, x2], [0, y2], 'k--', alpha=0.5, linewidth=1)
    
    # Configuración del gráfico
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.set_xlabel('x (m)', fontsize=12)
    ax.set_ylabel('y (m)', fontsize=12)
    ax.set_title(f'Fuerza Eléctrica entre Cargas Puntuales\nTipo: {tipo_fuerza.capitalize()}', 
                 fontsize=14, weight='bold')
    
    # Leyenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
                   markersize=10, label='Carga Positiva'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
                   markersize=10, label='Carga Negativa'),
        plt.Line2D([0], [0], color='green', linewidth=3, label='Vector Fuerza')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.show()

def mostrar_resultados(q1, q2, x2, y2, Fx, Fy, magnitud, angulo, tipo_fuerza):
    """
    Muestra los resultados del cálculo de manera organizada.
    """
    print("\n" + "="*60)
    print("           RESULTADOS DEL CÁLCULO")
    print("="*60)
    print(f"Configuración del sistema:")
    print(f"  Q1 (origen):      {q1:.2e} C en (0, 0)")
    print(f"  Q2 (variable):    {q2:.2e} C en ({x2}, {y2})")
    print(f"  Distancia:        {math.sqrt(x2**2 + y2**2):.4f} m")
    print(f"  Tipo de fuerza:   {tipo_fuerza.capitalize()}")
    print("\nVector de fuerza sobre Q2:")
    print(f"  Fx = {Fx:.6e} N")
    print(f"  Fy = {Fy:.6e} N")
    print(f"  |F⃗| = {magnitud:.6e} N")
    print(f"  θ = {angulo:.2f}°")
    print("="*60)

def obtener_datos_usuario():
    """
    Solicita los datos al usuario de manera interactiva.
    """
    print("="*60)
    print("    CALCULADORA DE FUERZA ELÉCTRICA")
    print("        Universidad CENFOTEC - Física II")
    print("="*60)
    print("Ingrese los siguientes datos:")
    print("(Use notación científica: ej. 2e-9 para 2×10⁻⁹)")
    
    try:
        q1 = float(input("\nCarga Q1 en el origen [C]: "))
        q2 = float(input("Carga Q2 [C]: "))
        x2 = float(input("Coordenada x de Q2 [m]: "))
        y2 = float(input("Coordenada y de Q2 [m]: "))
        
        return q1, q2, x2, y2
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
        return obtener_datos_usuario()

def main():
    """
    Función principal del programa.
    """
    # Obtener datos del usuario
    q1, q2, x2, y2 = obtener_datos_usuario()
    
    try:
        # Calcular la fuerza eléctrica
        Fx, Fy, magnitud, angulo, tipo_fuerza = calcular_fuerza_electrica(q1, q2, x2, y2)
        
        # Mostrar resultados
        mostrar_resultados(q1, q2, x2, y2, Fx, Fy, magnitud, angulo, tipo_fuerza)
        
        # Crear gráfico
        graficar_sistema(q1, q2, x2, y2, Fx, Fy, tipo_fuerza)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Función de ejemplo para pruebas
def ejemplo_demostracion():
    """
    Ejecuta un ejemplo predefinido para demostración.
    """
    print("Ejecutando ejemplo de demostración...")
    q1 = 2e-9  # 2 nC
    q2 = -3e-9  # -3 nC
    x2, y2 = 3, 4  # Posición de Q2
    
    Fx, Fy, magnitud, angulo, tipo_fuerza = calcular_fuerza_electrica(q1, q2, x2, y2)
    mostrar_resultados(q1, q2, x2, y2, Fx, Fy, magnitud, angulo, tipo_fuerza)
    graficar_sistema(q1, q2, x2, y2, Fx, Fy, tipo_fuerza)

if __name__ == "__main__":
    # Descomenta la línea siguiente para ejecutar el ejemplo
    # ejemplo_demostracion()
    
    # Ejecutar programa principal
    main()
