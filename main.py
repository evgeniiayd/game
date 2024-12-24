import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
CIRCLE_RADIUS = 50
CIRCLE_COLOR = (0, 255, 0)  # Зеленый цвет
BACKGROUND_COLOR = (0, 0, 0)  # Черный цвет
FONT_COLOR = (255, 255, 255)  # Белый цвет
FONT_SIZE = 36

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game")

# Шрифты
font = pygame.font.Font(None, FONT_SIZE)

# Игровые переменные
score = 0
circles = []
circle_timer = 0
circle_interval = 2000  # Интервал появления кругов в миллисекундах


# Функция для создания нового круга
def create_circle():
    x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
    circles.append((x, 0))


# Основной игровой цикл
def main():
    global circle_timer, score, circles
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND_COLOR)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Нажмите пробел для удара
                    for circle in circles:
                        if circle[1] > HEIGHT - CIRCLE_RADIUS:
                            score += 1
                            circles.remove(circle)
                            break

        # Создание нового круга
        circle_timer += clock.get_time()
        if circle_timer >= circle_interval:
            create_circle()
            circle_timer = 0

        # Обновление позиций кругов
        for i in range(len(circles)):
            circles[i] = (circles[i][0], circles[i][1] + 5)  # Двигаем круги вниз

        # Отрисовка кругов
        for circle in circles:
            pygame.draw.circle(screen, CIRCLE_COLOR, (circle[0], circle[1]), CIRCLE_RADIUS)

        # Отображение счета
        score_text = font.render(f'Score: {score}', True, FONT_COLOR)
        screen.blit(score_text, (10, 10))

        # Проверка на выход за границы
        circles = [circle for circle in circles if circle[1] < HEIGHT]

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

# Запуск игры
if __name__ == "__main__":
    main()
