import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. CONFIGURACION DE LA SIMULACION
# ==========================================================

fs = 1024                  # Frecuencia de muestreo en Hz
N = 1024                   # Numero de muestras
t = np.arange(N) / fs      # Vector de tiempo en segundos

# Vector de frecuencias centrado en cero
f = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))


# ==========================================================
# 2. DEFINICION DE LAS SEÑALES EN EL DOMINIO DEL TIEMPO
# ==========================================================

# Pulso rectangular: amplitud 1 entre 0.25 y 0.50 segundos
pulso = np.where((t >= 0.25) & (t < 0.50), 1.0, 0.0)

# Funcion escalon: cambia de 0 a 1 en t = 0.50 segundos
escalon = np.where(t >= 0.50, 1.0, 0.0)

# Señal senoidal de 50 Hz y amplitud 1
senoidal = np.sin(2 * np.pi * 50 * t)


# ==========================================================
# 3. FUNCION PARA CALCULAR Y GRAFICAR LA TRANSFORMADA
# ==========================================================

def analizar_senal(x, nombre):
    # Calcula la Transformada Discreta de Fourier
    X = np.fft.fft(x)

    # Centra el espectro para mostrar frecuencias negativas
    X_centrada = np.fft.fftshift(X)

    # Magnitud normalizada y fase en radianes
    magnitud = np.abs(X_centrada) / N
    fase = np.angle(X_centrada)

    # Evita interpretar la fase de componentes casi nulos
    fase[magnitud < 1e-6] = np.nan

    # Grafica la señal y sus espectros
    fig, ax = plt.subplots(3, 1, figsize=(10, 9))

    ax[0].plot(t, x)
    ax[0].set_title(f"{nombre}: dominio del tiempo")
    ax[0].set_xlabel("Tiempo (s)")
    ax[0].set_ylabel("Amplitud")
    ax[0].grid(True)

    ax[1].plot(f, magnitud)
    ax[1].set_title("Espectro de magnitud")
    ax[1].set_xlabel("Frecuencia (Hz)")
    ax[1].set_ylabel("Magnitud normalizada")
    ax[1].set_xlim(-150, 150) 
    ax[1].grid(True)

    ax[2].plot(f, fase, ".")
    ax[2].set_title("Espectro de fase")
    ax[2].set_xlabel("Frecuencia (Hz)")
    ax[2].set_ylabel("Fase (rad)")
    ax[2].set_xlim(-150, 150)
    ax[2].grid(True)

    plt.tight_layout()
    plt.show()

    return X


# ==========================================================
# 4. VISUALIZACION DE LAS TRES SEÑALES
# ==========================================================

X_pulso = analizar_senal(pulso, "Pulso rectangular")
X_escalon = analizar_senal(escalon, "Funcion escalon")
X_senoidal = analizar_senal(senoidal, "Señal senoidal")


# ==========================================================
# 5. PROPIEDAD DE LINEALIDAD
# ==========================================================

# La transformada de a*x + b*y debe ser a*X + b*Y
a = 2
b = 3

senal_combinada = a * pulso + b * senoidal
X_combinada = np.fft.fft(senal_combinada)

X_lineal = a * np.fft.fft(pulso) + b * np.fft.fft(senoidal)

error_linealidad = np.max(np.abs(X_combinada - X_lineal))
print("Error de linealidad:", error_linealidad)


# ==========================================================
# 6. PROPIEDAD DE DESPLAZAMIENTO EN EL TIEMPO
# ==========================================================

# Desplazamiento circular de 50 muestras
desplazamiento = 50
senal_desplazada = np.roll(senoidal, desplazamiento)

X_desplazada = np.fft.fft(senal_desplazada)
X_original = np.fft.fft(senoidal)

# El desplazamiento cambia la fase, pero conserva la magnitud
error_magnitud = np.max(
    np.abs(np.abs(X_desplazada) - np.abs(X_original))
)

print("Error de magnitud por desplazamiento:", error_magnitud)


# ==========================================================
# 7. ESCALAMIENTO EN FRECUENCIA
# ==========================================================

# Compara dos senoidales: 20 Hz y 40 Hz.
# Duplicar la frecuencia comprime el periodo a la mitad.
seno_20 = np.sin(2 * np.pi * 20 * t)
seno_40 = np.sin(2 * np.pi * 40 * t)

F20 = np.fft.fftshift(np.fft.fft(seno_20))
F40 = np.fft.fftshift(np.fft.fft(seno_40))

plt.figure(figsize=(10, 5))
plt.plot(f, np.abs(F20) / N, label="Senoidal de 20 Hz")
plt.plot(f, np.abs(F40) / N, label="Senoidal de 40 Hz")
plt.xlim(-80, 80)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud normalizada")
plt.title("Comparacion del escalamiento en frecuencia")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("Analisis de Fourier finalizado.")
