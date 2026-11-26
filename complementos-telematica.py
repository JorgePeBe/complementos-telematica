import math


def calcular_potencia_recibida():
    p_tx_dbm = float(input("Potencia transmitida Pt (dBm): "))

    while True:
        try:
            g_tx_dbi = float(input("Ganancia antena transmisora Gt (dBi): "))
        except ValueError:
            print("Error: introduce un número válido.")
            continue
        if g_tx_dbi >= 0:
            break
        print("Error: la ganancia transmisora debe ser mayor o igual que 0 dBi.")

    while True:
        try:
            g_rx_dbi = float(input("Ganancia antena receptora Gr (dBi): "))
        except ValueError:
            print("Error: introduce un número válido.")
            continue
        if g_rx_dbi >= 0:
            break
        print("Error: la ganancia receptora debe ser mayor o igual que 0 dBi.")

    while True:
        try:
            perdidas_db = float(
                input("Pérdidas de propagación L (dB, valor negativo o 0): ")
            )
        except ValueError:
            print("Error: introduce un número válido.")
            continue
        if perdidas_db <= 0:
            break
        print("Error: las pérdidas deben ser menores o iguales que 0 dB.")

    # Las pérdidas se introducen como valor negativo: Pr = Pt + Gt + Gr + L.
    p_rx_dbm = p_tx_dbm + g_tx_dbi + g_rx_dbi + perdidas_db

    # Conversión de dBm a mW: P(mW) = 10^(P(dBm) / 10)
    p_rx_mw = math.pow(10, p_rx_dbm / 10)

    print("\n--- Resultados ---")
    print(f"Potencia transmitida (Pt): {p_tx_dbm:.2f} dBm")
    print(f"Ganancia transmisora (Gt): {g_tx_dbi:.2f} dBi")
    print(f"Ganancia receptora (Gr):   {g_rx_dbi:.2f} dBi")
    print(f"Pérdidas (L):              {perdidas_db:.2f} dB")
    print(f"Potencia recibida (Pr):    {p_rx_dbm:.2f} dBm")
    if p_rx_mw >= 1e-3:
        print(f"Potencia recibida (Pr):    {p_rx_mw:.6f} mW")
    else:
        print(f"Potencia recibida (Pr):    {p_rx_mw:.6e} mW")


if __name__ == "__main__":
    calcular_potencia_recibida()