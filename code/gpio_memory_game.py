from gpiozero import LED, Button
from time import sleep
import random

inputpins = [7, 8, 9, 10]
outputpins = [22, 23, 24, 25]
buttons = [Button(pin) for pin in inputpins]
leds = [LED(pin) for pin in outputpins]

players_lives = 3
round_speed = 0.80
difficulty = 1

def pattern_generator(number):
    global pattern
    for i in range(number):
        pattern.extend([random.randint(0,3)])

def play_pattern():
    for pin in pattern:
        sleep(speed)
        leds[pin].on()
        sleep(speed)
        leds[pin].off()

def detect_input():
    while True:
        if buttons[0].is_pressed:
            sleep(0.3)
            return 0
        elif buttons[1].is_pressed:
            sleep(0.3)
            return 1
        elif buttons[2].is_pressed:
            sleep(0.3)
            return 2
        elif buttons[3].is_pressed:
            sleep(0.3)
            return 3

def detect_pattern():
    for pin in pattern:
        if detect_input() != pin:
            return False
    return True

def game_setup():
    global pattern, score, lives, speed
    lives = players_lives
    speed = round_speed
    score = 0
    pattern = []
    pattern_generator(difficulty)

def game_menu():
    global game_over
    print("\nPress the left button to start,")
    print("or any other button to exit")
    if detect_input() == 0:
        game_setup()
        game_over = False
    else:
        game_over = True

print("How good is your memory?")
game_menu()
while not game_over:
    play_pattern()
    if detect_pattern():
        score += 10
        if speed >= 0.2:
            speed = (speed * 0.80)
        pattern_generator(difficulty)
    else:
        lives -= 1
    sleep(0.5)
    if lives == 0:
        print("\nYour score is %s points" % score)
        game_menu()
