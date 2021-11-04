from GeradorDeNumerosAleatorios import GeradorDeNumerosAleatorios
from Fila import Fila
from Escalonador import Escalonador
from Utils import current_milli_time

gerador = GeradorDeNumerosAleatorios(current_milli_time(), 100_000)

fila1 = Fila(nome="F1",
            intervaloChegada=(1,4),
            intervalorAtendimento=(1,1.5),
            nServidores=1,
            chegadaPrimeiro=1)

fila2 = Fila(nome="F2",
            intervalorAtendimento=(5,10),
            nServidores=3,
            capacidade=5)

fila3 = Fila(nome="F3",
            intervalorAtendimento=(10,20),
            nServidores=2,
            capacidade=8)

fila1.adicionar_fila_de_saida(fila2, 0.8)
fila1.adicionar_fila_de_saida(fila3, 0.2)

fila2.adicionar_fila_de_saida(fila1, 0.3)
fila2.adicionar_fila_de_saida(fila3, 0.5)

fila3.adicionar_fila_de_saida(fila2, 0.7)

listaDeFilas = [fila1, fila2, fila3]

escalonador = Escalonador(gerador, listaDeFilas)
escalonador.inicializar_simulacao()

for fila in listaDeFilas:
    print(fila)