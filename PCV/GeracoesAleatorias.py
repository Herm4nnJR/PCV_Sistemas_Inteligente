from Caminho import Caminho
from Grafo import Grafo
from Populacao import Populacao
import time

inicio = time.time()

grafo = Grafo('.\matriz500.txt')
grafo.mostraGrafo()
tamanho_populacao = 250000
n_geracoes = 1
populacao = Populacao(tamanho_populacao, grafo)
populacao.show_caminhos()
print('\n')
populacao.rank()
populacao.show_caminhos()
for i in range(n_geracoes-1) :
    print('\n')
    populacao.novos_caminhos_aleatorio(tamanho_populacao,grafo)
    populacao.show_caminhos()
    print('\n')
    populacao.rank()
    populacao.show_caminhos()
print('\n')
populacao.melhor_caminho()

fim = time.time()
print(fim - inicio)