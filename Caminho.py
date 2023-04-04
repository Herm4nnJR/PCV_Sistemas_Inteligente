import random as rd
import sys
import numpy as np
import copy

from Grafo import Grafo

class Caminho:
    def __init__(self, grafo = None,qntd_vizinhos_verif = None,qntd_nos_verif = None):
        self.distancia = 0
        self.caminho = []
        if qntd_vizinhos_verif == None:
            self.caminho_aleatorio(grafo)
        else:
            if qntd_nos_verif == None:
                self.caminho_mais_prox(grafo, qntd_vizinhos_verif)
            else:
                self.caminho_feixo(grafo, qntd_vizinhos_verif, qntd_nos_verif,self.caminho)

    def __str__(self):
        return f'Caminho({self.distancia,self.caminho})'

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
    
    def verifica_dist_parcial(self, grafo):
        dist = 0
        for i in range(0, len(self.caminho) - 1):
            dist = dist + grafo.matriz[self.caminho[i]][self.caminho[i+1]]
        return dist

    #funcao para um caminho completo
    def caminho_mais_prox(self, grafo, qntd_vizinhos_verif):
        nao_caminho = np.arange(grafo.vertices)
        caminho = []
        #sorteia no inicial
        no_atual = rd.randint(0,grafo.vertices-1)
        caminho.append(no_atual)
        nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == no_atual))
        while len(nao_caminho) > 0:
            no_mais_prox = -1
            for i in range(0,qntd_vizinhos_verif):
                prox_no = nao_caminho[rd.randint(0, qntd_vizinhos_verif-1)]
                if no_mais_prox == -1:
                    no_mais_prox = prox_no
                    #dist_atual = grafo[no_atual][no_mais_prox]
                elif grafo.matriz[no_atual][prox_no] < grafo.matriz[no_atual][no_mais_prox]:#dist_atual:
                    no_mais_prox = prox_no
            caminho.append(no_mais_prox)
            nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == no_mais_prox))
            no_atual = no_mais_prox
            if len(nao_caminho) <= qntd_vizinhos_verif:
                qntd_vizinhos_verif = len(nao_caminho)
        self.caminho = caminho
        self.distancia = self.verifica_dist(grafo)
    
    #funcao para caminhos parciais
    def caminho_feixo(self, grafo, qntd_vizinhos_verif, qntd_nos_verificados, caminho_parcial):
        nao_caminho = np.arange(grafo.vertices)
        tam_vetor = len(caminho_parcial)
        if tam_vetor == 0:
            no_atual = rd.randint(0,grafo.vertices-1)
            caminho_parcial.append(no_atual)
            nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == no_atual))
            qntd_nos_verificados = qntd_nos_verificados - 1
        else:
            for i in range(0, tam_vetor):
                nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == caminho_parcial[i]))
            no_atual = caminho_parcial[tam_vetor-1]
        for i in range(tam_vetor, tam_vetor + qntd_nos_verificados):
            no_mais_prox = -1
            for j in range(0,qntd_vizinhos_verif):
                prox_no = nao_caminho[rd.randint(0, len(nao_caminho)-1)]
                if no_mais_prox == -1:
                    no_mais_prox = prox_no
                    #dist_atual = grafo[no_atual][no_mais_prox]
                elif grafo.matriz[no_atual][prox_no] < grafo.matriz[no_atual][no_mais_prox]:#dist_atual:
                    no_mais_prox = prox_no
            caminho_parcial.append(no_mais_prox)
            nao_caminho = np.delete(nao_caminho, np.where(nao_caminho == no_mais_prox))
            no_atual = no_mais_prox
            if len(nao_caminho) <= qntd_nos_verificados:
                qntd_nos_verificados = len(nao_caminho)
            if len(nao_caminho) <= qntd_vizinhos_verif:
                qntd_vizinhos_verif = len(nao_caminho)
        self.caminho = caminho_parcial
        self.distancia = self.verifica_dist_parcial(grafo)
        
    def mutacao(self,grafo):
        no1 = rd.randint(0, grafo.vertices)
        no2 = rd.randint(0, grafo.vertices)
        while no1 == no2:
            no2 = rd.randint(0, grafo.vertices)
        noaux = self.caminho[no2]
        self.caminho[no2] = self.caminho[no1]
        self.caminho[no1] = noaux