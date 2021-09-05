#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"


class Ponto:

    """
    Classe Ponto
    """

    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def imprime(self):
        """
        Imprime os valores de cada eixo do ponto
        """
        print (self.x, self.y, self.z)
