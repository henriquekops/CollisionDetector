#!/usr/bin/env python
#-*- coding: utf-8 -*-

# dependencias internas
from typing import Tuple

# dependencias de codigo
from ponto import Ponto

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


class Interseccao:

    @staticmethod
    def __intersec2d(k:Ponto, l:Ponto, m:Ponto, n:Ponto) -> Tuple[int, float, float]:
        """
        - Calcula a interseccao entre 2 retas (no plano 'XY' Z = 0)
        - Params:
            - k: ponto inicial da reta 1
            - l: ponto final da reta 1
            - m: ponto inicial da reta 2
            - n: ponto final da reta 2
        - Returns:
            - 0, se não houver interseccao ou 1, caso haja
            - int, valor do parâmetro no ponto de interseção (sobre a reta KL)
            - int, valor do parâmetro no ponto de interseção (sobre a reta MN)
        """
        det = (n.x - m.x) * (l.y - k.y)  -  (n.y - m.y) * (l.x - k.x)

        if (det == 0.0):
            return 0, None, None # não há intersecção

        s = ((n.x - m.x) * (m.y - k.y) - (n.y - m.y) * (m.x - k.x))/ det
        t = ((l.x - k.x) * (m.y - k.y) - (l.y - k.y) * (m.x - k.x))/ det

        return 1, s, t # há intersecção

    @classmethod
    def valida(cls, k:Ponto, l:Ponto, m:Ponto, n:Ponto) -> bool:
        """
        - Detecta interseccao entre os pontos
        """
        ret, s, t = cls.intersec2d( k,  l,  m,  n)

        if not ret: return False

        return s>=0.0 and s <=1.0 and t>=0.0 and t<=1.0
