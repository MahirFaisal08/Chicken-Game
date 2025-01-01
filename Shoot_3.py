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
from modules.stage3animate import stage3animate
from modules.straightline import draw_points
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18

class GameEngine:
    def setup_scene():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
        glMatrixMode(GL_MODELVIEW)

def render_world():
    GameEngine.setup_scene()
    
    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
    draw_chicken2()
    
    for weapon in config.missiles:
        weapon.draw()
        
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('c'))
    
    if config.chickenHealth <= 0:
        print("Target eliminated successfully!")
        config.pause = True
    
    for idx in range(len(config.centers) - 1, -1, -1):
        center_pos_x = config.centers[idx][0]
        center_pos_y = config.centers[idx][1]
        current_rad = config.radiuses[idx]
        
        point_data = draw_circle(
            center_pos_x, center_pos_y, 
            current_rad,
            config.boundary_x_min, 
            config.boundary_x_max,
            config.boundary_y_min,
            config.boundary_y_max
        )
        
        if point_data[0] is None:
            print(f'Current Points: {config.get_points()}')
            config.radiuses.pop(idx)
            config.centers.pop(idx)
        else:
            coord_x, coord_y = point_data
            for i in range(len(coord_x)):
                draw_points(coord_x[i], coord_y[i], 3)
    
    if config.create_new:
        new_pos_x, new_pos_y = config.create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(new_pos_x, new_pos_y)
        glEnd()
        
    if config.end:
        config.speed = 1
        glutLeaveMainLoop()
        
    glutSwapBuffers()

def initialize_graphics():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

def setup_game_window():
    glutInit()
    
    window_params = {
        'width': config.W_Width,
        'height': config.W_Height,
        'pos_x': 0,
        'pos_y': 0
    }
    
    glutInitWindowSize(window_params['width'], window_params['height'])
    glutInitWindowPosition(window_params['pos_x'], window_params['pos_y'])
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    
    return glutCreateWindow(b"Battle Simulation v1.0")

def main():
    game_window = setup_game_window()
    initialize_graphics()
    
    glutDisplayFunc(render_world)
    glutIdleFunc(stage3animate)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener_stage2)
    
    glutMainLoop()

if __name__ == "__main__":
    main()