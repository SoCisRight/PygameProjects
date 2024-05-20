
import cfg
import sys
import random
import pygame
from modules import *


'''main'''
def main(highest_score):
    # 游戏初始化
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('跑酷游戏')
    # 播放背景音乐
    pygame.mixer.music.load(cfg.AUDIO_PATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)
    # 字体加载
    font = pygame.font.Font(cfg.FONT_PATH, 40)
    # 导入所有声音文件
    sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        sounds[key] = pygame.mixer.Sound(value)
    # 游戏开始界面
    GameStartInterface(screen, sounds, cfg)
    # 游戏背景
    background=pygame.image.load("resources/images/background.png")  #图片位置
    # 定义一些游戏中必要的元素和变量
    score = 0
    score_board = Scoreboard(cfg.IMAGE_PATHS['numbers'], position=(534, 15), bg_color=cfg.BACKGROUND_COLOR)
    highest_score = highest_score
    highest_score_board = Scoreboard(cfg.IMAGE_PATHS['numbers'], position=(435, 15), bg_color=cfg.BACKGROUND_COLOR, is_highest=True)
    rabbit = Rabbit(cfg.IMAGE_PATHS['rabbit'])
    ground = Ground(cfg.IMAGE_PATHS['ground'], position=(0, cfg.SCREENSIZE[1]))
    #sky = Sky(cfg.IMAGE_PATHS['sky'], position=(0, cfg.SCREENSIZE[0]))
    #创建精灵组统一管理图片
    cloud_sprites_group = pygame.sprite.Group()
    obstacle_sprites_group = pygame.sprite.Group()
    bird_sprites_group = pygame.sprite.Group()
    food_sprites_group = pygame.sprite.Group()
    generate_food_freq = random.randint(10, 20)
    generate_food_count = 0
    add_obstacle_timer = 0
    score_timer = 0
    # 当前得分/历史最高分数
    carrotNum = 0
    # 游戏主循环
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    rabbit.jump(sounds)
                elif event.key == pygame.K_DOWN:
                    rabbit.duck()
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                rabbit.unduck()
        #背景上色
        screen.blit(background, (0, 0))  # 对齐的坐标
        #screen.fill(cfg.BACKGROUND_COLOR)
        # --随机添加云
        if len(cloud_sprites_group) < 5 and random.randrange(0, 300) == 10:
            cloud_sprites_group.add(Cloud(cfg.IMAGE_PATHS['cloud'], position=(cfg.SCREENSIZE[0], random.randrange(30, 175)),size=[(70, 70)] ))
        # --随机添加树桩/石块/灌木、飞鸟
        add_obstacle_timer += 1
        if add_obstacle_timer > random.randrange(50, 150):
            add_obstacle_timer = 0
            random_value = random.randrange(0, 10)
            if random_value >= 5 and random_value <= 7:
                obstacle_sprites_group.add(Obstacle(cfg.IMAGE_PATHS['obstacle']))
            elif random_value >= 8 and random_value <= 10:
                position_ys = [cfg.SCREENSIZE[1]*0.67, cfg.SCREENSIZE[1]*0.3, cfg.SCREENSIZE[1]*0.5]
                bird_sprites_group.add(Bird(cfg.IMAGE_PATHS['bird'], position=(800, random.choice(position_ys))))
            else:
                food_sprites_group.add(Food(cfg.IMAGE_PATHS['carrot']))

        # --更新食物
        for food in food_sprites_group:
           if food.update(): food_sprites_group.remove(food)
        # --更新游戏元素
        ground.update()
        rabbit.update()

        cloud_sprites_group.update()
        obstacle_sprites_group.update()
        bird_sprites_group.update()
        score_timer += 1
        if score_timer > (cfg.FPS//12):
            score_timer = 0
            score += 1
            score = min(score, 99999)
            if score > highest_score:
                highest_score = score
            if score % 100 == 0:
                sounds['point'].play()
            if score % 1000 == 0:
                ground.speed -= 1
                for item in cloud_sprites_group:
                    item.speed -= 1
                for item in obstacle_sprites_group:
                    item.speed -= 1
                for item in bird_sprites_group:
                    item.speed -= 1
        # --碰撞检测
        #检测所有障碍物是否碰到兔子
        for item in obstacle_sprites_group:
            if pygame.sprite.collide_mask(rabbit, item):
                rabbit.die(sounds)
                #检测所有飞鸟是否碰到兔子
        for item in bird_sprites_group:
            if pygame.sprite.collide_mask(rabbit, item):
                rabbit.die(sounds)
        #胡萝卜是否碰到兔子
        for food in food_sprites_group:
            if pygame.sprite.collide_mask(rabbit, food):
                #game_sounds['get'].play()
                food.eat(sounds)
                food_sprites_group.remove(food)
                carrotNum += food.score
                if carrotNum > highest_score: highest_score = score
        # --将游戏元素画到屏幕上
        ground.draw(screen)
        rabbit.draw(screen)

        cloud_sprites_group.draw(screen)
        obstacle_sprites_group.draw(screen)
        bird_sprites_group.draw(screen)
        food_sprites_group.draw(screen)
        score_board.set(score)
        highest_score_board.set(highest_score)
        score_board.draw(screen)
        highest_score_board.draw(screen)
        # --显示得分数
        score_text = f'Carrot: {carrotNum}, Journey: {highest_score}'
        score_text = font.render(score_text, True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.topleft = [5, 5]
        screen.blit(score_text, score_rect)
        # --更新屏幕
        pygame.display.update()
        clock.tick(cfg.FPS)
        # --游戏是否结束
        if rabbit.is_dead:
            break
    # 游戏结束界面
    return GameEndInterface(screen, cfg), highest_score


'''run'''
if __name__ == '__main__':
    highest_score = 0
    while True:
        flag, highest_score = main(highest_score)
        if not flag: break