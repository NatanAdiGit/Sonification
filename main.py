import pandas as pd
import pygame
from pygame import *
import time
import sys

column_name = 'Category: All categories'

covid_list = pd.read_csv('excel/covid.csv')[column_name].tolist()[2:]

lockdown_list = pd.read_csv('excel/lockdown.csv')[column_name].tolist()[2:55]

women_data_list = [pd.read_csv('excel/domesticviolence.csv')[column_name].tolist()[2:55],
                pd.read_csv('excel/helpforwomen.csv')[column_name].tolist()[2:55],
                pd.read_csv('excel/womenhomicide.csv')[column_name].tolist()[2:55],
                pd.read_csv('excel/womensshelter.csv')[column_name].tolist()[2:55],
                pd.read_csv('excel/financialaid.csv')[column_name].tolist()[2:55]]

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)

sound_1 = pygame.mixer.Sound('sounds/sound_one.mp3')
sound_2 = pygame.mixer.Sound('sounds/sound_two.mp3')


def get_average_data_list():
    av_data_list = []
    for i in range(52):

        # get the average of all the samples from the data about women
        average = 0
        for j in range(5):
            average += float(women_data_list[j][i])
        average = average / 5

        # set the volume param according to the average
        if average <= 45:
            av_data_list.append(0.2)
        elif average <= 50:
            av_data_list.append(0.3)
        elif average <= 55:
            av_data_list.append(0.4)
        elif average <= 60:
            av_data_list.append(0.6)
        elif average <= 65:
            av_data_list.append(0.8)
        else:
            av_data_list.append(1)
    return av_data_list


def pause(sec):
    time_end = time.time() + sec
    while time.time() < time_end:
        continue


def play_data(av_data_list):
    sound_1.play()
    for j in range(52):
        sound_1.set_volume(av_data_list[j])

        sound_2.set_volume(float(covid_list[j]) / 100)
        sound_2.play()

        value = float(lockdown_list[j])
        if value <= 2:
            pause(1.4)
        elif value <= 2:
            pause(1.2)
        elif value <= 4:
            pause(1.1)
        elif value <= 6:
            pause(1)
        elif value <= 8:
            pause(0.9)
        elif value <= 10:
            pause(0.8)
        elif value <= 30:
            pause(0.7)
        else:
            pause(0.6)


if __name__ == '__main__':
    average_data_list = get_average_data_list()
    print(average_data_list)
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
                    play_data(average_data_list)
        pygame.display.update()
