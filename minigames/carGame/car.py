import sys, pygame
pygame.init()
clock = pygame.time.Clock()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0
green = 0, 255, 0

car = pygame.image.load('car.png')
screen = pygame.display.set_mode(size)

car_rect = car.get_rect()
car_rect.left = (size[0] / 2) - (car_rect.width / 2)
car_rect.bottom = size[1]

x_change = 0
y_change = 0

while 1:
    x = 0
    y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    x += x_change
    y += y_change
    car_rect = car_rect.move((x, y))

    screen.fill(black)
    screen.blit(car, car_rect)
    pygame.display.update()
    clock.tick(60)
