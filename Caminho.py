import random as rd
import sys
import numpy as np

from Grafo import Grafo

class Caminho:
    def __init__(self, grafo,qntd_nos_verificados = None):
        self.distancia = 0
        self.caminho = []
        if qntd_nos_verificados == None:
            self.caminho_aleatorio(grafo)
        else:
            self.caminho_mais_prox(grafo, qntd_nos_verificados)

    def caminho_aleatorio(self, grafo):
        nos = list(range(grafo.vertices))
        rd.shuffle(nos) #embaralha os nós

        #cria um caminho, totalmente aleatório
        caminho = []
        for no in nos:
            if no not in caminho:
                caminho.append(no)
        self.caminho = caminho
        self.distancia = self.verifica_dist(grafo)
    
    def verifica_dist(self, grafo):
        dist = 0
        for i in range(0, len(self.caminho) - 2) :
            dist = dist + grafo.matriz[self.caminho[i]][self.caminho[i+1]]
        dist = dist + grafo.matriz[self.caminho[len(self.caminho) - 1]][self.caminho[0]]
        return dist

    def caminho_mais_prox(self, grafo, qntd_nos_verificados):
        nao_caminho = np.arange(grafo.vertices)
        caminho = []
        #sorteia no inicial
        no_atual = rd.randint(0,grafo.vertices-1)
        caminho.append(no_atual)
        nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == no_atual))
        while len(nao_caminho) > 0:
            no_mais_prox = -1
            for i in range(0,qntd_nos_verificados):
                prox_no = nao_caminho[rd.randint(0, qntd_nos_verificados-1)]
                if no_mais_prox == -1:
                    no_mais_prox = prox_no
                    #dist_atual = grafo[no_atual][no_mais_prox]
                elif grafo.matriz[no_atual][prox_no] < grafo.matriz[no_atual][no_mais_prox]:#dist_atual:
                    no_mais_prox = prox_no
            caminho.append(no_mais_prox)
            nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == no_mais_prox))
            no_atual = no_mais_prox
            if len(nao_caminho) <= qntd_nos_verificados:
                qntd_nos_verificados = len(nao_caminho)
        self.caminho = caminho
        self.distancia = self.verifica_dist(grafo)
        
        #def cruzamento