import pygame
import sys
import time
import copy
import numpy as np

window = (400,400)
screen = pygame.display.set_mode(window)

background = pygame.Surface(window)
background.fill((255,0,0))

width = 400
rows = 20
mat = [[0 for i in range(20)] for j in range(20)]
each_w = width/rows

clock = pygame.time.Clock()
FPS = 30


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





def draw_rect(i,j):
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




def simulate():
    background.fill((255,0,0))
    drawGrid()
    pygame.display.update()
    for i in range(20):
        for j in range(20):
            if mat[i][j] == 1:
                draw_rect(i,j)
    pygame.display.update()


def main():
    global mat
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

                draw_rect(i, j)
                print(np.matrix(mat))
                print("Initial State")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playSim = 1

        if playSim:
            for i in range(1):
                mat = crawl(mat)
                simulate()
            print(np.matrix(mat))
            playSim = 0
        screen.blit(background, (0, 0))

        clock.tick(FPS)
        pygame.display.update()
        drawGrid()

main()
