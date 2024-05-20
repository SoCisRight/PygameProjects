'''配置文件'''
import os


'''屏幕大小'''
SCREENSIZE = (800, 500)
'''FPS速度'''
FPS = 60
'''音频素材路径'''
AUDIO_PATHS = {
    'bgm': os.path.join(os.getcwd(), 'resources/audios/bgm.wav'),
    'die': os.path.join(os.getcwd(), 'resources/audios/die.wav'),
    'jump': os.path.join(os.getcwd(), 'resources/audios/jump.wav'),
    'point': os.path.join(os.getcwd(), 'resources/audios/point.wav'),
    'get': os.path.join(os.getcwd(), 'resources/audios/get.wav')
}
'''图片素材路径'''
IMAGE_PATHS = {
    #障碍物
    'obstacle': [
        os.path.join(os.getcwd(), 'resources/images/muzhuang.png'),
        os.path.join(os.getcwd(), 'resources/images/cao.png'),
        os.path.join(os.getcwd(), 'resources/images/stone.png')
    ],
    #云
    'cloud': os.path.join(os.getcwd(), 'resources/images/cloud.png'),
    #兔子
    'rabbit': [
        os.path.join(os.getcwd(), 'resources/images/rabbit.png'),
        os.path.join(os.getcwd(), 'resources/images/dino_ducking.png')
    ],
    #结束
    'gameover': os.path.join(os.getcwd(), 'resources/images/end.png'),
    #开始
    'gamestart': os.path.join(os.getcwd(), 'resources/images/start.png'),
    #地板
    'sky': os.path.join(os.getcwd(), 'resources/images/background.png'),
    'ground': os.path.join(os.getcwd(), 'resources/images/ground.png'),
    #移动距离
    'numbers': os.path.join(os.getcwd(), 'resources/images/numbers.png'),
    #飞鸟
    'bird': os.path.join(os.getcwd(), 'resources/images/bird.png'),
    #胡萝卜
    'carrot': os.path.join(os.getcwd(), 'resources/images/carrot.png'),
    #苹果
    'apple': os.path.join(os.getcwd(), 'resources/images/apple.png'),
    #重玩，改成下一关
    'replay': os.path.join(os.getcwd(), 'resources/images/restart.png')
}
'''字体路径'''
FONT_PATH = os.path.join(os.getcwd(), 'resources/font/font.TTF')
'''背景颜色'''
BACKGROUND_COLOR = (235, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)