import pygame
pygame.init()

def draw(imgs, win):
    for img, position in imgs:
        win.blit(img, position)

def player_move(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player.x > 0:
            player.move_left()
    if keys[pygame.K_d]:
        player.move_right()
    if keys[pygame.K_w]:
        if player.y > 0:
            player.move_up()
    if keys[pygame.K_s]:
        player.move_down()


# font variables
FONT = pygame.font.SysFont("comicsans",40)
text = FONT.render(f"You  Crashed", True, "red")
text_bg = pygame.Surface((text.get_width(), text.get_height()))
text_bg.fill("black")

FONT2 = pygame.font.SysFont("comicsans",30)
text2 = FONT2.render('press space to play again', True, "white")
text_bg2 = pygame.Surface((text2.get_width(), text2.get_height()))
text_bg2.fill("black")

FONT3 = pygame.font.SysFont("comicsans",45)
text3 = FONT3.render('You Win !!!', True, "green")
text_bg3 = pygame.Surface((text3.get_width(), text3.get_height()))
text_bg3.fill("black")


def colide_handle(player, WIN, WIDTH, HEIGHT):
        player.collide_stop()
        text_bg.blit(text, (0, 0))
        WIN.blit(text_bg, (WIDTH // 2 - text_bg.get_width() // 2, HEIGHT // 2 - text_bg.get_height() // 2))
        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        text_bg2.blit(text2, (0, 0))
        WIN.blit(text_bg2, (WIDTH // 2 - text_bg2.get_width() // 2, (HEIGHT // 2 - text_bg2.get_height() // 2)+100))
        WIN.blit(text2, (WIDTH // 2 - text2.get_width() // 2, (HEIGHT // 2 - text2.get_height() // 2)+100))

def win_handle(WIN, WIDTH, HEIGHT):
        text_bg3.blit(text3, (0, 0))
        WIN.blit(text_bg3, (WIDTH // 2 - text_bg3.get_width() // 2, HEIGHT // 2 - text_bg3.get_height() // 2))
        WIN.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 - text3.get_height() // 2))

        text_bg2.blit(text2, (0, 0))
        WIN.blit(text_bg2, (WIDTH // 2 - text_bg2.get_width() // 2, (HEIGHT // 2 - text_bg2.get_height() // 2)+100))
        WIN.blit(text2, (WIDTH // 2 - text2.get_width() // 2, (HEIGHT // 2 - text2.get_height() // 2)+100))