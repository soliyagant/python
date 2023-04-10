import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


def dec2bin(decimal):
    return[int(i) for i in bin(decimal)[2:].zfill(bits)]


def adc(): #десятичное число, пропорц. напр на тройка-модуле
    min = 0
    max = 255
    while (max - min > 1):
        middle = (max + min) // 2
        GPIO.output(dac, dec2bin(int(middle)))
        time.sleep(0.007)
        if GPIO.input(comp) == 0:
            max = middle
        else:
            min = middle
    return min


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka,GPIO.OUT, initial = GPIO.HIGH)

bits = len(dac)
levels = 2**bits
max_v = 3.3


try:
    while True:
        exit_value = adc()
        voltage = exit_value / levels * max_v
        signal = dec2bin(exit_value)
        print(voltage, signal)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()