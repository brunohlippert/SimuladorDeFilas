from GeradorDeNumerosAleatorios import GeradorDeNumerosAleatorios
from Fila import Fila
from Escalonador import Escalonador
from Utils import current_milli_time

gerador = GeradorDeNumerosAleatorios(current_milli_time(), 100_000)

fila1 = Fila(intervaloChegada=(2,3),
            intervalorAtendimento=(2,5),
            nServidores=2,
            capacidade=3,
            chegadaPrimeiro=2.5)

fila2 = Fila(intervalorAtendimento=(3,5),
            nServidores=1,
            capacidade=3)

fila1.adicionar_fila_de_saida(fila2)

listaDeFilas = [fila1, fila2]

escalonador = Escalonador(gerador, listaDeFilas)
escalonador.inicializar_simulacao()

for fila in listaDeFilas:
    print(fila)