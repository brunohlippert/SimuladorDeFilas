# Simulador de filas

Este código contém um simulador de filas utilizando números pseudo aleatórios.

## Executando
### Gerador de números pseudo aleatórios
Para instanciar o gerador de números pseudo aleatórios utilize o seguinte formato, passando uma seed e a quantidade de números a serem gerados.
```
gerador = GeradorDeNumerosAleatorios(current_milli_time(), 100_000)
```

### Fila
Para definir as propriedades da fila abra o arquivo ```SimuladorDeFilas.py``` e defina as propriedades da fila conforme o exemplo a baixo
```
fila = Fila(intervaloChegada=(2,4),
            intervalorAtendimento=(3,5),
            nServidores=2,
            capacidade=5,
            chegadaPrimeiro=3.0)
```

É possível não usar os atributos ```intervaloChegada``` e ```chegadaPrimeiro``` caso a chegada da fila seja a saída de outra, para definir este comportamento, defina a segunda fila como abaixo.

```
fila2 = Fila(intervalorAtendimento=(3,5),
            nServidores=1,
            capacidade=3)
```

e adicione a ```fila2``` como sendo a saída da primeira, como abaixo.
```
fila1.filaDeSaida = fila2
```

### Escalonador
O escalonador é responsável pela execução do algoritmo, para instancialo é necessário passar o gerador de números pseudo aleatórios e uma lista de filas a serem simuladas. Em seguida, chamar o método ```inicializar_simulacao```, como no exemplo a baixo.
```
listaDeFilas = [fila]

escalonador = Escalonador(gerador, listaDeFilas)
escalonador.inicializar_simulacao()
```

### Observando resultados
Para observar o resultado da simulação, basta realizar o comando ```print``` em uma fila, conforme o exemplo a baixo.
```
print(fila)
```

O resultado será uma análise de cada estado da fila durante a simulação, contendo o tempo que a fila passou em determinado estado e a probabilidade de a fila se encontrar neste estado, conforme o exemplo a baixo.

```
Estado: 0 Tempo: 2087.7573 Prob: 1.39
Estado: 1 Tempo: 95625.4643 Prob: 63.80
Estado: 2 Tempo: 51913.1269 Prob: 34.63
Estado: 3 Tempo: 267.8216 Prob: 0.18
Total 149894.1702 100%
```

### Executando o simulador
Após as definir os itens anteriores, basta executar o seguinte comando para rodar o simulador.
``` python3 SimuladorDeFilas.py ```

Observação: este simulador foi desenvolvido em Python3, não tendo nenhuma garantia de funcionar em versões anteriores.