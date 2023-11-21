import pygame
from utils import draw, player_move, colide_handle, win_handle

pygame.init()
is_finished = False
# loading the images and variables
MAZE = pygame.image.load("./img/maze-border.png")
MAZE_MASK = pygame.mask.from_surface(MAZE)
PLAYER = pygame.image.load("./img/player.png")
PLAYER = pygame.transform.scale(PLAYER, (17,17))
PLAYER_X = 75
PLAYER_Y = 0
PLAYER_vel = 0.8
WIDTH, HEIGHT = MAZE.get_width(), MAZE.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner!")

class Player:
    def __init__(self, player, vel):
        self.vel = vel
        self.player = player
        self.x, self.y = PLAYER_X, PLAYER_Y
    def move_right(self):
        self.x += self.vel
    def move_left(self):
        self.x -= self.vel
    def move_up(self):
        self.y -= self.vel
    def move_down(self):
        self.y += self.vel
    
    def collide(self, mask, x=0, y=0):
        player_mask = pygame.mask.from_surface(self.player)
        offset = (int(self.x - x), int(self.y - y))
        collision = mask.overlap(player_mask, offset)
        return collision
    def collide_stop(self):
        self.vel = 0
    def reset(self):
        self.x, self.y = PLAYER_X, PLAYER_Y
        self.vel = PLAYER_vel

images = [(MAZE,(0,0)),]

# running game frames per seconds
FPS = 60
run = True
clock = pygame.time.Clock()
player = Player(PLAYER, PLAYER_vel)


while run:
    clock.tick(FPS)
    WIN.fill((255,255,255))
    draw(images, WIN)
    for event in pygame.event.get():
        # close the window if pressing close button
        if event.type == pygame.QUIT:
            run = False
            break
    # player_move(RECT)

    if player.collide(MAZE_MASK):
        is_finished = True
        colide_handle(player, WIN, WIDTH, HEIGHT)

    if player.x > 540 and player.y > 600:
        win_handle(WIN, WIDTH, HEIGHT)
        is_finished = True
        player.vel = 0

    keys = pygame.key.get_pressed()
    player_move(player)
    if is_finished:
        if keys[pygame.K_SPACE]:
            player.reset()
            is_finished = False

    WIN.blit(PLAYER,(player.x, player.y))
    pygame.display.update()
pygame.quit()