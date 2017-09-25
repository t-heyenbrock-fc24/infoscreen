#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
#GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24

#Richtung der GPIO-Pins festlegen (IN / OUT)
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)

class Distance:
    # Constructor
    def __init__(self, pinTrigger, pinEcho, throttle_time):
        self.pinTrigger = pinTrigger
        self.pinEcho = pinEcho
        self.throttle_time = throttle_time
        self.last_update_current = 0
        self.current_distance = 0

    def compute_distance(self):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.pinTrigger, GPIO.OUT)
        GPIO.setup(self.pinEcho, GPIO.IN)
        
        # setze Trigger auf HIGH
        GPIO.output(self.pinTrigger, True)
        
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(self.pinTrigger, False)
        
        startTime = time.time()
        stopTime = time.time()
        
        # speichere Startzeit
        while GPIO.input(self.pinEcho) == 0:
            startTime = time.time()
        
        # speichere Ankunftszeit
        while GPIO.input(self.pinEcho) == 1:
            stopTime = time.time()
        
        # Zeit Differenz zwischen Start und Ankunft
        timeElapsed = stopTime - startTime
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        return (timeElapsed * 34300) / 2

    def get_distance(self):
        if time.time() - self.last_update_current < self.throttle_time:
            return self.current_distance
        self.current_distance = self.compute_distance()
        self.last_update_current = time.time()
        return self.current_distance
