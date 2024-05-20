
import sys
import pygame
from ..sprites import Rabbit


'''游戏开始界面'''
def GameStartInterface(screen, sounds, cfg):
    rabbit = Rabbit(cfg.IMAGE_PATHS['rabbit'])
    BG = pygame.image.load("resources/images/BG.png")  # 图片位置
    #ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))
    #ground = pygame.transform.scale(ground, (100, 100))
    #rect = ground.get_rect()
    #rect.left, rect.bottom = cfg.SCREENSIZE[0]/20, cfg.SCREENSIZE[1]
    playgame_image = pygame.image.load(cfg.IMAGE_PATHS['gamestart'])
    playgame_image = pygame.transform.scale(playgame_image, (400, 150))
    playgame_image_rect = playgame_image.get_rect()
    playgame_image_rect.centerx = cfg.SCREENSIZE[0] / 2
    playgame_image_rect.centery = cfg.SCREENSIZE[1] * 0.45
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
                    rabbit.jump(sounds)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if playgame_image_rect.collidepoint(mouse_pos):
                    press_flag = True
                    rabbit.jump(sounds)
        rabbit.update()
        screen.fill(cfg.BACKGROUND_COLOR)
        #screen.blit(ground, rect)
        screen.blit(BG, (0, 0))  # 对齐的坐标
        rabbit.draw(screen)
        screen.blit(playgame_image, playgame_image_rect)
        pygame.display.update()
        clock.tick(cfg.FPS)
        if (not rabbit.is_jumping) and press_flag:
            return True