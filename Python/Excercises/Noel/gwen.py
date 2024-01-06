import random
from os import system
from time import sleep

colors = [
    '\033[30m', '\033[31m',
    '\033[32m', '\033[33m',
    '\033[34m', '\033[35m',
    '\033[36m', '\033[37m',
    '\033[38m', '\033[39m',
]

system('')

f = open('Excercises/Noel/Gwen.txt', 'r')
santa_claus = f.read()

while True:
    i = random.randint(0, 9)
    print(colors[i] + santa_claus)
    sleep(2)
    # system('clear')