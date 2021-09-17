#!/usr/bin/env python
#-*- coding: utf-8 -*-

# dependencias internas
from math import floor

# dependencias de codigo
from src.linha import Linha
from src.ponto import Ponto
from src.validador import Interseccao

__author__ = "Henrique Kops & Gabriel Castro"


class Celula:
    """
    Sub-Classe Celula
    """

    def __init__(self, pRef:Ponto, tamX:float, tamY:float) -> None:
        self.p1 = pRef
        self.p2 = Ponto(pRef.x, pRef.y+tamY)
        self.p3 = Ponto(pRef.x+tamX, pRef.y+tamY)
        self.p4 = Ponto(pRef.x+tamX, pRef.y)
        self.contem = False
        self.linhas = []

    def testaInterseccao(self, linha:Linha):
        """
        Testa a interseccao das linhas da celula com a linha em questao a partir
        de um ponto de referencia
        """
        return Interseccao.valida(self.p1, self.p2, linha.p1, linha.p2) or \
            Interseccao.valida(self.p2, self.p3, linha.p1, linha.p2) or \
            Interseccao.valida(self.p3, self.p4, linha.p1, linha.p2) or \
            Interseccao.valida(self.p4, self.p1, linha.p1, linha.p2)


class SubdivisaoRegular:

    """
    Classe SubdivisaoRegular
    """

    def __init__(self, n:int, xDiv:int, yDiv:int) -> None:
        self.N = n
        self.M = [[None for _ in range(self.N)] for _ in range(self.N)]
        self.tamX = self.N / xDiv
        self.tamY = self.N / yDiv
    
    def geraMatriz(self):
        """
        Gera a matriz de Celulas NxN
        """
        for i in range(self.N):
            for j in range(self.N):
                pRef=Ponto(x=(self.tamX*(i)), y=(self.tamY*(j)))
                self.M[i][j] = Celula(pRef, self.tamX, self.tamY)

    def envelope(self, linha:Linha):
        """
        Calcula o envelope da linha em questao
        """
        pMin = linha.pontoMin()
        pMax = linha.pontoMax()

        minX = floor(pMin.x/self.tamX)
        minY = floor(pMin.y/self.tamY)
        maxX = floor(pMax.x/self.tamX)
        maxY = floor(pMax.y/self.tamY)

        if (minX == maxX) and (minY == maxY):
            celula = self.M[minX][minY]
            celula.contem = True
        else:
            for i in range(minX, maxX+1):
                for j in range(minY, maxY+1):

                    celula = self.M[i][j]
                    if celula.testaInterseccao(linha):
                        celula.linhas.append(linha.idx)
                        celula.contem = True
