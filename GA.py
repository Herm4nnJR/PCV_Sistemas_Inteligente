from Caminho import Caminho
from Grafo import Grafo
from Populacao import Populacao

grafo = Grafo('.\PCV\matriz500.txt')
grafo.mostraGrafo()
tamanho_populacao = 9
n_geracoes = 10
visinhos_visitados = 5
populacao = Populacao(tamanho_populacao, grafo, visinhos_visitados)
populacao.show_caminhos()
print('\n')
populacao.rank()
populacao.show_caminhos()
for i in range(n_geracoes-1) :
    print('\n')
    populacao.novos_caminhos_mais_prox(tamanho_populacao,grafo,visinhos_visitados)
    populacao.show_caminhos()
    print('\n')
    populacao.rank()
    populacao.show_caminhos()
print('\n')
populacao.melhor_caminho()