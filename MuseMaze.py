import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

done = False
image = pygame.image.load('maze.png').convert()
pygame.mouse.set_pos([319, 27])

while not done:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            print (mouse_pos)

            rect = pygame.Rect((370, 22), (388, 268))

        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))
    screen.blit(image, (20, 20))
    pygame.display.flip()

    clock.tick(60)


pygame.quit()

