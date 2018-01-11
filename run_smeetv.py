# run_smeetv.py
# Written by Matthew Timms

import pygame
from pygame.locals import *
import time
import random
import collect_imgs
import sys


def display_img(file_addr, delay=5):
    img = pygame.image.load(file_addr)
    img = pygame.transform.scale(img, (1920, 1080))
    windowSurface.blit(img, (0, 0))  # Replace (0, 0) with desired coordinates
    pygame.display.flip()
    time.sleep(delay)

pygame.init()
WIDTH = 1920
HEIGHT = 1080
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN, 32)
pygame.mouse.set_visible(0)


file_search_key = ['.jpg', '.png']
adv_imgs = collect_imgs.collect_imgs('.', file_search_key, 0)
std_imgs = collect_imgs.collect_imgs('smeetv/', file_search_key)

ad_count = 10
img_no = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(1)

    if ad_count == 10:
        #For important pics add them here w/ display_img(). Second input is time delay
        for x in xrange(0, len(adv_imgs)):
            display_img(adv_imgs[x], delay=8)
        ad_count = 0

    img_no = random.randrange(1, len(std_imgs))  # Comment out for not-random sequence
    try:
        display_img(std_imgs[img_no], 5)
        ad_count += 1
        img_no += 1
    except:
        img_no = 0
