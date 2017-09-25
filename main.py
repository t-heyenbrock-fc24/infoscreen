import sys
import pygame
import switchPage
import weather
import distance

pygame.init()

size = width, height = 640, 800
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Helvetica', 30)

weatherimage = pygame.image.load("images/weather.png")
weatherrect = weatherimage.get_rect()

weatherrect.left = 50
weatherrect.top = 50

weather = weather.Weather(100)
distance = distance.Distance(18, 24, 1)

dummyrect = pygame.Rect(0, 0, 0, 0)

page = 0

speed = [0, 0]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                if dummyrect.left % width == 0:
                    page = page + width
            elif event.key == pygame.K_RIGHT:
                if dummyrect.left % width == 0:
                    page = page - width

    weather.update_current()

    speed = switchPage.get_speed(dummyrect.left, page, width, 100)

    dummyrect = dummyrect.move(speed)
    weatherrect = weatherrect.move(speed)

    debugstring = str(speed[0]) + "," + str(speed[1]) + "\n" + str(dummyrect.left) + "\n" + str(distance.get_distance())
    debug = font.render(debugstring, False, white)
    debugrect = pygame.Rect(50, 500, 100, 100)

    screen.fill(black)
    screen.blit(weatherimage, weatherrect)
    screen.blit(debug, debugrect)
    pygame.display.flip()
