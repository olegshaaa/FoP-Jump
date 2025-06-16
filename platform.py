import random
from settings import *
import pygame
from settings import PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR

class Platform:
    def __init__(self, x, y, question=None):
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.color = PLATFORM_COLOR
        self.question = question

    def render(self, box, scroll):
        platform_rect = self.rect.move(0, scroll)
        pygame.draw.rect(box, self.color, platform_rect)

def create_platform(y, used_questions, topic_questions):
    available_questions = [q for q in topic_questions if q not in used_questions]
    if not available_questions:
        return None
    x = random.randint(100, SCREEN_WIDTH - PLATFORM_WIDTH - 100)
    question = random.choice(available_questions)
    used_questions.add(question)
    return Platform(x, y, question)