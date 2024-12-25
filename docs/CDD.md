# Software Design Document (SDD)

## Введение

• Цель документа: Предоставить подробное описание проектных решений для 2D игры “ПианоРитм” на Python с использованием Pygame.

• Область применения: Документ предназначен для разработчиков, участвующих в создании игры.

• Ссылки: SRS документация для игры “ПианоРитм”.

## Общее описание системы

• Игра представляет собой ритмичную казуальную игру, где игрок пытается попасть по клавишам в такт.

• Игра разрабатывается на Python 3.11.6 с использованием Pygame 2.6.1.

## Архитектурный дизайн

• В будущей разработке планируется создание классов Platform и Combo.

## Детальное описание компонентов

Методы
- main(): Запускает игру и поддерживает её ход.

- create_note(): Создает платформу в случайно выбранной дорожке.

- get_hit_grade(time_diff): Оценивает насколько игрок попал по клавише в зависимости от положения платформы на экране в этот момент.

  time_diff - разница между падением и линией попадания.

## Дизайн данных

• Списки note_KEY и notes используются для хранения клавиш, нажатие которых вызывает обработчик событий, и для выводимых платформ соответственно.
• Позиции объектов хранятся в виде координатных пар (x, y).

## Интерфейс системы

• Метод main() вызывает методы create_note и hit_grade() для изменения состояния игры.
• Пользователь взаимодействует с игрой через клавиатуру (клавиши для попадания A-S-D-F).

## Пользовательский интерфейс (UI)

• Игровой экран отображает дорожки, скатывающиеся вниз платформы и линии зоны попадания.
• Попадание по клавишам осуществляется нажатием клавиш A-S-D-F.

## Требования к производительности

• Игра должна поддерживать стабильную частоту кадров не менее 60 FPS.
• Потребление оперативной памяти не должно превышать 100 МБ.

## Безопасность (в разработке)

Планирование:
• Используются блоки try-except для обработки ошибок загрузки ресурсов.
• Проверяется наличие необходимых файлов ресурсов при запуске игры.

## Обеспечение качества
.
• Игра проходит стресс-тестирование с большим количеством клавиш без снижения производительности.

## Требования к среде разработки

• Язык программирования: Python 3.11+.
• Библиотеки: Pygame 2.6+.
• Среда разработки: PyCharm Community Edition.

## Приложения
### Диаграмма обновления игрового состояния в каждом цикле while, который находится в main().

![image](https://github.com/user-attachments/assets/b22f76e5-cef2-428c-bd8d-4f915be4a417)


