class GeradorDeNumerosAleatorios:
    m = 100_000_000
    qtdNumerosGerados = 0
    a = 37291
    c = 12938

    def __init__(self, seed, qtdNumeros):
        self.seed = seed
        self.x = seed

        self.qtdMaxNumeros = qtdNumeros

    def __cacular_proximo_numero_linear_congruente(self):
        return (self.a * self.x + self.c) % self.m

    def gerar_proximo_numero_aleatorio(self):
        self.x = self.__cacular_proximo_numero_linear_congruente()
        self.qtdNumerosGerados += 1
        return self.x / self.m

    def ha_numero_para_gerar(self):
        return self.qtdNumerosGerados < self.qtdMaxNumeros