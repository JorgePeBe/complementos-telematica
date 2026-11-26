# Cálculo de Potencia Recibida en un Radioenlace

**Autor:** [Jorge Pérez Berlanga]

## ¿Qué hace el script?
Este programa en Python (`complementos-telematica.py`) calcula la **potencia recibida ($P_r$)** en un enlace de comunicaciones a partir de los parámetros básicos del balance de enlace introducidos por teclado:

* **Potencia transmitida ($P_t$):** en $\text{dBm}$.
* **Ganancia de la antena transmisora ($G_t$):** en $\text{dBi}$ (validada para que sea $\ge 0$).
* **Ganancia de la antena receptora ($G_r$):** en $\text{dBi}$ (validada para que sea $\ge 0$).
* **Pérdidas de propagación ($L$):** en $\text{dB}$ (validadas para que se introduzcan como valor negativo o cero, $\le 0$).

A partir de estos datos, aplica la ecuación del balance de enlace en unidades logarítmicas:

$$P_r\text{ (dBm)} = P_t + G_t + G_r + L$$

Posteriormente convierte el resultado a unidades lineales en milivatios mediante $P_r\text{ (mW)} = 10^{P_r\text{ (dBm)} / 10}$ y muestra por consola un resumen completo con todos los parámetros y resultados formateados.

## Requisitos y cómo se ejecuta
Solo requiere tener instalado **Python 3** (utiliza únicamente el módulo estándar `math`).

1. Descarga el archivo `complementos-telematica.py` o clona este repositorio.
2. Abre una terminal en la carpeta donde se encuentre el archivo.
3. Ejecuta el siguiente comando:

```bash
python complementos-telematica.py
