import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 100)

noten = {
    "c": 261,
    "d": 294,
    "e": 329,
    "f": 349,
    "g": 392,
    "a": 440,
    "b": 493,
}

entchen = "cdefGGaaaaGPaaaaGPffffEEpddddC"

speed = 0.3
if __name__ == '__main__':
    GPIO.output(12, True)
    p.start(20)  # 10% duty cycle sounds 'ok'

    for note in entchen:
        if note.lower() == "p":
            if note.islower():
                time.sleep(0.1)
            else:
                time.sleep(0.2)
        else:
            p.ChangeDutyCycle(20)
            p.ChangeFrequency(noten[note.lower()])
            if note.islower():
                time.sleep(speed)
            else:
                time.sleep(speed * 2)
            p.ChangeDutyCycle(0)
        time.sleep(0.1)

    p.stop()
    GPIO.cleanup()
