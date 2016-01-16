#!/usr/bin/env python
# GPIO Memory Game Script By Scott Luker
# https://github.com/scottluker

from gpiozero import LED, Button
from time import sleep
import random

setup = [3, 850, 3]
inputpins= [7, 8, 9, 10]
outputpins = [22, 23, 24, 25]
buttons = [Button(pin=pin, bounce_time=0.2) for pin in inputpins]
leds = [LED(pin) for pin in outputpins]

def pattern_generator():
    global pattern
    pattern.extend([random.randint(0,3)])

def play_pattern():
    sleep(0.5)
    for pin in pattern:
        sleep(speed / 1000.0)
        leds[pin].on()
        sleep(speed / 1000.0)
        leds[pin].off()

def detect_input():
    while True:
        if buttons[0].is_pressed:
            sleep(0.2)
            return 0
        elif buttons[1].is_pressed:
            sleep(0.2)
            return 1
        elif buttons[2].is_pressed:
            sleep(0.2)
            return 2
        elif buttons[3].is_pressed:
            sleep(0.2)
            return 3

def detect_pattern():
    global detected_pattern
    detected_pattern = []
    for pin in pattern:
        detected = detect_input()
        if detected == pin:
            detected_pattern.extend([pin])
        else:
            break

def game_setup():
    global pattern, completed, lives, speed
    pattern = []
    completed = 0
    lives = setup[0]
    speed = float(setup[1])
    while (len(pattern) != setup[2]):
        pattern_generator()

def game_intro():
    print ("How Good Is Your Memory?")
    print ("Press Left Button To Start")
    buttons[0].wait_for_press()

def game_over():
    print ("\n Your Score Is %d") % (completed * 10)
    print ("Press Left Button To Play Again \n")
    buttons[0].wait_for_press()
    game_setup()

game_setup()
game_intro()
while True:
    play_pattern()
    detect_pattern()
    if pattern != detected_pattern:
        lives -= 1
        if lives == 0:
            game_over()
    else:
        completed += 1
        if speed > 0.2:
            speed = (speed * 0.80)
        pattern_generator()
