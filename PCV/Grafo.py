import numpy as np

class Grafo:
    def __init__(self, arquivo):
        self.matriz = np.loadtxt(arquivo, delimiter=',')
        self.vertices = len(self.matriz[0])

    def criaCaminho(self, u, v, custo):
        self.grafo[u - 1].append([v, custo])

    def mostraGrafo(self):
        print(self.matriz)

    def printFile(self):
        file = open("Teste.txt", "a")
        for i in range(self.vertices):
            for j in self.grafo[i]:
                file.write(str(j), ",")
            file.write("\n")
        file.close

    def readFile(self, name="Teste.txt"):
        v = 0
        file = open(name, "r")
        for i in range(self.vertices):
            str = file.readline()
            for a in str.split(";"):
                v = 0
                for b in a.split(","):
                    if v == 0:
                        c = b
                    elif v == 1:
                        self.criaCaminho(i + 1, int(c), int(b))
                        v = 0
                    v = v + 1

