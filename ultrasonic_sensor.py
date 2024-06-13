import logging
import RPi.GPIO as GPIO
import time
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

class UltrasonicSensor(NeuronModule):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.trigger_pin = kwargs.get('trigger_pin', None)
        self.echo_pin = kwargs.get('echo_pin', None)
        
        if self.trigger_pin is None or self.echo_pin is None:
            raise InvalidParameterException("Trigger pin and Echo pin must be provided")
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

        distance = self.get_distance()
        self.say(distance)
        self.cleanup()

    def get_distance(self):
        # Set trigger to HIGH
        GPIO.output(self.trigger_pin, True)
        # Set trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        # Save start_time
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        # Save stop_time
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # Time difference between start and arrival
        time_elapsed = stop_time - start_time
        # Multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (time_elapsed * 34300) / 2

        return distance

    def cleanup(self):
        GPIO.cleanup()

    def say(self, distance):
        message = f"Distance: {distance:.1f} cm"
        self.say(message)
        logger.info(message)
