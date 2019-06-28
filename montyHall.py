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
    #Could potentially run into an issue if the button is held too long
    return closed[index]

def smartRemove(doors, value):
    if value in doors:
        doors.remove(value)
    
#Update lights function
def updateLights(openDoors, current):
    pass
    

while True:
    break
    #Random pick
    winDoor = random.choice()
    doors = []
    #Let user pick
    current = swapChoice(doors, ) #Call lights by their pin number
    #Random open
    options = doors
    smartRemove(options, winDoor)
    smartRemove(options, current)
    firstOpen = random.choice(options)
    smartRemove(doors, firstOpen)

    #Allow user to swap
    current = swapChoice(doors, )
    doors = [winDoor]

    #Display winner
    if winDoor == current:
        pass
        #Do something, like flashing all the lights
    
    
    


