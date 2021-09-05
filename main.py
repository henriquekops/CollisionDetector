#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops & Gabriel Castro"
__credits__ = "Marcio Sarroglia Pinho"

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ponto import Ponto
from linha import Linha
from typing import Tuple
from aabb import AABB
import time

# Constantes
N_LINHAS = 50
MAX_X = 100
ESCAPE = b'\x1b'

# Variaveis globais
ContChamadas, ContadorInt, nFrames, TempoTotal, AccumDeltaT = 0, 0, 0, 0, 0
oldTime = time.time()
linhas = []
aabbs = []

def init() -> None:
    """
    - Inicializa os parâmetros globais de OpenGL
    """
    global linhas, aabbs

    # Define a cor do fundo da tela (BRANCO) 
    glClearColor(1.0, 1.0, 1.0, 1.0)
    
    linhas = [Linha() for _ in range(N_LINHAS)]

    for linha in linhas:
        linha.geraLinha(MAX_X, 10)

    # Gera os AABBs
    aabbs = [AABB(linha) for linha in linhas]


def reshape(w:int, h:int) -> None:
    """
    - Trata o redimensionamento da janela OpenGL
    """
    # Reseta coordenadas do sistema antes the modificala
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Define os limites lógicos da área OpenGL dentro da Janela
    glOrtho(0, 100, 0, 100, 0, 1)

    # Define a área a ser ocupada pela área OpenGL dentro da Janela
    glViewport(0, 0, w, h)

    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def intersec2d(k:Ponto, l:Ponto, m:Ponto, n:Ponto) -> Tuple[int, float, float]:
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


def HaInterseccao(k:Ponto, l:Ponto, m:Ponto, n:Ponto) -> bool:
    """
    - Detecta interseccao entre os pontos
    """
    ret, s, t = intersec2d( k,  l,  m,  n)

    if not ret: return False

    return s>=0.0 and s <=1.0 and t>=0.0 and t<=1.0


def DesenhaLinhas() -> None:
    """
    - Desenha as linhas na tela
    """
    global linhas

    glColor3f(0,1,0)

    for linha in linhas:
        linha.desenhaLinha()
    
    glColor3f(1,0,0)

    for aabb in aabbs:
        aabb.centro.desenhaPonto()


def DesenhaCenario() -> None:
    """
    - Desenha o cenario
    """
    global ContChamadas, ContadorInt

    ContChamadas, ContadorInt = 0, 0
    
    # Desenha as linhas do cenário
    glLineWidth(1)
    glColor3f(1,0,0)
    
    for i in range(N_LINHAS):
        PA = linhas[i].p1
        PB = linhas[i].p2

        for j in range(N_LINHAS):
            PC = linhas[j].p1
            PD = linhas[j].p2

            ContChamadas += 1

            if aabbs[i].colisao(aabbs[j]):
                if HaInterseccao(PA, PB, PC, PD):
                    ContadorInt += 1
                    linhas[i].desenhaLinha()
                    linhas[j].desenhaLinha()


def display() -> None:
    """
    - Funcao que exibe os desenhos na tela
    """
    # Limpa a tela com  a cor de fundo
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    DesenhaLinhas()
    DesenhaCenario()
    
    glutSwapBuffers()


def animate() -> None:
    """
    - Funcao chama enquanto o programa esta ocioso.
    Calcula o FPS e numero de interseccao detectadas, junto com outras informacoes.
    """
    global nFrames, TempoTotal, AccumDeltaT, oldTime

    nowTime = time.time()
    dt = nowTime - oldTime
    oldTime = nowTime

    AccumDeltaT += dt
    TempoTotal += dt
    nFrames += 1
    
    if AccumDeltaT > 1.0/30:  # fixa a atualização da tela em 30
        AccumDeltaT = 0
        glutPostRedisplay()

    if TempoTotal > 5.0:
        print(f'Tempo Acumulado: {TempoTotal} segundos.')
        print(f'Nros de Frames sem desenho: {int(nFrames)}')
        print(f'FPS(sem desenho): {int(nFrames/TempoTotal)}')
        
        TempoTotal = 0
        nFrames = 0
        
        print(f'Contador de Intersecoes Existentes: {ContadorInt/2.0}')
        print(f'Contador de Chamadas: {ContChamadas}')


def keyboard(*args) -> None:
    """
    - Valida inicializacao / finalizacao do programa
    """

    if args[0] == ESCAPE:   # Termina o programa qdo
        os._exit(0)         # a tecla ESC for pressionada

    if args[0] == b' ':
        init()

    # Força o redesenho da tela
    glutPostRedisplay()


def arrow_keys(a_keys:int, x:int, y:int) -> None:
    """
    - Valida a entrada de teclado
    """
    if a_keys == GLUT_KEY_UP:         # Se pressionar UP
        pass
    if a_keys == GLUT_KEY_DOWN:       # Se pressionar DOWN
        pass
    if a_keys == GLUT_KEY_LEFT:       # Se pressionar LEFT
        pass
    if a_keys == GLUT_KEY_RIGHT:      # Se pressionar RIGHT
        pass

    glutPostRedisplay()


def mouse(button: int, state:int, x:int, y:int) -> None:
    """
    - Redesenha caso o mouse esteja sobre a janela
    """
    glutPostRedisplay()


def mouseMove(x:int, y:int) -> None:
    """
    - Redesenha caso o mouse passe sobre a janela
    """
    glutPostRedisplay()


# Programa Principal
if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)

    # Define o tamanho inicial da janela grafica do programa
    glutInitWindowSize(650, 500)

    # Cria a janela na tela, definindo o nome da
    # que aparecera na barra de título da janela.
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Algorimos de Cálculo de Colisão")

    # executa algumas inicializações
    init ()

    # Define que o tratador de evento para
    # o redesenho da tela. A funcao "display"
    # será chamada automaticamente quando
    # for necessário redesenhar a janela
    glutDisplayFunc(display)
    glutIdleFunc (animate)

    # o redimensionamento da janela. A funcao "reshape"
    # Define que o tratador de evento para
    # será chamada automaticamente quando
    # o usuário alterar o tamanho da janela
    glutReshapeFunc(reshape)

    # Define que o tratador de evento para
    # as teclas. A funcao "keyboard"
    # será chamada automaticamente sempre
    # o usuário pressionar uma tecla comum
    glutKeyboardFunc(keyboard)
        
    # Define que o tratador de evento para
    # as teclas especiais(F1, F2,... ALT-A,
    # ALT-B, Teclas de Seta, ...).
    # A funcao "arrow_keys" será chamada
    # automaticamente sempre o usuário
    # pressionar uma tecla especial
    glutSpecialFunc(arrow_keys)

    #glutMouseFunc(mouse)
    #glutMotionFunc(mouseMove)

    try:
        # inicia o tratamento dos eventos
        glutMainLoop()
    except SystemExit:
        pass
