import time 
import RPi.GPIO as GPIO

# use BCM GPIO references instead of physical pin numbers. 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Define GPIO to use on PI. 
GPIO_TRIGGER = 23
GPIO_ECHO = 24


def init_pin():
    """
    initializes pins. Which pin is for in and which for out. 
    sleeping for half a second after. 
    """
    #print("Setting up.")
    # set pins as output and inputs.
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # set trigger to False (low)
    GPIO.output(GPIO_TRIGGER, False)
    
    #print("Allowing it to settle")
    # Allow module to settle
    time.sleep(0.5)


def start():
    """
    Used to trigger the pin.
    sends the signal for i microcenter. 
    turns the pin off. 
    """
    print("Starting read process")
    # Send 10us pulse to trigger. 
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)


def read_results():
    """
    Used to calcaulte the time it took for the sound to come back. 
    when the pin is triggered it starts time. 
    when the pin is no triggered it stops time.

    Returns: elapsed time : stop time - start time.
    """
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        pass
    stop = time.time()
    # calculate pulse length. 
    elapsed = stop - start
    return elapsed


def get_distance(elapsed):
    """
    using the constant for speed of sound at sea level. 
    This speed is convered from m to cm. 
    distance divided in half, since it has to reach the target and come
    back. 
    
    :return: distance in cm. 

    """
    # Distance pulse travelled in that time. 
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300

    # distance is the for there and back. need to half it. 
    distance = distance / 2
    distance = round(distance, 4)
    return distance

def convert_distance(distance):
    """
    This function is used to convert distance from cm to m. 
    : distance : measurement in cm. 
    : return : distance in meters.
    """
    distance = distance / 100
    return distance


def main():
    """
    Main method. used to execute the program. 
    Creating an infinite loop to get a continued flow of
    reading.
    will stop when used pressed CTRL+C. 
    Resets GPIO. 

    """
    try:
        while True:

            init_pin()
            start()
            
            elapsed_time = read_results()
            distance = get_distance(elapsed_time)
            
            print 'Distance', distance, 'cm'
            meters = convert_distance(distance)
            print "Distance", meters, "m"

            print "Press CTRL+C to stop. \n" 
            time.sleep(1)

    # press CTRL+C to exit.
    except KeyboardInterrupt:
        print "\nUser stopped measurement."
        # reste the GPIO settings . 
        GPIO.cleanup()

if __name__ == '__main__':
    main()

"""
Resources: 
    * For the inifite loop:  
   https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
    * How to use the sensor: 
    https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiBhsHSpY3gAhUQc98KHYPGAp8QjRx6BAgBEAU&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DeQBcgYyB1vk&psig=AOvVaw1TrRnDH6ukVcxJ-bRVRug6&ust=1548632878538339
    * Forum that helped answer GPIO question: 
    https://www.raspberrypi.org/forums/viewtopic.php?t=185195
"""
