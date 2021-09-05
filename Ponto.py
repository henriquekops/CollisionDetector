#!/usr/bin/env python
#-*- coding: utf-8 -*-

from OpenGL.GL import (
    glBegin,
    GL_POINTS,
    glVertex2f,
    glEnd
)
from OpenGL.GL.exceptional import glVertex


__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


class Ponto:

    """
    Classe Ponto
    """

    def __init__(self, x:float=0, y:float=0) -> None:
        self.x = x
        self.y = y

    def desenhaPonto(self) -> None:
        """
        Desenha o ponto
        """
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()
    
    def imprime(self) -> None:
        """
        Imprime os valores de cada eixo do ponto
        """
        print (self.x, self.y, self.z)
