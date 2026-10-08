from vpython import box, color, vector, scene, rate
import numpy as np

cube = np.zeros((6, 3, 3), dtype=str)

cube[0,:,:] = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
cube[1,:,:] = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
cube[2,:,:] = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]   
cube[3,:,:] = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
cube[4,:,:] = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
cube[5,:,:] = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]

COLOR_MAP = {
    'W': vector(1, 1, 1),
    'Y': vector(1, 1, 0),
    'G': vector(0, 0.8, 0.2),
    'R': vector(0, 0.4, 1),
    'B': vector(0.9, 0.1, 0.1),
    'O': vector(1, 0.4, 0)
}

scene.title = "Rubik's Cube 3D | Press Keys: [U] Up, [D] Down, [L] Left, [R] Right | Hold [Shift] for Layer 2"
scene.background = vector(0.12, 0.12, 0.12)
scene.width = 900
scene.height = 700

stickers = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}}

def init_3d_cube():
    for x in range(3):
        for y in range(3):
            for z in range(3):
                box(pos=vector(x - 1, y - 1, z - 1), size=vector(0.96, 0.96, 0.96), color=vector(0.08, 0.08, 0.08))

    for r in range(3):
        for c in range(3):
            stickers[0][(r, c)] = box(pos=vector(c - 1, 1.49, 1 - r), size=vector(0.85, 0.02, 0.85))

    for r in range(3):
        for c in range(3):
            stickers[5][(r, c)] = box(pos=vector(c - 1, -1.49, r - 1), size=vector(0.85, 0.02, 0.85))

    for r in range(3):
        for c in range(3):
            stickers[2][(r, c)] = box(pos=vector(c - 1, 1 - r, 1.49), size=vector(0.85, 0.85, 0.02))

    for r in range(3):
        for c in range(3):
            stickers[3][(r, c)] = box(pos=vector(1 - c, 1 - r, -1.49), size=vector(0.85, 0.85, 0.02))

    for r in range(3):
        for c in range(3):
            stickers[1][(r, c)] = box(pos=vector(1.49, 1 - r, 1 - c), size=vector(0.02, 0.85, 0.85))

    for r in range(3):
        for c in range(3):
            stickers[4][(r, c)] = box(pos=vector(-1.49, 1 - r, c - 1), size=vector(0.02, 0.85, 0.85))

def update_3d_cube(cube):
    for face in range(6):
        for r in range(3):
            for c in range(3):
                stickers[face][(r, c)].color = COLOR_MAP[cube[face, r, c]]

