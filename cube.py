import os
import numpy as np

cube = np.zeros((6, 3, 3), dtype=str)

cube[0,:,:] = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
cube[1,:,:] = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
cube[2,:,:] = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]   
cube[3,:,:] = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
cube[4,:,:] = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
cube[5,:,:] = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]

COLOR_BLOCKS = {
    'W': '\033[47m  \033[0m',
    'Y': '\033[43m  \033[0m',
    'G': '\033[42m  \033[0m',
    'B': '\033[44m  \033[0m',
    'O': '\033[48;5;208m  \033[0m',
    'R': '\033[41m  \033[0m',
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_cube(cube):
    def render_row(face_idx, row_idx):
        return "".join(COLOR_BLOCKS.get(cell, "  ") for cell in cube[face_idx, row_idx])

    print("\n" + "=" * 32)
    for r in range(3):
        print("        " + render_row(0, r))
    print("        " + "------")

    for r in range(3):
        o_str = render_row(3, r)
        g_str = render_row(4, r)
        r_str = render_row(1, r)
        b_str = render_row(2, r)
        print(f"{o_str}|{g_str}|{r_str}|{b_str}")

    print("        " + "------")
    for r in range(3):
        print("        " + render_row(5, r))
    print("=" * 32 + "\n")

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

while True:
    clear_screen()
    display_cube(cube)
    move = input("Enter the move (e.g., U, D, L, R): ")
    if move == 'U':
        c = int(input("Enter the column (0 or 2): "))
        F = input("Enter the face (W, R, B, G, Y, O): ")
        rotate_up(cube, c, F)
    elif move == 'D':
        c = int(input("Enter the column (0 or 2): "))
        F = input("Enter the face (W, R, B, G, Y, O): ")
        rotate_down(cube, c, F)
    elif move == 'L':
        c = int(input("Enter the row (0 or 2): "))
        F = input("Enter the face (W, R, B, G, Y, O): ")
        rotate_left(cube, c, F)
    elif move == 'R':
        c = int(input("Enter the row (0 or 2): "))
        F = input("Enter the face (W, R, B, G, Y, O): ")
        rotate_right(cube, c, F)
    

