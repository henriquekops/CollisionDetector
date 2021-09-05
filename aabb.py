#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops & Gabriel Castro"

from __future__ import annotations
from ponto import Ponto
from linha import Linha
from math import (
    sqrt,
    pow
)


class AABB:

    """
    - Classe AABB
    """

    def __init__(self, linha:Linha) -> None:
        self.metadeX = (linha.p2.x - linha.p1.x) / 2
        self.metadeY = (linha.p2.y - linha.p1.y) / 2
        self.centro = Ponto(self.metadeX, self.metadeY)

    def __distanciaEuclidiana(self, aabb:AABB):
        """
        - Calcula a distancia euclidiana entre os centros das AABBs
        """
        deltaX = aabb.centro.x - self.centro.x
        deltaY = aabb.centro.y - self.centro.y
        return sqrt(pow(deltaX) + pow(deltaY))
    
    def __somaMetadesX(self, aabb:AABB):
        """
        - Soma as metades das linhas horizontais das AABBs
        """
        return aabb.metadeX + self.metadeX

    def __somaMetadesY(self, aabb:AABB):
        """
        - Soma as metades das linhas verticais das AABBs
        """
        return aabb.metadeY + self.metadeY

    def colisao(self, aabb:AABB) -> bool:
        """
        - Verifica a colisao entre as AABBs
        """
        return (
            self.__distanciaEuclidiana(aabb) < self.__somaMetadesX(aabb) and
            self.__distanciaEuclidiana(aabb) < self.__somaMetadesY(aabb)
        )
