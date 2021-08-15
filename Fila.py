class Fila:
    
    estadoAtual = 0
    tempoUltimoEvento = 0
    estadosDaFila = {}

    def __init__(self, intervaloChegada, intervalorAtendimento, nServidores, capacidade, chegadaPrimeiro):
        """
        Atributos
        ---------
        intervaloChegada : tuple
            tupla contendo o intervalo de chegada na fila
        intervalorAtendimento : tuple
            tupla contendo o intervalo de atendimento
        nServidores : int
            quantidade de servidores da fila
        capacidade : int
            quantidade de espacos na fila, -1 para infinito
        chegadaPrimeiro : int
            tempo em que chega o primeiro elemento da fila, -1 caso nao
        """

        self.intervaloChegada = intervaloChegada
        self.intervalorAtendimento = intervalorAtendimento
        self.nServidores = nServidores
        self.capacidade = capacidade
        self.chegadaPrimeiro = chegadaPrimeiro
    
    def adicionar_na_fila(self, tempoGlobal):
        self.__somar_tempo_passado_no_estado_atual(tempoGlobal)
        
        self.estadoAtual += 1

        if self.estadoAtual > self.capacidade and self.capacidade > -1:
            raise Exception("Erro logico: capacidade da fila excedida")

    def remover_da_fila(self, tempoGlobal):
        self.__somar_tempo_passado_no_estado_atual(tempoGlobal)
        
        self.estadoAtual -= 1

        if self.estadoAtual < 0:
            raise Exception("Erro logico: estado da fila negativo")
    
    def tem_espaco(self):
        return self.estadoAtual < self.capacidade or self.capacidade == -1
    
    def get_quantidade_na_fila(self):
        return self.estadoAtual

    def __somar_tempo_passado_no_estado_atual(self, tempoGlobal):
        tempoPassadoNoEstadoAtual = tempoGlobal - self.tempoUltimoEvento
        self.tempoUltimoEvento = tempoGlobal

        if self.estadoAtual not in self.estadosDaFila:
            self.estadosDaFila[self.estadoAtual] = 0
        
        self.estadosDaFila[self.estadoAtual] += tempoPassadoNoEstadoAtual

    def __str__(self):
        totalTime = 0

        for estado in self.estadosDaFila:
            totalTime += self.estadosDaFila[estado]
        
        print("==========================")

        for estado in self.estadosDaFila:
            tempoEstado = self.estadosDaFila[estado]
            print("Estado:", estado, "Tempo:", "%.4f" % tempoEstado, "Prob:", "%.2f" % ((tempoEstado / totalTime) * 100))
        
        print("Total", "%.4f" % totalTime, "100%")

        return ""