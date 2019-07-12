import random
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Function for swapping
def swapChoice(closed, current):
    index=closed.index(current)
    while not GPIO.input(16):
        if GPIO.input(18):
            index = (index+1)%len(closed)
            updateChosen(closed[index])
            while GPIO.input(18):
                pass
    while GPIO.input(16):
        pass
                
    #Could potentially run into an issue if the button is held too long
    return closed[index]

def smartRemove(doors, value):
    if value in doors:
        doors.remove(value)
    
#Update lights function
def closeDoor(closed):
    GPIO.output(closed, False)
    
def updateChosen(current):
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    if current == 29:
        print('red')
        GPIO.output(11, True)
    elif current == 31:
        print('green')
        GPIO.output(13, True)
    else:
        print('blue')
        GPIO.output(15, True)
    
    
    
def toggleDoors(val):
    GPIO.output(29, val)
    GPIO.output(31, val)
    GPIO.output(33, val)
        
    
#DEfault pins, red: 29, green: 31 blue: 33
#RGB pins: red:11, green:13, blue15


while True:
    toggleDoors(True)
    #Random pick
    doors = [29,31,33]
    winDoor = random.choice(doors)
    #Let user pick
    current = swapChoice(doors, 29) #Call lights by their pin number
    #Random open
    options = [29, 31, 33]
    smartRemove(options, winDoor)
    smartRemove(options, current)
    firstOpen = random.choice(options)
    closeDoor(firstOpen)
    print(doors)
    smartRemove(doors, firstOpen)
    print(doors)
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
    
    
    


