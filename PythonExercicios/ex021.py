# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
#*-coding:utf-8;-*
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
stop = input('Digite algo para parar...')