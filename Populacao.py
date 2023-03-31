from Caminho import Caminho
from Grafo import Grafo

class Populacao:
    def __init__(self, tam_populacao, grafo,qntd_nos_verificados=None):
        self.caminhos = []
        self.gerar_pop_inicial(tam_populacao, grafo, qntd_nos_verificados)
        
    def gerar_pop_inicial(self, tam_populacao, grafo, qntd_nos_verificados):
        for i in range(tam_populacao):
            caminho_ini = Caminho(grafo, qntd_nos_verificados)
            self.caminhos.append(caminho_ini)
    
    def show_caminhos(self):
        for i in range(len(self.caminhos)):
            print(self.caminhos[i].caminho, self.caminhos[i].distancia)

    def rank(self):
        caminhos_rank = sorted(self.caminhos, key=lambda x: x.distancia)
        self.caminhos = caminhos_rank

    def novos_caminhos_aleatorio(self,tam_populacao,grafo):
        #não mexer no melhor caminho
        for i in range(1,tam_populacao-1):
            self.caminhos[i] = Caminho(grafo)
    
    def novos_caminhos_mais_prox(self,tam_populacao,grafo,qntd_nos_verificados):
        #não mexer no melhor caminho
        for i in range(1,tam_populacao-1):
            self.caminhos[i] = Caminho(grafo,qntd_nos_verificados)

    def melhor_caminho(self):
        print(self.caminhos[0].caminho)
        print('\n')
        print(self.caminhos[0].distancia)

    #def cruzamento(self,caminho1,caminho2):
        