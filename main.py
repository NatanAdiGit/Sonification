import pandas as pd
import pygame
from pygame import *
from random import uniform
import time
import sys

column_name = 'Category: All categories'

covid_list = pd.read_csv('excel/covid.csv')[column_name].tolist()[2:]
print(len(covid_list))

lockdown_list = pd.read_csv('excel/lockdown.csv')[column_name].tolist()[2:55]

domestic_violence_list = pd.read_csv('excel/domesticviolence.csv')[column_name].tolist()[2:55]
help_for_women_list = pd.read_csv('excel/helpforwomen.csv')[column_name].tolist()[2:55]
women_homicide_list = pd.read_csv('excel/womenhomicide.csv')[column_name].tolist()[2:55]
womens_shelter_list = pd.read_csv('excel/womensshelter.csv')[column_name].tolist()[2:55]
finantial_aid_list = pd.read_csv('excel/finantialaid.csv')[column_name].tolist()[2:55]

data_list = []

# print(len(domestic_violence_list))
# print(len(help_for_women_list))
# print(len(women_homicide_list))
# print(len(womens_shelter_list))
# print(len(finantial_aid_list))

for i in range(52):
    average = (int(domestic_violence_list[i]) + int(help_for_women_list[i]) +
               int(women_homicide_list[i]) + int(womens_shelter_list[i]) + int(finantial_aid_list[i])) / 5.0
    if average <= 45:
        data_list.append(0.2)
    elif average <= 50:
        data_list.append(0.4)
    elif average <= 55:
        data_list.append(0.6)
    elif average <= 60:
        data_list.append(0.8)
    else:
        data_list.append(1)


pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

sound_1_list = [pygame.mixer.Sound('sounds/sound_101.mp3'),
                pygame.mixer.Sound('sounds/sound_102.mp3'),
                pygame.mixer.Sound('sounds/sound_103.mp3'),
                pygame.mixer.Sound('sounds/sound_104.mp3'),
                pygame.mixer.Sound('sounds/sound_105.mp3')]

sound_2 = pygame.mixer.Sound('sounds/sound_111.mp3')

screen = pygame.display.set_mode((400, 400), 0, 32)

# print(lockdown_list)
print(data_list)


def pause(sec):
    time_end = time.time() + sec
    while time.time() < time_end:
        continue


def play_data():
    for j in range(52):
        index = j % 5
        sound_1 = sound_1_list[index]
        sound_1.set_volume(data_list[j])
        sound_1.play()

        sound_2.set_volume(float(covid_list[j]) / 100)
        sound_2.play()

        time_gap = 0
        if index == 4:
            time_gap = 0.8

        value = float(lockdown_list[j])
        if value <= 10:
            pause(2.0 - time_gap)
        elif value <= 20:
            pause(1.9 - time_gap)
        elif value <= 50:
            pause(1.8 - time_gap)
        else:
            pause(1.7 - time_gap)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_UP:
                play_data()
                # while ch.get_busy():
                #     pygame.time.delay(100)
    pygame.display.update()
