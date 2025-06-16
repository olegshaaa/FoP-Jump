import pygame
from settings import *


def main_menu(screen):
    font = pygame.font.SysFont(None, 48)
    button_color = (50, 150, 50)
    text_color = (255, 255, 255)
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50)

    while True:
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, button_color, button_rect)
        text_box = font.render("Начать игру", True, text_color)
        text_rect = text_box.get_rect(center=button_rect.center)
        screen.blit(text_box, text_rect)

        for act in pygame.event.get():
            if act.type == pygame.QUIT:
                exit()
            elif act.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(act.pos):
                    return

        pygame.display.flip()


def instruction(screen):
    font = pygame.font.SysFont(None, 32)
    small_font = pygame.font.SysFont(None, 28)
    button_color = (50, 150, 50)
    text_color = (255, 255, 255)
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 80, 100, 40)

    instructions = [
        "Правила игры:",
        "",
        "- Отвечай на вопросы за отведенное время.",
        "- Нажми 'Z' для ответа 'Да', 'X' — для 'Нет'.",
        "- Если ответ верный, ты прыгаешь выше.",
        "- Если неверный — игра окончена.",
    ]


    while True:
        screen.fill(BACKGROUND_COLOR)
        for index, line in enumerate(instructions):
            text = font.render(line, True, text_color)
            screen.blit(text, (50, 100 + index * 40))

        pygame.draw.rect(screen, button_color, button_rect)
        button_text = small_font.render("Ок", True, text_color)
        button_rect_text = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_rect_text)

        for act in pygame.event.get():
            if act.type == pygame.QUIT:
                exit()
            elif act.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(act.pos):
                    return

        pygame.display.flip()


def choose_topic(screen):
    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 28)

    topics = ["Молекулярная физика", "МКТ", "Термодинамика"]
    buttons = []
    for i, topic in enumerate(topics):
        rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, 200 + i * 80, 300, 50)
        buttons.append((topic, rect))

    camera_speed = 0.55

    while True:
        screen.fill(BACKGROUND_COLOR)
        title = font.render("Выберите раздел:", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        for topic, rect in buttons:
            pygame.draw.rect(screen, (50, 150, 50), rect)
            text = font.render(topic, True, (255, 255, 255))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

        cam_speed_text = small_font.render(f"Скорость камеры: {camera_speed:.2f}", True, (255, 255, 255))
        screen.blit(cam_speed_text, (SCREEN_WIDTH // 2 - 120, 470))

        speed_hint = small_font.render("стрелка вверх/вниз изменить ", True, (180, 180, 180))
        screen.blit(speed_hint, (SCREEN_WIDTH // 2 - 150, 500))

        for act in pygame.event.get():
            if act.type == pygame.QUIT:
                exit()

            elif act.type == pygame.MOUSEBUTTONDOWN:
                for topic, rect in buttons:
                    if rect.collidepoint(act.pos):
                        return topic, camera_speed

            elif act.type == pygame.KEYDOWN:
                if act.key == pygame.K_DOWN:
                    camera_speed = max(0.2, camera_speed - 0.05)
                elif act.key == pygame.K_UP:
                    camera_speed = min(2.0, camera_speed + 0.05)

        pygame.display.flip()


