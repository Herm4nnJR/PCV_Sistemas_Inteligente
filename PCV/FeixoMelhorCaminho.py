from Caminho import Caminho
from Grafo import Grafo
from Populacao import Populacao
import time

inicio = time.time()

grafo = Grafo('.\matriz500.txt')
grafo.mostraGrafo()
tamanho_populacao = 50
vizinhos_visitados = 50
nos_por_vez = 25
populacao = Populacao(tamanho_populacao, grafo, vizinhos_visitados, nos_por_vez)
populacao.show_caminhos()
print('\n')
populacao.rank()
populacao.show_caminhos()
while (populacao.get_tam_cam() < grafo.vertices) :
    print('\n')
    populacao.novos_caminhos_feixo(tamanho_populacao,grafo,vizinhos_visitados, nos_por_vez)
    populacao.show_caminhos()
    print('\n')
    populacao.rank()
    populacao.show_caminhos()
print('\n')
populacao.melhor_caminho()

fim = time.time()
print(fim - inicio)