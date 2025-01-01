import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.stage1animate import stage1animate
from modules.listeners import keyboardListener
from modules.listeners import mouseListener_stage1
from modules.listeners import specialKeyListener
import math
from modules.playPauseX import draw_pause, draw_play, draw_x
from modules.shapes import draw_boat, draw_bucket, draw_chicken2, draw_diamond, draw_basket
from modules.config import config
from modules.straightline import draw_any_line, draw_circle2, draw_points

def generate_arc(mid_x, mid_y, size):
    curr_x = size
    curr_y = 0
    decision_param = 1 - size

    x_vals = []
    y_vals = []

    x_vals.append(curr_x + mid_x)
    y_vals.append(curr_y + mid_y)

    while curr_x >= curr_y:
        curr_y += 1

        if decision_param < 0:
            decision_param += 2 * curr_y + 1
        else:
            curr_x -= 1
            decision_param += 2 * (curr_y - curr_x) + 1

        if curr_y <= curr_x:
            x_vals.append(curr_x + mid_x)
            y_vals.append(curr_y + mid_y)
            x_vals.append(-curr_x + mid_x)
            y_vals.append(curr_y + mid_y)
            x_vals.append(curr_y + mid_x)
            y_vals.append(curr_x + mid_y)
            x_vals.append(-curr_y + mid_x)
            y_vals.append(curr_x + mid_y)

    for i in range(len(x_vals)):
        draw_points(x_vals[i], y_vals[i], 1)

def create_container(start_x, start_y, container_width, container_height):
    rim_size = container_height / 10
    body_size = container_height - 2 * rim_size

    total_w = container_width
    total_h = container_height
    handle_size = total_w // 2

    handle_x = total_w // 2
    handle_y = total_h + handle_size

    generate_arc(handle_x + start_x, handle_y - 2, handle_size)
    generate_arc(handle_x + start_x, handle_y - 2, handle_size - 10)

    top_y = start_y + container_height - rim_size
    draw_any_line(start_x, top_y, start_x + container_width, top_y)

    bottom_y = start_y + rim_size
    draw_any_line(start_x, bottom_y, start_x + container_width, bottom_y)

    draw_any_line(start_x, bottom_y, start_x, top_y)
    draw_any_line(start_x + container_width, bottom_y, start_x + container_width, top_y)

    weave_count = 5
    weave_gap = body_size / weave_count
    for i in range(weave_count):
        y_pos = bottom_y + i * weave_gap
        draw_any_line(start_x, y_pos, start_x + container_width, y_pos)

    vert_weaves = 7
    vert_gap = container_width / vert_weaves
    for i in range(vert_weaves):
        x_pos = start_x + i * vert_gap
        draw_any_line(x_pos, bottom_y, x_pos, top_y)

def show_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
    draw_chicken2()

    if (config.create_new):
        x_coord, y_coord = config.create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(x_coord, y_coord)
        glEnd()
    if (config.end):
        config.speed = 1
        glutLeaveMainLoop()
    glutSwapBuffers()

def initialize():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(config.W_Width, config.W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

game_window = glutCreateWindow(b"OpenGL Coding Practice")
initialize()

glutDisplayFunc(show_scene)
glutIdleFunc(stage1animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener_stage1)

glutMainLoop()