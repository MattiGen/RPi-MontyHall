import random as rand
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#Function for swapping
def swapChoice(closed, current):
    index=closed.index(current)
    while not GPIO.input():
        if GPIO.input():
            index = (index+1)%len(closed)
            updateChosed(closed[index])
    #Could potentially run into an issue if the button is held too long
    return closed[index]

def smartRemove(doors, value):
    if value in doors:
        doors.remove(value)
    
#Update lights function
def closeDoor(closed):
    GPIO.output(closed, False)
    
def updateChosen(current):
    toggleDoors(False)
    if current == 29:
        GPIO.output(11, val)
    elif current == 31:
        GPIO.output(13, val)
    else:
        GPIO.output(15, val)
    
    
    
def toggleDoors(val):
    GPIO.output(29, val)
    GPIO.output(31, val)
    GPIO.output(33, val)
        
    
#DEfault pins, red: 29, green: 31 blue: 33
#RGB pins: red:11, green:13, blue15


while True:
    toggleDorrs(True)
    #Random pick
    winDoor = random.choice()
    doors = [29,31,33]
    #Let user pick
    current = swapChoice(doors, 29) #Call lights by their pin number
    #Random open
    options = doors
    smartRemove(options, winDoor)
    smartRemove(options, current)
    firstOpen = random.choice(options)
    closeDoor(firstOpen)
    smartRemove(doors, firstOpen)

    #Allow user to swap
    current = swapChoice(doors, current)
    toggleDoors(False)
    GPIO.output(winDoor, True)

    #Display winner
    if winDoor == current:
        input("Congrats! Press any key to continue")
        #Do something, like flashing all the lights
    else:
        input("You Lose! Press any key to continue")
    
    
    


