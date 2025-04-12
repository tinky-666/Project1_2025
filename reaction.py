from gpiozero import LED, Button
from time import sleep
from random import uniform
import sys

led = LED(4)
right_button = Button(15)
left_button = Button(14)
game_active = False

left_name = input('Left player name: ')
right_name = input('Right player name: ')

def pressed(button):
 if game_active:
    winner = left_name if button.pin.number == 14 else right_name
    print(f"{winner} won the game!")

right_button.when_pressed = pressed
left_button.when_pressed = pressed

try:
   while True:
     print("Get ready...")
     led.on()
     game_active =False
     sleep(uniform(5, 10))
     led.off()
     game_active = True
     sleep(3) 
except KeyboardInterrupt:
  led.close()
  right_button.close()
  left_button.close()
  sys.exit(0)
