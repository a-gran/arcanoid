# Импортируем необходимые библиотеки
import pygame  # Библиотека для создания игр
from random import randint  # Функция для генерации случайных чисел
import time  # Библиотека для работы со временем

# Инициализация pygame
pygame.init()

# Создаем объект для управления временем
clock = pygame.time.Clock()
# Генерируем случайный цвет фона (RGB)
back = (randint(0, 255), randint(0, 255), randint(0, 255))
# Генерируем случайные размеры окна
width = randint(500, 1000)
height = randint(500, 1000)
# Создаем окно игры
mw = pygame.display.set_mode((width, height))
# Заполняем окно случайным цветом
mw.fill(back)

# Определяем основные цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60  # Частота обновления экрана

# Базовый класс для создания прямоугольных областей
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        # Создаем прямоугольник с заданными параметрами
        self.rect = pygame.Rect(x, y, width, height)
        # Устанавливаем цвет заливки
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        # Метод для изменения цвета
        self.fill_color = new_color

    def fill(self):
        # Метод для отрисовки прямоугольника
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def colliderect(self, rect):
        # Метод для проверки столкновения с другим прямоугольником
        return self.rect.colliderect(rect)

# Класс для создания текстовых надписей
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        # Создаем текстовое изображение
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        # Отрисовываем текст с учетом смещения
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Класс для работы с изображениями
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        # Инициализируем базовый класс
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        # Пытаемся загрузить изображение
        self.image = None
        try:
            self.image = pygame.image.load(filename)
        except:
            # Если загрузка не удалась, устанавливаем цвет для прямоугольника
            if 'ball' in filename.lower():
                self.fill_color = BLUE  # Мяч будет синим
            elif 'platform' in filename.lower():
                self.fill_color = GREEN  # Платформа будет зеленой
            else:
                self.fill_color = RED  # Монстры будут красными

    def draw(self):
        # Отрисовываем изображение или цветной прямоугольник
        if self.image is not None:
            mw.blit(self.image, (self.rect.x, self.rect.y))
        else:
            pygame.draw.rect(mw, self.fill_color, self.rect)

# Задаем начальные параметры игры
platform_x = randint(0, width-100)  # Случайная позиция платформы по X
platform_y = randint(height-200, height-50)  # Случайная позиция платформы по Y
monster_x = 25  # Начальная позиция монстров по X
monster_y = 25  # Начальная позиция монстров по Y
count = 9  # Количество монстров в ряду
monsters = []  # Список для хранения монстров
# Список файлов с изображениями врагов
enemies = ['enemy2.png', 'enemy3.png', 'enemy4.png', 'enemy5.png', 'enemy6.png', 
           'enemy7.png', 'enemy8.png', 'enemy9.png', 'enemy10.png']
speed = randint(5, 10)  # Случайная скорость движения платформы
dx = 4  # Скорость движения мяча по X
dy = 4  # Скорость движения мяча по Y

# Создаем мяч и платформу
ball = Picture('poceball.png', randint(50, width-50), randint(150, 250), 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 25)

# Создаем монстров
for j in range(randint(2, 7)):  # Случайное количество рядов
    y = monster_y + (55 * j)  # Вычисляем позицию по Y для текущего ряда
    x = monster_x + (27.5 * j)  # Вычисляем начальную позицию по X
    for i in range(count):  # Создаем монстров в ряду
        # Создаем монстра со случайным изображением
        monster = Picture(enemies[randint(0, len(enemies) - 1)], x, y, 50, 50)
        monsters.append(monster)  # Добавляем монстра в список
        x += 55  # Смещаем позицию для следующего монстра
    count -= 1  # Уменьшаем количество монстров в следующем ряду

# Флаги для управления движением
move_right = False
move_left = False
move_up = False
move_down = False
game_over = False  # Флаг окончания игры

# Записываем время начала игры
start_time = time.time()

# Основной игровой цикл
while not game_over:
    # Очищаем предыдущие позиции мяча и платформы
    ball.fill()
    platform.fill()

    # Обработка событий во время паузы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажат крестик окна
            waiting = False
            pygame.quit()
            exit()  # Добавляем принудительный выход из программы

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        # Обработка отпускания клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    # Движение платформы вправо
    if move_right:
        platform.rect.x += speed
        # Ограничение движения справа
        if platform.rect.x > width-100:
            platform.rect.x = width-100

    # Движение платформы влево
    if move_left:
        platform.rect.x -= speed
        # Ограничение движения слева
        if platform.rect.x < 0:
            platform.rect.x = 0

    # Движение платформы вверх
    if move_up:
        platform.rect.y -= speed
        # Ограничение движения сверху
        if platform.rect.y < height-200:
            platform.rect.y = height-200

    # Движение платформы вниз
    if move_down:
        platform.rect.y += speed
        # Ограничение движения снизу
        if platform.rect.y > height-50:
            platform.rect.y = height-50

    # Движение мяча
    ball.rect.x += dx
    ball.rect.y += dy

    # Отскок мяча от верхней границы
    if ball.rect.y < 0:
        dy *= -1
    # Отскок мяча от боковых границ
    if ball.rect.x > width-50 or ball.rect.x < 0:
        dx *= -1

    # Проверка проигрыша (мяч упал вниз)
    if ball.rect.y > height-50:
        time_text = Label(150, 250, 200, 50, back)
        time_text.set_text('YOU LOSE', 60, WHITE)
        time_text.draw(10, 10)
        game_over = True

    # Проверка победы (все монстры уничтожены)
    if len(monsters) == 0:
        # Вычисляем время игры
        game_time = round(time.time() - start_time, 1)
        
        # Отрисовка надписи о победе
        win_text = Label(150, 250, 200, 50, back)
        win_text.set_text('YOU WIN', 60, WHITE)
        win_text.draw(10, 10)
        
        # Отрисовка времени под надписью о победе
        time_text = Label(150, 320, 200, 50, back)
        time_text.set_text(f'Время игры: {game_time} сек.', 40, WHITE)
        time_text.draw(10, 10)
        
        game_over = True

    # Проверка столкновения мяча с платформой
    if ball.rect.colliderect(platform.rect):
        dy *= -1

    # Обработка монстров
    for monster in monsters:
        monster.draw()  # Отрисовка монстра
        # Проверка столкновения мяча с монстром
        if monster.rect.colliderect(ball.rect):
            monsters.remove(monster)  # Удаляем монстра
            monster.fill()  # Очищаем область монстра
            dy *= -1  # Отскок мяча

    # Отрисовка платформы и мяча
    platform.draw()
    ball.draw()
    
    # Обновление экрана
    pygame.display.update()
    # Установка частоты обновления
    clock.tick(FPS)
 
# Финальное обновление экрана
pygame.display.update()