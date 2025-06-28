import sys

import pygame # type: ignore

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/sprite-0001.png")

        self.imgPos = [170, 170]
        self.movement = [False, False]

        self.collisionArea = pygame.Rect(50, 50, 540, 50)

        
    def run(self):
        while True:
            self.screen.fill((0, 0, 100))

            imgR = pygame.Rect(self.imgPos[0], self.imgPos[1], self.img.get_width(), self.img.get_height())
            if imgR.colliderect(self.collisionArea):
                pygame.draw.rect(self.screen, (255, 0, 0), self.collisionArea)
            else:
                pygame.draw.rect(self.screen, (0, 255, 0), self.collisionArea)

            self.imgPos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.imgPos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()