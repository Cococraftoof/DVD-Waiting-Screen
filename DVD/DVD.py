import sys, pygame
import random
from win32api import GetSystemMetrics
import random

Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)

pygame.init()

size = 0,0
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

dvd = dvd1 = pygame.image.load("dvd1.bmp")
dvd2 = pygame.image.load("dvd2.bmp")
dvd3 = pygame.image.load("dvd3.bmp")
dvd4 = pygame.image.load("dvd4.bmp")
dvd5 = pygame.image.load("dvd5.bmp")
dvd6 = pygame.image.load("dvd6.bmp")
dvd7 = pygame.image.load("dvd7.bmp")
dvd8 = pygame.image.load("dvd8.bmp")
dvd9 = pygame.image.load("dvd9.bmp")
dvd10 = pygame.image.load("dvd10.bmp")

dvdrect = dvd.get_rect()

rdm = [dvd1,dvd2,dvd3,dvd4,dvd5,dvd6,dvd7,dvd8,dvd9,dvd10]


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    dvdrect = dvdrect.move(speed)

    if dvdrect.left < 0 or dvdrect.right > Width:
        previousvalue = dvd
        dvd = random.choice(rdm)
        if previousvalue == dvd:
            dvd = previousvalue = random.choice(rdm)
        speed[0] = -speed[0]


    if dvdrect.top < 0 or dvdrect.bottom > Height:
        dvd = random.choice(rdm)

        speed[1] = -speed[1]

    if pygame.mouse.get_pressed() == (1,0,0):
        pygame.quit()

    pygame.mouse.set_visible(0)
    screen.fill(black)
    screen.blit(dvd, dvdrect)
    pygame.display.flip()

# dvd_images = [pygame.image.load(f"dvd{i}.bmp") for i in range(11)] Pour importer plusieurs images en même temps