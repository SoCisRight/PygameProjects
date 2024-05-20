
import pygame
import random

'''定义食物类'''
class Food(pygame.sprite.Sprite):
    def __init__(self, imagepath, position=(800,395), size=(70, 70), **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 导入图片
        self.images = []
        image = pygame.image.load(imagepath)
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i * 260, 0), (260, 260)), size))
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        # 定义一些必要的变量
        self.speed = -10
        self.is_eaten = False
        self.score = 1

    '''吃到了'''
    def eat(self, sounds):
        if self.is_eaten:
            return
        sounds['get'].play()
        self.is_eaten = True
    '''画到屏幕上'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    '''更新'''
    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()

