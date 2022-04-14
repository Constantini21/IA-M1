# :.:.: N-Queens :.:.:

### O problema
N-Queens é um problema popular de IA destinado a mostrar a eficiência de diferentes algoritmos. O problema é colocar N rainhas, que podem atacar outras rainhas verticalmente, horizontalmente ou diagonalmente de sua posição, em um tabuleiro NxN onde nenhuma das rainhas pode atacar outra.

### Algoritmo:
HillClimbingRandom: Modifica um único tabuleiro até que sua função heurística (o número de pares de rainhas que podem se atacar) retorne 0. Modifica o tabuleiro para um das casas adjacentes com o menor valor da função heurística. Se não houver valor mais baixo, ele se desvia para outras casas aleatórias para tentar encontrar uma. Depois de X passos, ele criará outro quadro e tentará o mesmo processo.

### Execultar programa
```bash
python run.py 8
```