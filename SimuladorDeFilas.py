from GeradorDeNumerosAleatorios import GeradorDeNumerosAleatorios
from Fila import Fila
from Utils import current_milli_time

gerador = GeradorDeNumerosAleatorios(current_milli_time(), 100_000)

fila1 = Fila(intervaloChegada=(1,2),
            intervalorAtendimento=(3,6),
            nServidores=1,
            capacidade=3,
            chegadaPrimeiro=2.0)