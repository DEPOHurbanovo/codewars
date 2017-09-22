import sys, pygame

pygame.init()
clock = pygame.time.Clock()

size = width, height = 800, 600
speed = [5, 5]
black = 0, 0, 0
green = 0, 255, 0
grey = 100, 100, 100

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

    keys_state = pygame.key.get_pressed()

    x_change = 0
    y_change = 0

    is_moving = False
    if keys_state[pygame.K_LEFT] == 1:
        x_change = -speed[0]
        is_moving = True
    if keys_state[pygame.K_RIGHT] == 1:
        x_change = speed[0]
        is_moving = True
    if keys_state[pygame.K_UP] == 1:
        y_change = -speed[1]
        is_moving = True
    if keys_state[pygame.K_DOWN] == 1:
        y_change = speed[1]
        is_moving = True

    if is_moving == False:
        x_change = 0;
        y_change = 0;
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += x_change
    y += y_change
    car_rect = car_rect.move((x, y))

    # Refresh the screen.
    screen.fill(black)
    # Grass
    grass_left = pygame.draw.rect(screen, green, (10, 0, 100, size[1]))
    grass_right = pygame.draw.rect(screen, green, (size[0] - 10, 0, -100, size[1]))
    # Wall
    wall_left = pygame.draw.rect(screen, grey, (0, 0, 10, size[1]))
    wall_right = pygame.draw.rect(screen, grey, (size[0], 0, -10, size[1]))

    
    if car_rect.colliderect(grass_left) or car_rect.colliderect(grass_right):
        speed = [2, 2]   
    else:
        speed = [5, 5]

    screen.blit(car, car_rect)
    pygame.display.update()
    clock.tick(60)
