import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
NOTE_WIDTH = 80
NOTE_HEIGHT = 30
NOTE_COLOR_OPTIONS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Красный, Зеленый, Синий
NOTE_KEYS = [pygame.K_a, pygame.K_s, pygame.K_d]  # Клавиши для A, S, D
NOTE_KEYS_COLOR_MAP = {pygame.K_a: (255, 0, 0), pygame.K_s: (0, 255, 0), pygame.K_d: (0, 0, 255)}  # Соответствие клавиш и цветов
BACKGROUND_COLOR = (0, 0, 0)  # Черный цвет
FONT_COLOR = (255, 255, 255)  # Белый цвет
FONT_SIZE = 36

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game Inspired by DJMAX")

# Шрифты
font = pygame.font.Font(None, FONT_SIZE)

# Игровые переменные
score = 0
notes = []  # Список нот
note_timer = 0
note_interval = 1000  # Интервал появления нот в миллисекундах

# Функция для создания новой ноты
def create_note():
    x = random.randint(0, WIDTH - NOTE_WIDTH)
    color = random.choice(NOTE_COLOR_OPTIONS)
    notes.append((x, 0, color))  # Добавление ноты с координатами (x, 0) и цветом

# Основной игровой цикл
def main():
    global note_timer, score, notes  # Объявляем переменные глобальными
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND_COLOR)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in NOTE_KEYS:  # Проверяем, нажата ли клавиша для нот
                    for note in notes:
                        if note[1] > HEIGHT - NOTE_HEIGHT and note[2] == NOTE_KEYS_COLOR_MAP[event.key]:  # Проверка цвета
                            score += 1
                            notes.remove(note)  # Удаление ноты после удара
                            break

        # Создание новой ноты
        note_timer += clock.get_time()
        if note_timer >= note_interval:
            create_note()
            note_timer = 0

        # Обновление позиций нот
        notes = [(note[0], note[1] + 5, note[2]) for note in notes]  # Двигаем ноты вниз

        # Отрисовка нот
        for note in notes:
            pygame.draw.rect(screen, note[2], (note[0], note[1], NOTE_WIDTH, NOTE_HEIGHT))

        # Отображение счета
        score_text = font.render(f'Score: {score}', True, FONT_COLOR)
        screen.blit(score_text, (10, 10))

        # Проверка на выход за границы
        notes = [note for note in notes if note[1] < HEIGHT]  # Удаляем ноты, вышедшие за границы

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

# Запуск игры
if __name__ == "__main__":
    main()

