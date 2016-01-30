from gpiozero import LED, Button
from time import sleep
import random

inputpins = [7, 8, 9, 10]
outputpins = [22, 23, 24, 25]
buttons = [Button(pin) for pin in inputpins]
leds = [LED(pin) for pin in outputpins]

def pattern_generator():
    global pattern
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
    global detected_pattern
    detected_pattern = []
    for pin in pattern:
        detected = detect_input()
        if detected == pin:
            detected_pattern.extend([detected])
        else:
            break

def game_setup():
    global pattern, score, lives, speed
    score = 0
    lives = 3
    speed = 0.85
    pattern = []
    while (len(pattern) != 3):
        pattern_generator()

def game_menu():
    global game_over
    print("Press the left button to start,")
    print("or any other button to exit")
    detected = detect_input()
    if detected == 0:
        game_setup()
        game_over = False
    else:
        game_over = True

print("How good is your memory?")
game_menu()
while not game_over:
    play_pattern()
    detect_pattern()
    if pattern != detected_pattern:
        lives -= 1
        if lives == 0:
            print("\nYour score is %d\n" % score)
            game_menu()
    else:
        score += 10
        if speed >= 0.4:
            speed = (speed * 0.80)
        pattern_generator()