def rotate_up(cube, c, F):
    if c not in (0, 2):
        return cube
    if(F == 'W'):
        for i in range(3):
            temp = cube[0, i, c]
            cube[0, i, c] = cube[4, i, c]
            cube[4, i, c] = cube[5, i, c]
            cube[5, i, c] = cube[2, i, c]
            cube[2, i, c] = temp
        if(c == 0):
            temp = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 2, 2]
            cube[3, 2, 2] = cube[3, 2, 0]
            cube[3, 2, 0] = temp
            temp_s = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 2, 1]
            cube[3, 2, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 2, 0]
            cube[1, 2, 0] = cube[1, 2, 2]
            cube[1, 2, 2] = temp
            temp_s = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = cube[1, 2, 1]
            cube[1, 2, 1] = temp_s
    elif(F == 'R'):
        for i in range(3):
            temp = cube[1, i, c]
            cube[1, i, c] = cube[5, i, c]
            cube[5, i, c] = cube[3, i, c]
            cube[3, i, c] = cube[0, i, c]
            cube[0, i, c] = temp
        if(c == 0):
            temp = cube[4, 0, 0]
            cube[4, 0, 0] = cube[4, 0, 2]
            cube[4, 0, 2] = cube[4, 2, 2]
            cube[4, 2, 2] = cube[4, 2, 0]
            cube[4, 2, 0] = temp
            temp_s = cube[4, 0, 1]
            cube[4, 0, 1] = cube[4, 1, 2]
            cube[4, 1, 2] = cube[4, 2, 1]
            cube[4, 2, 1] = cube[4, 1, 0]
            cube[4, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[2, 0, 2]
            cube[2, 0, 2] = cube[2, 0, 0]
            cube[2, 0, 0] = cube[2, 2, 0]
            cube[2, 2, 0] = cube[2, 2, 2]
            cube[2, 2, 2] = temp
            temp_s = cube[2, 1, 2]
            cube[2, 1, 2] = cube[2, 0, 1]
            cube[2, 0, 1] = cube[2, 1, 0]
            cube[2, 1, 0] = cube[2, 2, 1]
            cube[2, 2, 1] = temp_s
    elif(F == 'B'):
        for i in range(3):
            temp = cube[2, i, c]
            cube[2, i, c] = cube[5, i, c]
            cube[5, i, c] = cube[4, i, c]
            cube[4, i, c] = cube[0, i, c]
            cube[0, i, c] = temp
        if(c == 0):
            temp = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 2, 2]
            cube[1, 2, 2] = cube[1, 2, 0]
            cube[1, 2, 0] = temp
            temp_s = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 2, 1]
            cube[1, 2, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 2, 0]
            cube[3, 2, 0] = cube[3, 2, 2]
            cube[3, 2, 2] = temp
            temp_s = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = cube[3, 2, 1]
            cube[3, 2, 1] = temp_s
    elif(F == 'G'):
        for i in range(3):
            temp = cube[4, i, c]
            cube[4, i, c] = cube[5, i, c]
            cube[5, i, c] = cube[2, i, c]
            cube[2, i, c] = cube[0, i, c]
            cube[0, i, c] = temp
        if(c == 0):
            temp = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 2, 2]
            cube[3, 2, 2] = cube[3, 2, 0]
            cube[3, 2, 0] = temp
            temp_s = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 2, 1]
            cube[3, 2, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 2, 0]
            cube[1, 2, 0] = cube[1, 2, 2]
            cube[1, 2, 2] = temp
            temp_s = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = cube[1, 2, 1]
            cube[1, 2, 1] = temp_s
    elif(F == 'Y'):
        for i in range(3):
            temp = cube[5, i, c]
            cube[5, i, c] = cube[2, i, c]
            cube[2, i, c] = cube[0, i, c]
            cube[0, i, c] = cube[4, i, c]
            cube[4, i, c] = temp
        if(c == 0):
            temp = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 2, 2]
            cube[3, 2, 2] = cube[3, 2, 0]
            cube[3, 2, 0] = temp
            temp_s = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 2, 1]
            cube[3, 2, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 2, 0]
            cube[1, 2, 0] = cube[1, 2, 2]
            cube[1, 2, 2] = temp
            temp_s = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = cube[1, 2, 1]
            cube[1, 2, 1] = temp_s
    elif(F == 'O'):
        for i in range(3):
            temp = cube[3, i, c]
            cube[3, i, c] = cube[5, i, c]
            cube[5, i, c] = cube[1, i, c]
            cube[1, i, c] = cube[0, i, c]
            cube[0, i, c] = temp
        if(c == 0):
            temp = cube[4, 0, 0]
            cube[4, 0, 0] = cube[4, 0, 2]
            cube[4, 0, 2] = cube[4, 2, 2]
            cube[4, 2, 2] = cube[4, 2, 0]
            cube[4, 2, 0] = temp
            temp_s = cube[4, 0, 1]
            cube[4, 0, 1] = cube[4, 1, 2]
            cube[4, 1, 2] = cube[4, 2, 1]
            cube[4, 2, 1] = cube[4, 1, 0]
            cube[4, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[2, 0, 2]
            cube[2, 0, 2] = cube[2, 0, 0]
            cube[2, 0, 0] = cube[2, 2, 0]
            cube[2, 2, 0] = cube[2, 2, 2]
            cube[2, 2, 2] = temp
            temp_s = cube[2, 1, 2]
            cube[2, 1, 2] = cube[2, 0, 1]
            cube[2, 0, 1] = cube[2, 1, 0]
            cube[2, 1, 0] = cube[2, 2, 1]
            cube[2, 2, 1] = temp_s
    return cube

def rotate_down(cube, c, F):
    if c not in (0, 2):
        return cube
    if(F == 'W'):
        for i in range(3):
            temp = cube[0, i, c]
            cube[0, i, c] = cube[2, i, c]
            cube[2, i, c] = cube[5, i, c]
            cube[5, i, c] = cube[4, i, c]
            cube[4, i, c] = temp
        if(c == 0):
            temp = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 2, 0]
            cube[3, 2, 0] = cube[3, 2, 2]
            cube[3, 2, 2] = temp
            temp_s = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = cube[3, 2, 1]
            cube[3, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 2, 2]
            cube[1, 2, 2] = cube[1, 2, 0]
            cube[1, 2, 0] = temp
            temp_s = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 2, 1]
            cube[1, 2, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = temp_s
    elif(F == 'R'):
        for i in range(3):
            temp = cube[1, i, c]
            cube[1, i, c] = cube[0, i, c]
            cube[0, i, c] = cube[3, i, c]
            cube[3, i, c] = cube[5, i, c]
            cube[5, i, c] = temp
        if(c == 0):
            temp = cube[4, 0, 2]
            cube[4, 0, 2] = cube[4, 0, 0]
            cube[4, 0, 0] = cube[4, 2, 0]
            cube[4, 2, 0] = cube[4, 2, 2]
            cube[4, 2, 2] = temp
            temp_s = cube[4, 1, 2]
            cube[4, 1, 2] = cube[4, 0, 1]
            cube[4, 0, 1] = cube[4, 1, 0]
            cube[4, 1, 0] = cube[4, 2, 1]
            cube[4, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[2, 0, 0]
            cube[2, 0, 0] = cube[2, 0, 2]
            cube[2, 0, 2] = cube[2, 2, 2]
            cube[2, 2, 2] = cube[2, 2, 0]
            cube[2, 2, 0] = temp
            temp_s = cube[2, 0, 1]
            cube[2, 0, 1] = cube[2, 1, 2]
            cube[2, 1, 2] = cube[2, 2, 1]
            cube[2, 2, 1] = cube[2, 1, 0]
            cube[2, 1, 0] = temp_s
    elif(F == 'B'):
        for i in range(3):
            temp = cube[2, i, c]
            cube[2, i, c] = cube[0, i, c]
            cube[0, i, c] = cube[4, i, c]
            cube[4, i, c] = cube[5, i, c]
            cube[5, i, c] = temp
        if(c == 0):
            temp = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 2, 0]
            cube[1, 2, 0] = cube[1, 2, 2]
            cube[1, 2, 2] = temp
            temp_s = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = cube[1, 2, 1]
            cube[1, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 2, 2]
            cube[3, 2, 2] = cube[3, 2, 0]
            cube[3, 2, 0] = temp
            temp_s = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 2, 1]
            cube[3, 2, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = temp_s
    elif(F == 'G'):
        for i in range(3):
            temp = cube[4, i, c]
            cube[4, i, c] = cube[0, i, c]
            cube[0, i, c] = cube[2, i, c]
            cube[2, i, c] = cube[5, i, c]
            cube[5, i, c] = temp
        if(c == 0):
            temp = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 2, 0]
            cube[3, 2, 0] = cube[3, 2, 2]
            cube[3, 2, 2] = temp
            temp_s = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = cube[3, 2, 1]
            cube[3, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 2, 2]
            cube[1, 2, 2] = cube[1, 2, 0]
            cube[1, 2, 0] = temp
            temp_s = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 2, 1]
            cube[1, 2, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = temp_s
    elif(F == 'Y'):
        for i in range(3):
            temp = cube[5, i, c]
            cube[5, i, c] = cube[4, i, c]
            cube[4, i, c] = cube[0, i, c]
            cube[0, i, c] = cube[2, i, c]
            cube[2, i, c] = temp
        if(c == 0):
            temp = cube[3, 0, 2]
            cube[3, 0, 2] = cube[3, 0, 0]
            cube[3, 0, 0] = cube[3, 2, 0]
            cube[3, 2, 0] = cube[3, 2, 2]
            cube[3, 2, 2] = temp
            temp_s = cube[3, 1, 2]
            cube[3, 1, 2] = cube[3, 0, 1]
            cube[3, 0, 1] = cube[3, 1, 0]
            cube[3, 1, 0] = cube[3, 2, 1]
            cube[3, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[1, 0, 0]
            cube[1, 0, 0] = cube[1, 0, 2]
            cube[1, 0, 2] = cube[1, 2, 2]
            cube[1, 2, 2] = cube[1, 2, 0]
            cube[1, 2, 0] = temp
            temp_s = cube[1, 0, 1]
            cube[1, 0, 1] = cube[1, 1, 2]
            cube[1, 1, 2] = cube[1, 2, 1]
            cube[1, 2, 1] = cube[1, 1, 0]
            cube[1, 1, 0] = temp_s
    elif(F == 'O'):
        for i in range(3):
            temp = cube[3, i, c]
            cube[3, i, c] = cube[0, i, c]
            cube[0, i, c] = cube[1, i, c]
            cube[1, i, c] = cube[5, i, c]
            cube[5, i, c] = temp
        if(c == 0):
            temp = cube[4, 0, 2]
            cube[4, 0, 2] = cube[4, 0, 0]
            cube[4, 0, 0] = cube[4, 2, 0]
            cube[4, 2, 0] = cube[4, 2, 2]
            cube[4, 2, 2] = temp
            temp_s = cube[4, 1, 2]
            cube[4, 1, 2] = cube[4, 0, 1]
            cube[4, 0, 1] = cube[4, 1, 0]
            cube[4, 1, 0] = cube[4, 2, 1]
            cube[4, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[2, 0, 0]
            cube[2, 0, 0] = cube[2, 0, 2]
            cube[2, 0, 2] = cube[2, 2, 2]
            cube[2, 2, 2] = cube[2, 2, 0]
            cube[2, 2, 0] = temp
            temp_s = cube[2, 0, 1]
            cube[2, 0, 1] = cube[2, 1, 2]
            cube[2, 1, 2] = cube[2, 2, 1]
            cube[2, 2, 1] = cube[2, 1, 0]
            cube[2, 1, 0] = temp_s
    return cube

def rotate_right(cube, c, F):
    if c not in (0, 2):
        return cube
    if(F == 'W'):
        for i in range(3):
            temp = cube[0, c, i]
            cube[0, c, i] = cube[3, c, i]
            cube[3, c, i] = cube[5, c, i]
            cube[5, c, i] = cube[1, c, i]
            cube[1, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 2, 2]
            cube[0, 2, 2] = cube[0, 2, 0]
            cube[0, 2, 0] = temp
            temp_s = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 2, 1]
            cube[0, 2, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 2, 0]
            cube[5, 2, 0] = cube[5, 2, 2]
            cube[5, 2, 2] = temp
            temp_s = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = cube[5, 2, 1]
            cube[5, 2, 1] = temp_s
    elif(F == 'R'):
        for i in range(3):
            temp = cube[1, c, i]
            cube[1, c, i] = cube[0, c, i]
            cube[0, c, i] = cube[3, c, i]
            cube[3, c, i] = cube[5, c, i]
            cube[5, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 2, 2]
            cube[0, 2, 2] = cube[0, 2, 0]
            cube[0, 2, 0] = temp
            temp_s = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 2, 1]
            cube[0, 2, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 2, 0]
            cube[5, 2, 0] = cube[5, 2, 2]
            cube[5, 2, 2] = temp
            temp_s = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = cube[5, 2, 1]
            cube[5, 2, 1] = temp_s
    elif(F == 'B'):
        for i in range(3):
            temp = cube[2, c, i]
            cube[2, c, i] = cube[0, c, i]
            cube[0, c, i] = cube[4, c, i]
            cube[4, c, i] = cube[5, c, i]
            cube[5, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 2, 2]
            cube[0, 2, 2] = cube[0, 2, 0]
            cube[0, 2, 0] = temp
            temp_s = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 2, 1]
            cube[0, 2, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 2, 0]
            cube[5, 2, 0] = cube[5, 2, 2]
            cube[5, 2, 2] = temp
            temp_s = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = cube[5, 2, 1]
            cube[5, 2, 1] = temp_s
    elif(F == 'G'):
        for i in range(3):
            temp = cube[4, c, i]
            cube[4, c, i] = cube[3, c, i]
            cube[3, c, i] = cube[2, c, i]
            cube[2, c, i] = cube[1, c, i]
            cube[1, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 2, 2]
            cube[0, 2, 2] = cube[0, 2, 0]
            cube[0, 2, 0] = temp
            temp_s = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 2, 1]
            cube[0, 2, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 2, 0]
            cube[5, 2, 0] = cube[5, 2, 2]
            cube[5, 2, 2] = temp
            temp_s = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = cube[5, 2, 1]
            cube[5, 2, 1] = temp_s
    elif(F == 'Y'):
        for i in range(3):
            temp = cube[5, c, i]
            cube[5, c, i] = cube[3, c, i]
            cube[3, c, i] = cube[0, c, i]
            cube[0, c, i] = cube[1, c, i]
            cube[1, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 2, 2]
            cube[0, 2, 2] = cube[0, 2, 0]
            cube[0, 2, 0] = temp
            temp_s = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 2, 1]
            cube[0, 2, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 2, 0]
            cube[5, 2, 0] = cube[5, 2, 2]
            cube[5, 2, 2] = temp
            temp_s = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = cube[5, 2, 1]
            cube[5, 2, 1] = temp_s
    elif(F == 'O'):
        for i in range(3):
            temp = cube[3, c, i]
            cube[3, c, i] = cube[0, c, i]
            cube[0, c, i] = cube[1, c, i]
            cube[1, c, i] = cube[5, c, i]
            cube[5, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 2, 2]
            cube[0, 2, 2] = cube[0, 2, 0]
            cube[0, 2, 0] = temp
            temp_s = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 2, 1]
            cube[0, 2, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 2, 0]
            cube[5, 2, 0] = cube[5, 2, 2]
            cube[5, 2, 2] = temp
            temp_s = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = cube[5, 2, 1]
            cube[5, 2, 1] = temp_s
    return cube

