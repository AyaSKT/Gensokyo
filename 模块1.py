# coding:utf8
import pygame.constants
import sys

# 初始化pygame
pygame.init()
# 变量定义
size = width, height = 600, 400
bg = (255, 255, 255)

# 加载一个图片对象
img1 = pygame.image.load("123.jpg")
# 获取图像的位置
position = img1.get_rect()
# 创建一个游戏窗口
screen = pygame.display.set_mode(size)
# 游戏标题
pygame.display.set_caption("游戏title")
# 窗口想要长期存在，必须一个死循环
while True:
    # 遍历事件，当事件等于退出时，程序结束
    speed = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 键盘控制图片运动 KEYDOWN 是键盘按下的事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed[1] -= 5
            if event.key == pygame.K_DOWN:
                speed[1] += 5
            if event.key == pygame.K_LEFT:
                speed[0] -= 5
            if event.key == pygame.K_RIGHT:
                speed[0] += 5
    # 移动图像，根据上下左右的按键，改变speed，然后移动
    position = position.move(speed)
    # 填充背景
    screen.fill(bg)
    # 放置图片在移动后的位置，如果没有移动，就在初始位置。
    screen.blit(img1, position)
    # 更新界面
    pygame.display.flip()
