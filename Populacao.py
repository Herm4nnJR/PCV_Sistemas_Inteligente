from Caminho import Caminho
from Grafo import Grafo
import numpy as np
import random as rd
import copy

class Populacao:
    def __init__(self, tam_populacao, grafo,qntd_vizinhos_verif=None, qntd_nos_verif=None):
        self.caminhos = []
        self.gerar_pop_inicial(tam_populacao, grafo, qntd_vizinhos_verif,qntd_nos_verif)
    
    def get_tam_cam(self):
        return len(self.caminhos[0].caminho)
        
    def gerar_pop_inicial(self, tam_populacao, grafo, qntd_vizinhos_verif,qntd_nos_verif):
        for i in range(tam_populacao):
            caminho_ini = Caminho(grafo, qntd_vizinhos_verif, qntd_nos_verif)
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
    
    def novos_caminhos_mais_prox(self,tam_populacao,grafo,qntd_vizinhos_verif):
        #não mexer no melhor caminho
        self.caminho[tam_populacao] = self.caminho[0]
        for i in range(0,tam_populacao-1):
            self.caminhos[i] = Caminho(grafo,qntd_vizinhos_verif)
            
    def novos_caminhos_feixo(self,tam_populacao, grafo, qntd_vizinhos_verif,qntd_nos_verif):
        #iniciar a partir do melhor caminho atual
        caminho_atual =[]
        for i in range(0, len(self.caminhos[0].caminho)):
            caminho_atual.append(self.caminhos[0].caminho[i])
        for i in range(0,tam_populacao):
            self.caminhos[i].caminho_feixo(grafo, qntd_vizinhos_verif, qntd_nos_verif, caminho_atual.copy())

    def melhor_caminho(self):
        print(self.caminhos[0].caminho)
        print('\n')
        print(self.caminhos[0].distancia)

    #funcao para cruzar os 2 melhores caminhos e ajustar o segundo
    def cruzamento(self,caminho1,caminho2, grafo):
        porcentagem = rd.randint(40,70)/100
        inicio1 = rd.randint(0,grafo.vertices-1)
        inicio2 = rd.randint(0,grafo.vertices-1)
        novocaminho = []
        nosvisitados = []
        naovisitados = np.arange(grafo.vertices)
        for i in range(0, grafo.vertices-1):
            if inicio1//grafo.vertices < porcentagem*grafo.vertices-1:
                novocaminho[i] = caminho1[inicio1//grafo.vertices]
                inicio1 += inicio1
                nosvisitados[i] = novocaminho[i]
                naovisitados = np.delete(naovisitados,novocaminho[i])
            else:
                novocaminho[i] = caminho2[inicio2//grafo.vertices]
                inicio2 += inicio2
        for i in range(porcentagem*grafo.vertices-1,grafo.vertices - 1):
            if novocaminho[i] in naovisitados:
                nosvisitados.append(novocaminho[i])
                naovisitados = np.delete(naovisitados,novocaminho[i])
            else:
                sorteado = rd.randint(0,len(naovisitados) - 1)
                novocaminho[i] = naovisitados[sorteado]
                naovisitados = np.delete(naovisitados,novocaminho[i])
        return novocaminho
    
    #def selecao_cruz_rank(self):
        