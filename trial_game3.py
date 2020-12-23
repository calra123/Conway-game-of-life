# Game based on Conway's Game of Life.
# For futher reading checkout https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Built using pygame library.
# The code is free to use under I-Don't-Know License.

import pygame
import sys
import time
import copy
import numpy as np
import pygame_menu

# Let the game begin.
pygame.init()
window = (400,400)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Game of Life")

background = pygame.Surface(window)
sky_blue = (135,206,250)
background.fill(sky_blue)

width = 400
rows = 20
each_w = width/rows

clock = pygame.time.Clock()
FPS = 30

menu = pygame_menu.Menu(350, 350, 'Welcome',theme=pygame_menu.themes.THEME_BLUE)


def evolve(mat,i,j,n_mat):
    """
    Updating the current generation for each cell.
    Based on previous generation live neighbor cells.
    """
    count = hasNeighbors(mat,i,j)
    if mat[i][j] == 1 and count >=4:
        n_mat[i][j] = 0
    elif mat[i][j] == 0 and count == 3:
        n_mat[i][j] = 1
    elif mat[i][j] == 1 and count <= 1:
        n_mat[i][j] = 0

def crawl(mat):
    """
    Tying up the code together.
    Crawling through the matrix, to add or remove cells using evolve()
    """
    n_mat = copy.deepcopy(mat)
    for i in range(1,19):
        for j in range(1,19):
            evolve(mat,i,j,n_mat)

    mat = copy.deepcopy(n_mat)
    return mat

def hasNeighbors(mat,i,j):
    """
    Checks for "live" neighbor cells.
    Returns number of "live" neighbors.
    """
    pos_i = []
    pos_j = []
    count = 0
    if mat[i-1][j-1]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i-1][j]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i+1][j]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i][j-1]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i][j+1]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i+1][j+1]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i+1][j-1]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    if mat[i-1][j+1]==1:
        pos_i.append(i)
        pos_j.append(j)
        count+=1
    return count



def draw_rect(mat,i,j):
    """
    Draws a rectangle using the mouse co-ordinates.
    """
    click_i = i*each_w
    click_j = j*each_w
    pygame.draw.rect(background,(0,0,255),(click_i+2,click_j+2,20-2,20-2))
    mat[i][j] = 1


def drawGrid():
    """
    Adds grid lines to the boards.
    """
    x = 0
    y = 0

    for _ in range(rows):

        pygame.draw.line(background, (255,255,255), (x,0), (x,width))
        pygame.draw.line(background, (255,255,255), (0,y), (width,y))

        x+=each_w
        y+=each_w



def simulate(mat):
    """
    Updating the board with cells where user touched.
    """
    background.fill((135,206,250))
    drawGrid()
    pygame.display.update()
    for i in range(20):
        for j in range(20):
            if mat[i][j] == 1:
                draw_rect(mat,i,j)
    pygame.display.update()


def run_main():
    """
    Main function.
    Calls: draw_rect, crawl, simulate
    """
    mat = [[0 for i in range(20)] for j in range(20)]
    playSim = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                i = mx // rows
                j = my // rows

                # Draw a rectangle at the mouse coordinates.
                draw_rect(mat,i, j)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playSim = 1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.mainloop(screen)

        if playSim:
            for i in range(1):
                mat = crawl(mat)
                simulate(mat)
            playSim = 0
        
        screen.blit(background, (0, 0))

        clock.tick(FPS)
        pygame.display.update()
        drawGrid()


def play_animation():
    # TODO
    pass

def show_text(texts):
    """
    Re-usable function to show text one screen.
    texts: list of strings
    """
    font = pygame.font.SysFont('arial.ttf', 24)
    black = (0,0,0)
    rendered_texts = []

    for text in texts:
        render_text = font.render(text, True, black)
        rendered_texts.append(render_text)
    
    while True:
        screen.fill((200,200,200))

        spacing = 30
        inter_line_spacing = 20

        for text in rendered_texts:
            screen.blit(text, (20,inter_line_spacing))
            inter_line_spacing += spacing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # pygame.quit()
                    return
        pygame.display.update()
        pygame.display.flip()



def reset_the_game():
    """
    Resets the game, first instructions are shown.
    """
    texts = ["Press Spacebar to reset", "Press Esc to return"]
    show_text(texts)
    run_main()


def start_the_game():
    """
    Starter function, calls the run_main() function.
    """
    run_main()

def show_the_rules():
    # TODO

    # fonts = pygame.font.get_fonts()
    # for font in fonts:
    #     print(font)
    font = pygame.font.SysFont('arial.ttf', 24)

    black = (0,0,0)
    rule1 = "* Draw a cell by clicking anywhere"
    rule2 = "* Draw 2 or more cells to see the life simulation."
    rule3 = "* Press Spacebar to advance to next generation"
    info = "Press Esc to return to Main Menu."

    rules = "Rules: "
    game_rule1 = "1) Less than 2 cells, Dies by underpopulation"
    game_rule2 = "2) 2 or 3 cells, lives for another gen"
    game_rule3 = "3) More than 3 cells, Dies by overpopulation"
    game_rule4 = "4) Exactly 3 cells, a new cell is born"

    text1 = font.render(rule1, True, black)
    text2 = font.render(rule2, True, black)
    text3 = font.render(rule3, True, black)
    text4 = font.render(info, True, black)
    text5 = font.render(game_rule1, True, black)
    text6 = font.render(game_rule2, True, black)
    text7 = font.render(game_rule3, True, black)
    text8 = font.render(game_rule4, True, black)
    rules_text = font.render(rules, True, black)
    

    
    
    # textRect = text.get_rect()
    # textRect.center = (0,0)
    while True:
        # background = pygame.Surface(window)
        # background.fill((255,255,255))
        screen.fill((200,200,200))
        screen.blit(text1, (20,20))
        screen.blit(text2, (20,50))
        screen.blit(text3, (20,80))

        screen.blit(rules_text, (20,130))
        
        screen.blit(text5, (20,160))
        screen.blit(text6, (20,190))
        screen.blit(text7, (20,220))
        screen.blit(text8, (20,250))
        
        screen.blit(text4, (20,380))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # pygame.quit()
                    return
        pygame.display.update()
        pygame.display.flip()
        

    

menu.add_text_input('Name :', default='John Conway')
# menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add_text_input('Generations :', default=0, onchange=play_animation)
menu.add_button('Play', start_the_game)
menu.add_button('Rules', show_the_rules)
menu.add_button('Reset', reset_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)