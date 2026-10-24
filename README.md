# Simulacion-y-analisis-act2
Simulación y análisis de señales con la transformada de Fourier
# Análisis de señales mediante la Transformada de Fourier en Python

## Descripción

Este proyecto implementa una simulación de señales en el dominio del tiempo y de la frecuencia utilizando Python. Se emplea la Transformada Discreta de Fourier (DFT) para analizar el contenido frecuencial de diferentes señales y comprender sus propiedades matemáticas.

## Objetivos

- Generar señales elementales: pulso rectangular, función escalón y señal senoidal.
- Calcular la Transformada de Fourier mediante `numpy.fft.fft()`.
- Representar la magnitud y la fase del espectro de frecuencia.
- Verificar las propiedades de linealidad y desplazamiento temporal.
- Comparar señales senoidales de diferentes frecuencias.
- Interpretar los resultados obtenidos en ambos dominios.

## Requisitos

- Python 3
- NumPy
- Matplotlib

Instalar las dependencias con el siguiente comando:

```bash
pip install numpy matplotlib
```

## Estructura del proyecto

```text
analisis-fourier/
├── analisis_fourier.py
└── README.md
```

## Ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar las bibliotecas necesarias.
4. Ejecutar el programa:

```bash
python analisis_fourier.py
```

## Funcionamiento

El programa realiza las siguientes operaciones:

1. Define la frecuencia de muestreo y el vector de tiempo.
2. Genera un pulso rectangular, una función escalón y una señal senoidal.
3. Calcula la Transformada Discreta de Fourier de cada señal.
4. Grafica las señales originales y sus espectros de magnitud y fase.
5. Comprueba la propiedad de linealidad.
6. Analiza el efecto del desplazamiento temporal.
7. Compara señales senoidales de 20 Hz y 40 Hz para ilustrar el escalamiento en frecuencia.

## Resultados esperados

- El pulso rectangular produce un espectro extendido con forma aproximada de sinc.
- La función escalón presenta una componente de continua y contenido en distintas frecuencias.
- La señal senoidal de 50 Hz presenta picos espectrales en las frecuencias de -50 Hz y +50 Hz.
- La linealidad se verifica mediante un error numérico cercano a cero.
- El desplazamiento temporal conserva la magnitud espectral y modifica la fase.
- Al aumentar la frecuencia de la señal senoidal de 20 Hz a 40 Hz, los picos espectrales se desplazan hacia frecuencias de mayor magnitud.

## Conclusión

La simulación permite observar cómo una señal puede analizarse tanto en el dominio del tiempo como en el dominio de la frecuencia. La Transformada de Fourier facilita la identificación de los componentes frecuenciales y permite estudiar propiedades fundamentales del procesamiento de señales.

## Autor

Nombre del estudiante: [Escribe tu nombre]

Asignatura: [Escribe el nombre de la asignatura]

## Licencia

Proyecto académico de uso educativo.
