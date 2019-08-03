#!/usr/bin/python3
import RPi.GPIO as gpio
import time
import sys

buzz = 14
gpio.setmode(gpio.BCM)
gpio.setup(buzz, gpio.OUT)

alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}


def sound(dauer, freq=0.001):
    cycles = int(dauer * 1 / freq)
    for i in range(cycles):
        gpio.output(buzz, gpio.HIGH)
        time.sleep(freq)
        gpio.output(buzz, gpio.LOW)
        time.sleep(freq)


if __name__ == '__main__':
    wort = sys.argv[1]
    for stelle, buchstabe in enumerate(wort):
        tonfolge = alphabet[buchstabe.upper()]
        print(buchstabe, "ist", tonfolge)
        for ton in tonfolge:
            if ton == "-":
                sound(0.3, 0.003)
            elif ton == ".":
                sound(0.1, 0.001)
            time.sleep(0.1)
        time.sleep(0.5)
