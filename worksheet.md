# GPIO Memory Game

In this resource, you will create a memory game in Python with your Raspberry Pi and a selection of electronic components. You also will be using the GPIO Zero library, which means you can easily control the Raspberry Pi's GPIO pins from your program to turn LEDs on or off and detect when a button has been pressed.

## Connecting The Components

To begin, you're going to connect all the components together with your Raspberry Pi.

1. Start by placing the buttons into your breadboard, as shown below:

![](images/gpio-memory-game_1.png)

2. Next, place the resistors

![](images/gpio-memory-game_2.png)

3. Now place the LEDs into your breadboard. As LEDs are a polarized component, you must make sure the long leg is placed...

![](images/gpio-memory-game_3.png)

4. Finally, add jumper leads to connect all the components to your Raspberry Pi.

![](images/gpio-memory-game_4.png)

## create pattern_generator() and play_pattern()

```Python
from gpiozero import LED
from time import sleep
import random
```
```Python
outputpins = [22, 23, 24, 25]
leds = [LED(pin) for pin in outputpins]
```

```Python
def pattern_generator(number):
    global pattern
    for i in range(number):
        pattern.extend([random.randint(0,3)])
```

```Python
def play_pattern():
    for pin in pattern:
        sleep(speed)
        leds[pin].on()
        sleep(speed)
        leds[pin].off()
```


## create detect_input() and detect_pattern()

```Python
from gpiozero import LED, Button
```

```Python
inputpins = [7, 8, 9, 10]
outputpins = [22, 23, 24, 25]
buttons = [Button(pin) for pin in inputpins]
leds = [LED(pin) for pin in outputpins]
```

```Python
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
```

```Python
def detect_pattern():
    for pin in pattern:
        if detect_input() != pin:
            return False
    return True
```

## Testing The Code So Far

## create game_setup(), game_menu() and game while loop

## complete code


## What's next?

- You could create an extra menu to change the round speed, difficulty and player's lives.
