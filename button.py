import pygame

# Button Class
class Button():
    def __init__(self, x, y, WIDTH, image, center=True, scale=1):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        if center:
            self.auto_center(WIDTH)

    def draw(self, surface):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        surface.blit(self.image, (self.rect.x,self.rect.y))

        return action

    def auto_center(self, WIDTH):
        x = (WIDTH - self.rect[2]) / 2
        self.rect.topleft = (x, self.rect.topleft[1])