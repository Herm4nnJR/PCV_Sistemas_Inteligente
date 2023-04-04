from Caminho import Caminho
from Grafo import Grafo
from Populacao import Populacao

grafo = Grafo('.\matriz500.txt')
grafo.mostraGrafo()
tamanho_populacao = 50
visinhos_visitados = 10
nos_por_vez = 10
populacao = Populacao(tamanho_populacao, grafo, visinhos_visitados, nos_por_vez)
populacao.show_caminhos()
print('\n')
populacao.rank()
populacao.show_caminhos()
while (populacao.get_tam_cam() < grafo.vertices) :
    print('\n')
    populacao.novos_caminhos_feixo(tamanho_populacao,grafo,visinhos_visitados, nos_por_vez)
    populacao.show_caminhos()
    print('\n')
    populacao.rank()
    populacao.show_caminhos()
print('\n')
populacao.melhor_caminho()