def rotate_left(cube, c, F):
    if c not in (0, 2):
        return cube
    if(F == 'W'):
        for i in range(3):
            temp = cube[0, c, i]
            cube[0, c, i] = cube[1, c, i]
            cube[1, c, i] = cube[5, c, i]
            cube[5, c, i] = cube[3, c, i]
            cube[3, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 2, 0]
            cube[0, 2, 0] = cube[0, 2, 2]
            cube[0, 2, 2] = temp
            temp_s = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = cube[0, 2, 1]
            cube[0, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 2, 2]
            cube[5, 2, 2] = cube[5, 2, 0]
            cube[5, 2, 0] = temp
            temp_s = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 2, 1]
            cube[5, 2, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = temp_s
    elif(F == 'R'):
        for i in range(3):
            temp = cube[1, c, i]
            cube[1, c, i] = cube[2, c, i]
            cube[2, c, i] = cube[3, c, i]
            cube[3, c, i] = cube[4, c, i]
            cube[4, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 2, 0]
            cube[0, 2, 0] = cube[0, 2, 2]
            cube[0, 2, 2] = temp
            temp_s = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = cube[0, 2, 1]
            cube[0, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 2, 2]
            cube[5, 2, 2] = cube[5, 2, 0]
            cube[5, 2, 0] = temp
            temp_s = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 2, 1]
            cube[5, 2, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = temp_s
    elif(F == 'B'):
        for i in range(3):
            temp = cube[2, c, i]
            cube[2, c, i] = cube[3, c, i]
            cube[3, c, i] = cube[4, c, i]
            cube[4, c, i] = cube[1, c, i]
            cube[1, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 2, 0]
            cube[0, 2, 0] = cube[0, 2, 2]
            cube[0, 2, 2] = temp
            temp_s = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = cube[0, 2, 1]
            cube[0, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 2, 2]
            cube[5, 2, 2] = cube[5, 2, 0]
            cube[5, 2, 0] = temp
            temp_s = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 2, 1]
            cube[5, 2, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = temp_s
    elif(F == 'G'):
        for i in range(3):
            temp = cube[4, c, i]
            cube[4, c, i] = cube[1, c, i]
            cube[1, c, i] = cube[2, c, i]
            cube[2, c, i] = cube[3, c, i]
            cube[3, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 2, 0]
            cube[0, 2, 0] = cube[0, 2, 2]
            cube[0, 2, 2] = temp
            temp_s = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = cube[0, 2, 1]
            cube[0, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 2, 2]
            cube[5, 2, 2] = cube[5, 2, 0]
            cube[5, 2, 0] = temp
            temp_s = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 2, 1]
            cube[5, 2, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = temp_s
    elif(F == 'Y'):
        for i in range(3):
            temp = cube[5, c, i]
            cube[5, c, i] = cube[1, c, i]
            cube[1, c, i] = cube[0, c, i]
            cube[0, c, i] = cube[3, c, i]
            cube[3, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 2, 0]
            cube[0, 2, 0] = cube[0, 2, 2]
            cube[0, 2, 2] = temp
            temp_s = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = cube[0, 2, 1]
            cube[0, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 2, 2]
            cube[5, 2, 2] = cube[5, 2, 0]
            cube[5, 2, 0] = temp
            temp_s = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 2, 1]
            cube[5, 2, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = temp_s
    elif(F == 'O'):
        for i in range(3):
            temp = cube[3, c, i]
            cube[3, c, i] = cube[5, c, i]
            cube[5, c, i] = cube[1, c, i]
            cube[1, c, i] = cube[0, c, i]
            cube[0, c, i] = temp
        if(c == 0):
            temp = cube[0, 0, 2]
            cube[0, 0, 2] = cube[0, 0, 0]
            cube[0, 0, 0] = cube[0, 2, 0]
            cube[0, 2, 0] = cube[0, 2, 2]
            cube[0, 2, 2] = temp
            temp_s = cube[0, 1, 2]
            cube[0, 1, 2] = cube[0, 0, 1]
            cube[0, 0, 1] = cube[0, 1, 0]
            cube[0, 1, 0] = cube[0, 2, 1]
            cube[0, 2, 1] = temp_s
        elif(c == 2):
            temp = cube[5, 0, 0]
            cube[5, 0, 0] = cube[5, 0, 2]
            cube[5, 0, 2] = cube[5, 2, 2]
            cube[5, 2, 2] = cube[5, 2, 0]
            cube[5, 2, 0] = temp
            temp_s = cube[5, 0, 1]
            cube[5, 0, 1] = cube[5, 1, 2]
            cube[5, 1, 2] = cube[5, 2, 1]
            cube[5, 2, 1] = cube[5, 1, 0]
            cube[5, 1, 0] = temp_s
    return cube

init_3d_cube()
update_3d_cube(cube)

def get_camera_front_face():
    cam = scene.camera.pos
    
    abs_x, abs_y, abs_z = abs(cam.x), abs(cam.y), abs(cam.z)
    
    if abs_z >= abs_x and abs_z >= abs_y:
        return 'B' if cam.z > 0 else 'O'  
    elif abs_x >= abs_y and abs_x >= abs_z:
        return 'R' if cam.x > 0 else 'G'  
    else:
        return 'W' if cam.y > 0 else 'Y'

def keyInput(evt):
    k = evt.key.lower()
    c = 2 if evt.shift else 0
    F = get_camera_front_face()

    if k == 'u':
        rotate_up(cube, c, F)
    elif k == 'd':
        rotate_down(cube, c, F)
    elif k == 'l':
        rotate_left(cube, c, F)
    elif k == 'r':
        rotate_right(cube, c, F)

    update_3d_cube(cube)

scene.bind('keydown', keyInput)

while True:
    rate(30)