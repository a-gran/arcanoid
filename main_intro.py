# Импортируем библиотеку pygame для работы с графикой
import pygame
pygame.init()  # Инициализируем все необходимые модули pygame

# Определяем цвет фона (светлый голубой)
back = (200, 255, 255)

# Создаем окно размером 500x500 пикселей
mw = pygame.display.set_mode((500, 500))

# Заполняем экран фоном
mw.fill(back)

# Создаем объект для отслеживания времени и FPS
clock = pygame.time.Clock()
FPS = 60  # Устанавливаем частоту кадров (60 кадров в секунду)

# Класс Area для работы с прямоугольными областями
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        # Создаем прямоугольник с заданными координатами и размерами
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back  # Устанавливаем цвет по умолчанию (цвет фона)
        if color:  # Если передан новый цвет, то используем его
            self.fill_color = color

    # Метод для изменения цвета заливки области
    def color(self, new_color):       
        self.fill_color = new_color

    # Метод для отрисовки прямоугольника на экране
    def fill(self):        
        pygame.draw.rect(mw, self.fill_color, self.rect)

    # Проверяем на столкновение с другим прямоугольником
    def colliderect(self, rect):        
        return self.rect.colliderect(rect)

# Класс Label для работы с текстом (унаследован от Area)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        # Создаем изображение текста с заданным шрифтом и цветом
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    # Метод для отрисовки прямоугольника и текста
    def draw(self, shift_x=0, shift_y=0):        
        self.fill()  # Рисуем прямоугольник
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  # Отображаем текст поверх

# Класс Picture для работы с изображениями (унаследован от Area)
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        # Инициализируем родительский класс и загружаем изображение
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    # Метод для отображения изображения на экране
    def draw(self):        
        mw.blit(self.image, (self.rect.x, self.rect.y))

# Параметры для объектов на экране
platform_x = 200  # Начальная координата X платформы
platform_y = 400  # Начальная координата Y платформы
monster_x = 25  # Начальная координата X для монстров
monster_y = 25  # Начальная координата Y для монстров
count = 9  # Количество монстров в первой линии
monsters = []  # Список монстров
speed = 5  # Скорость мяча
dx = 2  # Направление движения мяча по оси X
dy = 2  # Направление движения мяча по оси Y

# Создаем объекты мяча и платформы
ball = Picture('ball.png', 160, 200, 50, 50)  # Мяч с начальной позицией и размерами
platform = Picture('platform.png', platform_x, platform_y, 100, 30)  # Платформа

# Создаем монстров, размещая их по линиям
for j in range(3):  # Проходим по трем линиям
    y = monster_y + (55 * j)  # Устанавливаем вертикальное положение монстров
    x = monster_x + (27.5 * j)  # Устанавливаем начальную горизонтальную позицию монстров
    for i in range(count):  # Размещаем монстров в линии
        d = Picture('enemy1.png', x, y, 50, 50)  # Создаем монстра
        monsters.append(d)  # Добавляем монстра в список
        x += 55  # Смещаем монстра по горизонтали
    count -= 1  # Уменьшаем количество монстров в следующей линии

# Флаги для управления движением платформы
move_right = False  # Флаг движения вправо
move_left = False  # Флаг движения влево
game_over = False  # Флаг окончания игры

# Основной игровой цикл
while not game_over:
    # Заполняем экран фоном
    ball.fill()  # Стираем предыдущий след мяча
    platform.fill()  # Стираем предыдущий след платформы

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если закрыли окно
            game_over = True  # Завершаем игру
            pygame.quit()  # Закрываем pygame

        # Обработка нажатий клавиш
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_RIGHT:  # Если нажата стрелка вправо
    #             move_right = True
    #         if event.key == pygame.K_LEFT:  # Если нажата стрелка влево
    #             move_left = True
    #     elif event.type == pygame.KEYUP:  # Если отпущены клавиши
    #         if event.key == pygame.K_RIGHT:
    #             move_right = False
    #         if event.key == pygame.K_LEFT:
    #             move_left = False

    # # Движение платформы
    # if move_right:
    #     platform.rect.x += speed  # Двигаем платформу вправо
    #     if platform.rect.x > 400:  # Ограничиваем движение справа
    #         platform.rect.x = 400
    # if move_left:
    #     platform.rect.x -= speed  # Двигаем платформу влево
    #     if platform.rect.x < 0:  # Ограничиваем движение слева
    #         platform.rect.x = 0

    # # Движение мяча
    # ball.rect.x += dx  # Двигаем мяч по X
    # ball.rect.y += dy  # Двигаем мяч по Y
    
    # # Обработка столкновений мяча с границами экрана
    # if ball.rect.y < 0:  # Если мяч коснулся верхней границы
    #     dy *= -1  # Меняем направление по Y
    # if ball.rect.x > 450 or ball.rect.x < 0:  # Если мяч коснулся боковых границ
    #     dx *= -1  # Меняем направление по X
    
    # # Проверка на проигрыш
    # if ball.rect.y > 520:  # Если мяч коснулся нижней границы
    #     time_text = Label(150, 200, 50, 50, back)  # Создаем надпись "YOU LOSE"
    #     time_text.set_text('YOU LOSE', 60, (255, 0, 0))
    #     time_text.draw(10, 10)  # Отображаем надпись
    #     game_over = True  # Завершаем игру
    
    # # Проверка на выигрыш
    # if len(monsters) == 0:  # Если все монстры уничтожены
    #     time_text = Label(150, 200, 50, 50, back)  # Создаем надпись "YOU WIN"
    #     time_text.set_text('YOU WIN', 60, (0, 200, 0))
    #     time_text.draw(10, 10)  # Отображаем надпись
    #     game_over = True  # Завершаем игру

    # # Обработка столкновения мяча с платформой
    # if ball.rect.colliderect(platform.rect):  # Если мяч касается платформы
    #     dy *= -1  # Меняем направление по Y
    
    # Отрисовка всех монстров
    for monster in monsters:
        monster.draw()  # Рисуем монстра
        if monster.rect.colliderect(ball.rect):  # Если мяч столкнулся с монстром
            monsters.remove(m)  # Удаляем монстра из списка
            monster.fill()  # Стираем его изображение
            dy *= -1  # Меняем направление мяча по Y

    # Отрисовка платформы и мяча
    platform.draw()
    ball.draw()

    # Обновляем экран
    pygame.display.update()
    clock.tick(FPS)  # Устанавливаем частоту кадров

# Обновляем экран после завершения игры
pygame.display.update()
