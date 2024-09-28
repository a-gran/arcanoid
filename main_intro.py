import pygame
pygame.init()

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()
FPS = 60

class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

platform_x = 200
platform_y = 400
monster_x = 25
monster_y = 25
count = 9
monsters = []
speed = 5
dx = speed
dy = speed

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 30)

for j in range(3):
    y = monster_y + (55 * j)
    x = monster_x + (27.5 * j)
    for i in range(count):
        d = Picture('enemy1.png', x, y, 50, 50)
        monsters.append(d)
        x += 55
    count -= 1

move_right = False
move_left = False
game_over = False

while not game_over:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()

    for m in monsters:
        m.draw()
    # если монстра коснулся мяч, удаляем монстра из списка и меняем направления движения мяча
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1

    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.display.update()




    #    if event.type == pygame.KEYDOWN:
    #        if event.key == pygame.K_RIGHT:
    #            move_right = True
    #        if event.key == pygame.K_LEFT:
    #            move_left = True
    #    elif event.type == pygame.KEYUP:
    #        if event.key == pygame.K_RIGHT:
    #            move_right = False
    #        if event.key == pygame.K_LEFT:
    #            move_left = False

    #if move_right:
    #    platform.rect.x += speed
    #    # ограничение платформы справа
    #    if platform.rect.x > 400:
    #        platform.rect.x = 400
    #if move_left:
    #    platform.rect.x -= speed
    #    # ограничение платформы слева
    #    if platform.rect.x < 0:
    #        platform.rect.x = 0

    #ball.rect.x += dx
    #ball.rect.y += dy

    #if ball.rect.y < 0:
    #    dy *= -1
    #if ball.rect.x > 450 or ball.rect.x < 0:
    #    dx *= -1
    ## отрисовка надписи при проигрыше
    #if ball.rect.y > 450:
    #    time_text = Label(150, 150, 50, 50, back)
    #    time_text.set_text('YOU LOSE', 60, (255, 0, 0))
    #    time_text.draw(10, 10)
    #    game_over = True
    ## отрисовка надписи при выигрыше
    #if len(monsters) == 0:
    #    time_text = Label(150, 150, 50, 50, back)
    #    time_text.set_text('YOU WIN', 60, (0, 200, 0))
    #    time_text.draw(10, 10)
    #    game_over = True
    ## отскок мяча от платформы
    #if ball.rect.colliderect(platform.rect):
    #    dy *= -1
