def calcular_media(valores):
    return sum(valores) / len(valores)

print("Sistema de Automação de Cálculos Iniciado.")

import statistics

def calcular_desvio_padrao(valores):
    return statistics.stdev(valores)