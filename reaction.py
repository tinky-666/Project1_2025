from gpiozero import LED, Button from time import sleep
from random import uniform
led=LED(4)
right_button= Button15)
left_button = Button(14)
led.on0
sleep(uniform(5,10)
led.off0
def pressed(button):
    print(str(button.pin.number) + ' won the game')
right_button.when_pressed = pressed
left_button.when_pressed = pressed
while True:
    sleep(0.1)
