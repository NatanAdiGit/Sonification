import pandas as pd
import pygame
from pygame import *
from random import uniform
import time
import sys


column_name = 'Category: All categories'

lockdown_list = pd.read_csv('excel/lockdown.csv')[column_name].tolist()[2:57]

data_list = [pd.read_csv('excel/domesticviolence.csv')[column_name].tolist()[2:57],
             pd.read_csv('excel/helpforwomen.csv')[column_name].tolist()[2:57],
             pd.read_csv('excel/womenhomicide.csv')[column_name].tolist()[2:57],
             pd.read_csv('excel/womensshelter.csv')[column_name].tolist()[2:57],
             pd.read_csv('excel/finantialaid.csv')[column_name].tolist()[2:57]]

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
sounds = [pygame.mixer.Sound('sounds/203486__tesabob2001__d3.mp3'),
          pygame.mixer.Sound('sounds/203463__tesabob2001__b3.mp3'),
          pygame.mixer.Sound('sounds/203459__tesabob2001__a-5.mp3'),
          pygame.mixer.Sound('sounds/203501__tesabob2001__f-3.mp3'),
          pygame.mixer.Sound('sounds/203493__tesabob2001__g3.mp3')]

screen = pygame.display.set_mode((400,400), 0, 32)


print(lockdown_list)


def pause(sec):
    time_end = time.time() + sec
    while time.time() < time_end:
        continue


def play_data():
    for i in range(55):
        for j in range(5):
            sounds[j].set_volume(float(data_list[j][i])/100)
            sounds[j].play()
            # if (j == 2):
            #     pause(0.25)
            # else:
            value = float(lockdown_list[i])
            if (value <= 10):
                    pause(0.25 + (0.1 - (value / 100)))
                    continue
            if (value <= 20):
                    pause(0.25)
                    continue
            if (value <= 30):
                    pause(0.22)
                    continue
            pause(0.17)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            elif event.key==K_UP:
                play_data()
                # while ch.get_busy():
                #     pygame.time.delay(100)
    pygame.display.update()



