import sys, pygame
pygame.init()
clock = pygame.time.Clock()

size = width, height = 800, 600
# how many pixels on one move, [x, y].
speed = [5, 5]
black = 0, 0, 0
green = 0, 255, 0
grey = 100, 100, 100

car = pygame.image.load('car.png')
screen = pygame.display.set_mode(size)

# Initialize screen.
car_rect = car.get_rect()
car_rect.left = (size[0] / 2) - (car_rect.width / 2)
car_rect.bottom = size[1]

x_change = 0
y_change = 0

while 1:
    # Reset the stae
    x = 0
    y = 0
    x_change = 0
    y_change = 0
    # Check pygame events in every tick.
    keys_state = pygame.key.get_pressed();
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    moving = False
    if keys_state[pygame.K_LEFT] == True:
        x_change = -speed[0]
        moving = True
    if keys_state[pygame.K_RIGHT] == True:
        x_change = speed[0]
        moving = True
    if keys_state[pygame.K_UP] == True:
        y_change = -speed[1]
        moving = True
    if keys_state[pygame.K_DOWN] == True:
        y_change = speed[1]
        moving = True
    if not moving:
        x_change = 0
        y_change = 0

    # Events processed, add change to current position.
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

    # Collision detection
    if car_rect.colliderect(grass_left) or car_rect.colliderect(grass_right):
        speed = [2, 2]
    else:
        speed = [5, 5]

    screen.blit(car, car_rect)
    pygame.display.update()
    # Set clock tick to control speed of game
    clock.tick(60)
