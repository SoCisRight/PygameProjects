
import random
import pygame


'''障碍物'''
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, imagepaths, position=(800, 396), sizes=[(70, 70), (50, 50), (60, 60)], **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 导入图片
        self.images = []
        image = pygame.image.load(imagepaths[0])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i*657, 0), (657, 520)), sizes[0]))
        image = pygame.image.load(imagepaths[1])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i*485, 0), (485, 312)), sizes[1]))
        image = pygame.image.load(imagepaths[2])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i * 834, 0), (834, 520)), sizes[2]))
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        # 定义一些必要的变量
        self.speed = -10
    '''画到屏幕上'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    '''更新'''
    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


'''小鸟'''
class Bird(pygame.sprite.Sprite):
    def __init__(self, imagepath, position, size=(56, 52), **kwargs):

        pygame.sprite.Sprite.__init__(self)
        # 导入图片
        self.images = []
        image = pygame.image.load(imagepath)
        for i in range(5):
            self.images.append(pygame.transform.scale(image.subsurface((i*592, 0), (592, 591)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)
        # 定义一些必要的变量
        self.speed = -10
        self.refresh_rate = 10
        self.refresh_counter = 0
    '''画到屏幕上'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    '''更新'''
    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.loadImage()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1
    '''载入当前状态的图片'''
    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)




