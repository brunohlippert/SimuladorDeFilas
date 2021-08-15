from enum import Enum
from Utils import muda_base_de_numero

class TiposEvento(Enum):
        CHEGADA = 0
        SAIDA = 1

class Escalonador:

    eventos = []
    tempoGlobal = 0.0

    def __init__(self, geradorDeAleatorios, listaDeFilas):
        self.geradorDeAleatorios = geradorDeAleatorios
        self.__inicializar_eventos_com_primeiras_chegadas(listaDeFilas)
        
    def __inicializar_eventos_com_primeiras_chegadas(self, listaDeFilas):
        for fila in listaDeFilas:
            if fila.chegadaPrimeiro > -1:
                self.__agendar_evento(TiposEvento.CHEGADA, fila.chegadaPrimeiro, fila)
    
    def inicializar_simulacao(self):
        while(self.geradorDeAleatorios.ha_numero_para_gerar()):
            evento = self.__pop_proximo_evento()
            self.tempoGlobal = evento["tempo"]

            if evento["tipo"] == TiposEvento.CHEGADA:
                self.__gerencia_chegada(evento)
            else:
                self.__gerencia_saida(evento)

    def __gerencia_chegada(self, evento):
        fila = evento["fila"]
        if fila.tem_espaco():
            fila.adicionar_na_fila(self.tempoGlobal)

            # Se tem um servidor livre ja atende a requisicao
            if fila.get_quantidade_na_fila() <= fila.nServidores:
                numeroAleatorio = self.geradorDeAleatorios.gerar_proximo_numero_aleatorio()
                horarioDaSaida = self.__calcular_tempo_proximo_evento(fila.intervalorAtendimento, numeroAleatorio)
                self.__agendar_evento(TiposEvento.SAIDA, horarioDaSaida, fila)
            
        # Agenda a proxima chegada, se nao nao faz nada e termina a execucao
        if self.geradorDeAleatorios.ha_numero_para_gerar():
            numeroAleatorio = self.geradorDeAleatorios.gerar_proximo_numero_aleatorio()
            horarioDaChegada = self.__calcular_tempo_proximo_evento(fila.intervaloChegada, numeroAleatorio)
            self.__agendar_evento(TiposEvento.CHEGADA, horarioDaChegada, fila)

    def __gerencia_saida(self, evento):
        fila = evento["fila"]
        fila.remover_da_fila(self.tempoGlobal)

        if fila.get_quantidade_na_fila() >= 1:
            numeroAleatorio = self.geradorDeAleatorios.gerar_proximo_numero_aleatorio()
            horarioDaSaida = self.__calcular_tempo_proximo_evento(fila.intervalorAtendimento, numeroAleatorio)
            self.__agendar_evento(TiposEvento.SAIDA, horarioDaSaida, fila)
    
    def __pop_proximo_evento(self):
        indexMaisProximo = 0
        diferencaMaisProximo = self.eventos[indexMaisProximo]["tempo"] - self.tempoGlobal
        
        for i in range(1, len(self.eventos)):
            evento = self.eventos[i]
            diferencaEventoI = evento["tempo"] - self.tempoGlobal
            if diferencaEventoI < diferencaMaisProximo:
                indexMaisProximo = i
                diferencaMaisProximo = diferencaEventoI
        
        proximoEvento = self.eventos[indexMaisProximo]
        del self.eventos[indexMaisProximo]

        return proximoEvento

    def __calcular_tempo_proximo_evento(self, intervalo, numeroRandomico):
        return self.tempoGlobal + muda_base_de_numero(intervalo[0], intervalo[1], numeroRandomico)


    def __agendar_evento(self, tipoEvento, tempoDoEvento, fila):
        self.eventos.append(
            {
                "tipo" : tipoEvento,
                "tempo" : tempoDoEvento,
                "fila" : fila
            }
        )