#!/usr/bin/env python
#-*- coding: utf-8 -*-

# dependencias internas
from __future__ import annotations

# dependencias de codigo
from src.ponto import Ponto
from src.linha import Linha

__author__ = "Henrique Kops & Gabriel Castro"


class AABB:

    """
    - Classe AABB
    """

    def __init__(self, linha:Linha) -> None:
        self.metadeX = (linha.p2.x - linha.p1.x) / 2
        self.metadeY = (linha.p2.y - linha.p1.y) / 2
        self.centro = Ponto(x=(linha.p1.x + self.metadeX), y=(linha.p1.y + self.metadeY))

    def __distanciaX(self, aabb:AABB) -> float:
        """
        - Calcula a distancia das coordenadas X dos centros das AABBs
        """
        return abs(aabb.centro.x - self.centro.x)

    def __distanciaY(self, aabb:AABB) -> float:
        """
        - Calcula a distancia das coordenadas Y dos centros das AABBs
        """
        return abs(aabb.centro.y - self.centro.y)

    def __somaMetadesX(self, aabb:AABB) -> float:
        """
        - Soma as metades das linhas horizontais das AABBs
        """
        return abs(aabb.metadeX) + abs(self.metadeX)

    def __somaMetadesY(self, aabb:AABB) -> float:
        """
        - Soma as metades das linhas verticais das AABBs
        """
        return abs(aabb.metadeY) + abs(self.metadeY)

    def colisao(self, aabb:AABB) -> bool:
        """
        - Verifica a colisao entre as AABBs
        """
        return (self.__distanciaX(aabb) < self.__somaMetadesX(aabb)) and (self.__distanciaY(aabb) < self.__somaMetadesY(aabb))
