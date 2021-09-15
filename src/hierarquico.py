#!/usr/bin/env python
#-*- coding: utf-8 -*-

# dependencias internas
from math import floor

# dependencias de codigo
from linha import Linha
from ponto import Ponto
from validador import Interseccao

__author__ = "Henrique Kops & Gabriel Castro"


class Celula:
    """
    Classe Celula
    """

    def __init__(self, p1:Ponto, p2:Ponto, p3:Ponto, p4:Ponto) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.linhas = []

    def testaInterseccao(self, linha:Linha):
        # Retas: (p1, p2) (p2, p3) (p3, p4) (p4, p1)
        return Interseccao.valida(self.p1, self.p2, linha.p1, linha.p2) or \
            Interseccao.valida(self.p2, self.p3, linha.p1, linha.p2) or \
            Interseccao.valida(self.p3, self.p4, linha.p1, linha.p2) or \
            Interseccao.valida(self.p4, self.p1, linha.p1, linha.p2)


class SubdivisaoRegular:

    """
    Classe SubdivisaoRegular
    """
    __MAX = 50

    def __init__(self, n:int, xDiv:int, yDiv:int) -> None:
        self.tamX = n / xDiv
        self.tamY = n / yDiv
        self.M = [[]]
    
    def geraUniverso(self):
        # TODO: como atribuir os pontos?
        for i in range(1, self.__MAX+1):
            for j in range(1, self.__MAX+1):
                p = Ponto(x=(self.tamX*i), y=(self.tamY*j))
                #self.M[i][j] = Celula(p...)

    def envelope(self, linha:Linha):
        pMin = linha.pontoMin()
        pMax = linha.pontoMax()

        minX = floor(pMin.x/self.tamX)
        minY = floor(pMin.y/self.tamY)
        maxX = floor(pMax.x/self.tamX)
        maxY = floor(pMax.x/self.tamY)

        for i in range(minX, maxX):
            for j in range(minY, maxY):
                cell = self.M[i][j]
                if cell.testaInterseccao(linha):
                    cell.linhas.append(linha.idx)
