import pygame # type: ignore

BASE_IMG_PATH = "data/images/"

def loadImage(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    return img