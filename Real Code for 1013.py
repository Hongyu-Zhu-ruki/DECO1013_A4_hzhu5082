from microbit import *
import speech
speech.say("hello!")

while True:
    if accelerometer.was_gesture('face up'):
        pin1.write_analog(500)
        sleep(300)
        display.show(Image.HAPPY)
    if accelerometer.is_gesture('face down'):
        display.show(Image.SAD)
        pin1.write_analog(500)
    if accelerometer.was_gesture('shake'):
        display.show(Image.SAD)
        pin1.write_analog(500)
        sleep(2000)
    if accelerometer.was_gesture('right'):
        display.show(Image.SAD)
        pin1.write_analog(500)
        sleep(1000)
    if accelerometer.was_gesture('left'):
        display.show(Image.SAD)
        pin1.write_analog(500)
        sleep(1000)
    if accelerometer.was_gesture('up'):
        display.show(Image.SAD)
        pin1.write_analog(500)
        sleep(1000)
    if accelerometer.was_gesture('down'):
        display.show(Image.SAD)
        pin1.write_analog(500)
        sleep(1000)
    if accelerometer.is_gesture('3g'):
        display.show(Image.ANGRY)
        speech.say("No!")
        pin1.write_analog(500)
        sleep(2000)
    elif button_b.is_pressed():
        display.show(Image.ASLEEP)
        speech.say("bye!")
        pin1.write_analog(500)
        sleep(500)
        pin1.write_analog(0)
        break
    else:
        pin1.write_analog(0)

display.clear()