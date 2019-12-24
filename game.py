import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Test")
screen.fill((255, 211, 0))
pygame.display.flip()

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('').convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()