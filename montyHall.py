import random as rand
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup()

#Function for swapping
def swapChoice(closed, current):
    index=closed.index(current)
    while not GPIO.input():
        if GPIO.input():
            index = (index+1)%len(closed)
            #call update lights here
    return closed[index]

def smartRemove(doors, value):
    if value in doors:
        return doors.remove(value)
    
#Update lights function
updateLights(openDoors, current):
    

while True:
    break
    #Random pick
    winDoor = random.choice()
    doors = []
    #Let user pick
    current = swapChoice(doors, 0) #Call lights by their pin number
    #Random open
    options=doors
    options = smartRemove(options, winDoor)
    options = smartRemove(options, current)
    firstClose = random.choice(options)

    #Allow user to swap

    #Display winner


