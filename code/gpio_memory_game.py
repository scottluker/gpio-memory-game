from gpiozero import LED, Button
from time import sleep
import random

inputpins = [7, 8, 9, 10]
outputpins = [22, 23, 24, 25]
button = [Button(pin) for pin in inputpins]
led = [LED(pin) for pin in outputpins]

# Order of colors, from left to right
red = 0 # First
blue = 1 # Second
green = 2 # Third
yellow = 3 # Forth
colors = [red, blue, green, yellow]

def pattern_generator(n):
    global pattern
    for i in range(n):
        pattern.extend([random.choice(colors)])

def play_pattern():
    for color in pattern:
        sleep(speed)
        led[color].on()
        sleep(speed)
        led[color].off()

def detect_input():
    while True:
        for color in colors:
            if button[color].is_pressed:
                sleep(0.3)
                return color

def detect_pattern():
    for color in pattern:
        if detect_input() != color:
            return False
    return True

def game_setup():
    global pattern, score, lives, speed, difficulty
    lives = 3
    speed = 0.8
    difficulty = 1
    score = 0
    pattern = []
    pattern_generator(difficulty)

def game_menu():
    global game_running
    print("\nPress the Red button to start,")
    print("or any other button to exit")
    if detect_input() == red:
        game_setup()
        game_running = True
    else:
        game_running = False

print("How good is your memory?")
game_menu()
while game_running:
    play_pattern()
    if detect_pattern():
        score += 10
        if speed >= 0.2:
            speed = (speed * 0.8)
        pattern_generator(difficulty)
    else:
        lives -= 1
    sleep(0.5)
    if lives == 0:
        print("\nYour score is %s points" % score)
        game_menu()
