import sys

import pygame # type: ignore

from scripts.utils import loadImage
from scripts.entities import physicsEntity

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "player": loadImage("entities/player.png"),
        }

        self.Player = physicsEntity(self, "player", (170, 170), (50, 50))

        
    def run(self):
        while True:
            self.screen.fill((0, 0, 100))

            self.Player.update((self.movement[1] - self.movement[0], 0))
            self.Player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()