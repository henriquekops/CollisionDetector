#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"

from ponto import Ponto
from random import randint as rand
from OpenGL.GL import (
    glBegin,
    GL_LINES,
    glVertex2f,
    glEnd
)


class Linha:

    """
    - Classe Linha
    """

    def __init__(self):
        self.p1 = Ponto()
        self.p2 = Ponto()

    def geraLinha(self, limite: int, tamMax: int):
        """
        - Gera uma linha com tamanho 'tamMax' dentro de um limite 'limite'.
        """
        # Geracao aleatoria para coordenadas de p1
        self.p1.x = (rand(0, limite)*10) / 10.0
        self.p1.y = (rand(0, limite)*10) / 10.0

        # Variacao entre p1 e p2 no intervalo [0;limite)
        deltaX = rand(0, limite) / limite
        deltaY = rand(0, limite) / limite

        # Geracao aleatoria para coordenada x de p2
        if (rand(0, 1) % 2):
            self.p2.x = self.p1.x + deltaX * tamMax
        else:
            self.p2.x = self.p1.x - deltaX * tamMax

        # Geracao aleatoria para coordenada y de p2
        if (rand(0, 2) % 2):
            self.p2.y = self.p1.y + deltaY * tamMax
        else:
            self.p2.y = self.p1.y - deltaY * tamMax

    def desenhaLinha(self):
        """
        - Desenha a linha na tela atual
        """
        glBegin(GL_LINES)
        
        glVertex2f(self.p1.x, self.p1.y)
        glVertex2f(self.p2.x, self.p2.y)

        glEnd()
