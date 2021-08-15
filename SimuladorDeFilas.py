from GeradorDeNumerosAleatorios import GeradorDeNumerosAleatorios
from Fila import Fila
from Escalonador import Escalonador
from Utils import current_milli_time

gerador = GeradorDeNumerosAleatorios(current_milli_time(), 100_000)

fila1 = Fila(intervaloChegada=(2,4),
            intervalorAtendimento=(3,5),
            nServidores=2,
            capacidade=5,
            chegadaPrimeiro=3.0)

listaDeFilas = [fila1]

escalonador = Escalonador(gerador, listaDeFilas)
escalonador.inicializar_simulacao()

for fila in listaDeFilas:
    print(fila)