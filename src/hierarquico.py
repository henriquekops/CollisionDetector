#!/usr/bin/env python
#-*- coding: utf-8 -*-

# dependencias internas
from math import floor

# dependencias de codigo
from linha import Linha

__author__ = "Henrique Kops & Gabriel Castro"


class Celula:
    """
    Classe Celula
    """

    def __init__(self) -> None:
        self.linhas = []

class SubdivisaoRegular:

    """
    Classe SubdivisaoRegular
    """
    __MAX = 50

    def __init__(self, n:int, xDiv:int, yDiv:int) -> None:
        self.M = [[Celula() for _ in range(self.__MAX)]] * self.__MAX
        self.tamX = n / xDiv
        self.tamY = n / yDiv

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
                # if linha atravessa celula: cell.linhas.append(linha.index)
