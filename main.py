import sys, pygame, switchPage

pygame.init()

size = width, height = 1280, 800
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

font = pygame.font.SysFont('Helvetica', 30)
textsurface = font.render("test", False, white)
textrect = textsurface.get_rect()

textrect.left = 50
textrect.top = 50

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

    speed = switchPage.get_speed(dummyrect.left, page, width, 100)

    dummyrect = dummyrect.move(speed)
    textrect = textrect.move(speed)

    debugstring = str(speed[0]) + "," + str(speed[1]) + "\n" + str(dummyrect.left)
    debug = font.render(debugstring, False, white)
    debugrect = pygame.Rect(50, 500, 100, 100)

    screen.fill(black)
    screen.blit(textsurface, textrect)
    screen.blit(debug, debugrect)
    pygame.display.flip()
