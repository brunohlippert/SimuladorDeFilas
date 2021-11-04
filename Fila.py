import operator
class Fila:
    def __init__(self, intervalorAtendimento, nServidores, capacidade, chegadaPrimeiro=-1, intervaloChegada=None,):
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

        self.estadoAtual = 0
        self.tempoUltimoEvento = 0
        self.estadosDaFila = {}
        self.saida = []

    def adicionar_fila_de_saida(self, fila, prob=1):
        """
        Adiciona uma fila de saida com uma probabilidade, padrão 100% caso não especificado.
        A diferença da soma das probabilidades das filas de saida eh a probabilidade de sair do sistema.
        Ex: fila1 com 50% e fila2 com 30%, somam 80% do total de probabilidade de irem para outra fila, sendo assim,
        20% de chance de o 'cliente' sair do sistema.
        """
        self.saida.append({
            "fila": fila,
            "prob": prob
        })

        # Deixa sempre ordenado em ordem crescente de probabilidade
        self.saida = sorted(self.saida, key=operator.itemgetter('prob'))

    def get_saida_da_fila(self, numeroAleatorio):
        probAcumulada = 0
        for filaSaida in self.saida:
            probAcumulada += filaSaida["prob"]
            if numeroAleatorio <= probAcumulada:
                return filaSaida["fila"]
        return None
    
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
            print("Estado:", estado, "Tempo:", int(tempoEstado), "Prob:", "%.2f" % ((tempoEstado / totalTime) * 100))
        
        print("Total", int(totalTime), "100%")

        return ""