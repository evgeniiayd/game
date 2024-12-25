import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
speed = 60
NOTE_WIDTH = 80
NOTE_HEIGHT = 30
NOTE_COLOR = (255, 255, 255)  # Белый цвет для всех нот
NOTE_KEYS = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]  # Клавиши для A, S, D, F
KEY_LABELS = ['A', 'S', 'D', 'F']  # Подписи клавиш
BACKGROUND_COLOR = (0, 0, 0)  # Черный цвет
FONT_COLOR = (255, 255, 255)  # Белый цвет
FONT_SIZE = 36
NOTE_FALL_SPEED = 5  # Скорость падения нот
NOTE_COLUMNS = 4  # Количество колонок для нот
HIT_LINE_Y = HEIGHT - 100  # Координата линии попадания
PERFECT_RANGE = 10  # Диапазон для "идеально"
GOOD_RANGE = 30  # Диапазон для "хорошо"
NORMAL_RANGE = 50  # Диапазон для "нормально"
BAD_RANGE = 70  # Диапазон для "плохо"
MISSED_RANGE = 90  # Диапазон для "промах"
GREAT_SCORE = 1000
GOOD_SCORE = 750
OK_SCORE = 500
BAD_SCORE = 200
MISS_SCORE = 0

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game")

# Шрифты
font = pygame.font.Font(None, FONT_SIZE)

# Звуковые эффекты
hit_sound = pygame.mixer.Sound('hit_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')

# Игровые переменные
score = 0
combo = 0  # Счетчик комбо
notes = []  # Список нот
note_timer = 0
note_interval = 1000  # Интервал появления нот в миллисекундах
last_hit_time = 0  # Время последнего удара
hit_text = ""  # Текст для отображения попадания
color = tuple[int, int, int]

# Функция для создания новой ноты
def create_note():
    # Определяем случайную колонку для ноты
    column = random.randint(0, NOTE_COLUMNS - 1)
    x = column * (WIDTH // NOTE_COLUMNS) + (WIDTH // NOTE_COLUMNS - NOTE_WIDTH) // 2  # Позиция по оси X для колонок
    y = -NOTE_HEIGHT  # Начальная позиция за экраном
    notes.append([x, y])  # Добавление ноты с координатами (x, 0)

# Функция для оценки попадания
def get_hit_grade(time_diff):
    """Оценка попадания в зависимости от времени"""
    if abs(time_diff) <= PERFECT_RANGE:
        return "Great", GREAT_SCORE, (0, 255, 0)  # Зелёный для "идеально"
    elif abs(time_diff) <= GOOD_RANGE:
        return "Good", GOOD_SCORE, (255, 165, 0)  # Оранжевый для "хорошо"
    elif abs(time_diff) <= NORMAL_RANGE:
        return "Ok", OK_SCORE, (255, 255, 0)  # Желтый для "нормально"
    elif abs(time_diff) <= BAD_RANGE:
        return "Bad", BAD_SCORE, (255, 165, 0)  # Оранжевый для "плохо"
    else:
        return "Miss", MISS_SCORE, (255, 0, 0)  # Красный для "промаха"

# Основной игровой цикл
def main():
    global note_timer, score, notes, last_hit_time, hit_text, combo, color  # Объявляем переменные глобальными
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
                    # Для каждой колонки находим соответствующую клавишу и проверяем, если нота внизу
                    column_index = NOTE_KEYS.index(event.key)
                    for note in notes:
                        note_x = note[0]
                        column_start = column_index * (WIDTH // NOTE_COLUMNS)
                        column_end = column_start + (WIDTH // NOTE_COLUMNS)

                        # Если нота в нужной колонке
                        if column_start <= note_x <= column_end:
                            time_diff = note[1] - HIT_LINE_Y  # Разница между падением и линией попадания

                            # Если нота еще не пересекла линию
                            grade, score_value, color = get_hit_grade(time_diff)
                            hit_text = grade  # Обновляем текст оценки

                            if grade != "Miss":
                                score += score_value
                                if grade != "Bad":
                                    combo += 1
                                else:
                                    combo = 0
                                notes.remove(note)  # Удаление ноты после удара
                                hit_sound.play()  # Воспроизведение звука удара
                            else:
                                combo = 0  # Сбросить комбо при промахе
                            break

        # Создание новой ноты
        note_timer += clock.get_time()
        if note_timer >= note_interval:
            create_note()
            note_timer = 0

        # Обновление позиций нот
        notes = [[note[0], note[1] + NOTE_FALL_SPEED] for note in notes]  # Двигаем ноты вниз

        # Отрисовка колонок
        for i in range(1, NOTE_COLUMNS):
            pygame.draw.line(screen, FONT_COLOR, (i * (WIDTH // NOTE_COLUMNS), 0), (i * (WIDTH // NOTE_COLUMNS), HEIGHT), 2)

        # Подписи клавиш
        for i in range(NOTE_COLUMNS):
            label = font.render(KEY_LABELS[i], True, FONT_COLOR)
            screen.blit(label, (i * (WIDTH // NOTE_COLUMNS) + (WIDTH // NOTE_COLUMNS - label.get_width()) // 2, HEIGHT-40))

        # Отрисовка линии попадания
        pygame.draw.line(screen, (255, 0, 0), (0, HIT_LINE_Y+20), (WIDTH, HIT_LINE_Y+20), 3)  # Красная линия

        # Отрисовка нот
        for note in notes:
            pygame.draw.rect(screen, NOTE_COLOR, (note[0], note[1], NOTE_WIDTH, NOTE_HEIGHT))

        # Отображение счета
        score_text = font.render(f'Score: {score}', True, FONT_COLOR)
        screen.blit(score_text, (10, 10))

        # Отображение комбо
        combo_text = font.render(f'Combo: x{combo}', True, FONT_COLOR)
        screen.blit(combo_text, (WIDTH - combo_text.get_width() - 10, 10))

        # Отображение оценки попадания
        if hit_text:
            hit_text_render = font.render(hit_text, True, color)
            screen.blit(hit_text_render, (WIDTH // 2 - hit_text_render.get_width() // 2, HEIGHT // 2))

        # Проверка на выход за границы
        notes = [note for note in notes if note[1] < HEIGHT]  # Удаляем ноты, вышедшие за границы

        # Пропущенные ноты
        if any(note[1] > HEIGHT for note in notes):
            miss_sound.play()  # Звук пропущенной ноты
            notes = [note for note in notes if note[1] <= HEIGHT]  # Удаляем пропущенные ноты
            combo = 0  # Сбросить комбо, если пропущена нота

        # Обновление экрана
        pygame.display.flip()
        clock.tick(speed)

# Запуск игры
if __name__ == "__main__":
    main()