import pygame
import sys
import time
import copy
import numpy as np
import pygame_menu

pygame.init()
window = (400,400)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Game of Life")

background = pygame.Surface(window)
background.fill((255,0,0))

width = 400
rows = 20
# mat = [[0 for i in range(20)] for j in range(20)]
each_w = width/rows

clock = pygame.time.Clock()
FPS = 30

menu = pygame_menu.Menu(350, 350, 'Welcome',theme=pygame_menu.themes.THEME_BLUE)





def evolve(mat,i,j,n_mat):
    count = hasNeighbors(mat,i,j)


    #print(count)
    #print("count: ", count)
    if mat[i][j] == 1 and count >=4:
        n_mat[i][j] = 0
    elif mat[i][j] == 0 and count == 3:
        n_mat[i][j] = 1
    elif mat[i][j] == 1 and count <= 1:
        n_mat[i][j] = 0

def crawl(mat):
    # print("Crawled")
    n_mat = copy.deepcopy(mat)
    # print(np.matrix(mat))


    #print("Crawl finish")
    for i in range(1,19):
        for j in range(1,19):
            evolve(mat,i,j,n_mat)
            # if mat[i][j] == 1:

    mat = copy.deepcopy(n_mat)
    return mat

def hasNeighbors(mat,i,j):
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
    click_i = i*each_w
    click_j = j*each_w
    pygame.draw.rect(background,(0,0,255),(click_i+2,click_j+2,20-2,20-2))
    mat[i][j] = 1


def drawGrid():


    x = 0
    y = 0

    for i in range(rows):


        pygame.draw.line(background, (255,255,255), (x,0), (x,width))
        pygame.draw.line(background, (255,255,255), (0,y), (width,y))

        x+=each_w
        y+=each_w

    #pygame.display.update()




def simulate(mat):
    background.fill((255,0,0))
    drawGrid()
    pygame.display.update()
    for i in range(20):
        for j in range(20):
            if mat[i][j] == 1:
                draw_rect(mat,i,j)
    pygame.display.update()


def main():
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

                draw_rect(mat,i, j)
                print(np.matrix(mat))
                print("Initial State")
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
            print(np.matrix(mat))
            playSim = 0
        screen.blit(background, (0, 0))

        clock.tick(FPS)
        pygame.display.update()
        drawGrid()

# main()

def play_animation():
    # TODO
    pass

def reset_the_game():
    # TODO
    global mat
    mat = [[0 for i in range(20)] for j in range(20)]
    main()
    # pass

def start_the_game():
    main()

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

    text1 = font.render(rule1, True, black)
    text2 = font.render(rule2, True, black)
    text3 = font.render(rule3, True, black)
    text4 = font.render(info, True, black)
    
    
    # textRect = text.get_rect()
    # textRect.center = (0,0)
    while True:
        # background = pygame.Surface(window)
        # background.fill((255,255,255))
        screen.fill((200,200,200))
        screen.blit(text1, (20,20))
        screen.blit(text2, (20,50))
        screen.blit(text3, (20,80))
        screen.blit(text4, (20,180))
        
        
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
menu.add_text_input('Generations :', default=0, onchange=play_animation)
menu.add_button('Play', start_the_game)
menu.add_button('Rules', show_the_rules)
menu.add_button('Reset', reset_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)