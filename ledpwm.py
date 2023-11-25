import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)
def change_brightness(duty_cycles, wait_time):
        for dc in duty_cycles:
                pwm.ChangeDutyCycle(dc)
                time.sleep(wait_time)
        duty_cycles = [0, 25, 50, 75, 100]
try:
        while True:
                change_brightness(duty_cycles, 1)
except KeyboardInterrupt:
        print("Exiting the program")
finally:
        pwm.stop()
        GPIO.cleanup()
        print("GPIO pins cleaned up")

