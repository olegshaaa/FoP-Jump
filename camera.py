class Camera:
    def __init__(self, screen_height, speed = 0.60):
        self.scroll = 0
        self.screen_height = screen_height
        self.speed = speed

    def move(self):
        self.scroll += self.speed

