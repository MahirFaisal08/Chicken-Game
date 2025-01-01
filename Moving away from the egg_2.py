import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.stage1animate import stage1animate
from modules.listeners import keyboardListener, mouseListener_stage2
from modules.listeners import mouseListener_stage1
from modules.listeners import specialKeyListener
import math
from modules.playPauseX import draw_pause, draw_play, draw_x
from modules.shapes import draw_boat, draw_bucket, draw_chicken2, draw_circle, draw_diamond
from modules.config import config
from modules.stage2animate import stage2animate
from modules.straightline import draw_points

def graphics_update():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    camera_z = 200
    gluLookAt(0, 0, camera_z, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    
    update_controls()
    update_entities()
    update_circle_system()
    update_marker()
    
    if config.end:
        config.speed = 1
        glutLeaveMainLoop()
    
    glutSwapBuffers()

def update_controls():
    draw_x()
    draw_pause()
    draw_play()

def update_entities():
    draw_diamond()
    draw_boat()
    draw_chicken2()

def update_circle_system():
    for pos in range(len(config.centers) - 1, -1, -1):
        circle_x = config.centers[pos][0]
        circle_y = config.centers[pos][1]
        size = config.radiuses[pos]
        
        circle_data = draw_circle(
            circle_x, circle_y, size,
            config.boundary_x_min, config.boundary_x_max,
            config.boundary_y_min, config.boundary_y_max
        )
        
        if circle_data[0] is None:
            print(f'Points: {config.get_points()}')
            config.radiuses.pop(pos)
            config.centers.pop(pos)
        else:
            pos_x, pos_y = circle_data
            for i in range(len(pos_x)):
                draw_points(pos_x[i], pos_y[i], 3)

def update_marker():
    if config.create_new:
        marker_x, marker_y = config.create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(marker_x, marker_y)
        glEnd()

def setup_graphics():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

def init_window():
    glutInit()
    display_settings = {
        'dimensions': (config.W_Width, config.W_Height),
        'location': (0, 0),
        'display_flags': (GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    }
    
    glutInitWindowSize(*display_settings['dimensions'])
    glutInitWindowPosition(*display_settings['location'])
    glutInitDisplayMode(display_settings['display_flags'])
    
    return glutCreateWindow(b"Visual Simulation Environment")

def run_game():
    app_window = init_window()
    setup_graphics()
    
    glutDisplayFunc(graphics_update)
    glutIdleFunc(stage2animate)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener_stage2)
    
    glutMainLoop()

if __name__ == "__main__":
    run_game()