import pygame
from settings import *
from player import Player
from platform import Platform, create_platform
from questions import get_questions_by_topic
from camera import Camera
from windows import main_menu, instruction, choose_topic


pygame.init()
pygame.display.set_caption("FoP Jump")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


main_menu(screen)
instruction(screen)

while True:
    selected_topic, camera_speed = choose_topic(screen)
    topic_questions = get_questions_by_topic(selected_topic)

    time = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    camera = Camera(SCREEN_HEIGHT, speed = camera_speed)
    used_questions = set()
    platforms = []

    start_platform = Platform(SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2,SCREEN_HEIGHT - PLATFORM_HEIGHT - 50,None)
    platforms.append(start_platform)

    player = Player(start_platform.rect.centerx - PLAYER_WIDTH // 2,start_platform.rect.top - PLAYER_HEIGHT)
    player.on_platform = start_platform

    y = start_platform.rect.top - 150
    first_platform = create_platform(y, used_questions, topic_questions)
    current_question = first_platform.question if first_platform else None

    if first_platform:
        platforms.append(first_platform)
    else:
        player.alive = False

    game_win = False
    game_ended = True
    return_to_topic_select = False

    while not return_to_topic_select:
        time.tick(FPS)
        for act in pygame.event.get():
            if act.type == pygame.QUIT:
                exit()

            if act.type == pygame.KEYDOWN and player.alive and not game_win:
                if act.key in (pygame.K_z, pygame.K_x):
                    player_answer = act.key == pygame.K_z
                    current_platform = player.on_platform

                    upper_platforms = [p for p in platforms if p.rect.top < current_platform.rect.top]
                    if upper_platforms:
                        next_platform = min(upper_platforms, key=lambda p: current_platform.rect.top - p.rect.top)
                        if next_platform.question is not None and next_platform.question.answer == player_answer:
                            player.score += 1
                            player.jump_to_platform(next_platform)
                            current_question = None
                            next_platform.question = None

                            highest_y = min(p.rect.top for p in platforms)
                            new_platform = create_platform(highest_y - 150, used_questions, topic_questions)
                            if new_platform:
                                platforms.append(new_platform)
                                current_question = new_platform.question
                            else:
                                game_win = True
                        else:
                            player.alive = False


            elif game_ended and act.type == pygame.KEYDOWN:
                return_to_topic_select = True


        if not player.alive or game_win:
            if not game_ended:
                game_ended = True

            screen.fill(BACKGROUND_COLOR)
            text = f"Вы прошли все вопросы! Счёт: {player.score}" if game_win else f"Игра окончена! Правильных ответов: {player.score}"
            game_over_box = font.render(text, True, (230, 230, 15) if game_win else (255, 20, 20))
            rect = game_over_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_box, rect)

            info_box = font.render("Нажмите любую клавишу для возврата к выбору разделов", True, (255, 255, 255))
            info_rect = info_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
            screen.blit(info_box, info_rect)


            pygame.display.flip()
            continue

        camera.move()
        if player.rect.top + camera.scroll > SCREEN_HEIGHT:
            player.alive = False

        screen.fill(BACKGROUND_COLOR)

        for platform in platforms:
            platform.render(screen, camera.scroll)

        player_rect = player.rect.copy()
        player_rect.y += camera.scroll
        pygame.draw.rect(screen, player.color, player_rect)

        if current_question:
            question_box = font.render(current_question.text, True, (255, 255, 255))
            rect = question_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            screen.blit(question_box, rect)

        score_box = font.render(f"Правильных ответов: {player.score}", True, (255, 255, 255))
        screen.blit(score_box, (10, 10))

        pygame.display.flip()



