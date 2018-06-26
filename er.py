#!/usr/bin/python3.5
#This is a test to see how much faster I can read when words are flashed at me.
#By, codeDirtyToMe

from time import sleep
import os, re, argparse, time

#Create some options.
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="File to be read.")
parser.add_argument("-s", "--speed", type=float, help="Speed in words/min")
parser.add_argument("-p", "--pause", type=float, help="Pause length on end of sentences and commas.")
parser.add_argument("-x", "--exit", help="Auto exit", action="store_true")
arguments = parser.parse_args()

argFile = arguments.file
argSpeed = arguments.speed
argPause = arguments.pause
argExit = arguments.exit

def reader(readList, speed, pause):
    # Regex for finding the end of sentences or other pause inducing symbols.
    endOfSentence = re.compile(r'\.$|\?$|!$|,$|;$|:$')

    b = 1 #This will essentially be a counter that drops words off of the beginning of the scrolling text.
    os.system("clear") # Clear the screen before countdown.

    #Countdown timer.
    for t in range(3, 0, -1):
        print("Starting in " + str(t) + "\n\n\nStart reading here>>")
        sleep(1)
        os.system("clear")

    #Main loop for execution
    startTime = time.time()
    for z in range(len(readList)):

        #This first if statement controls the scrolling text.
        if z < 8 : #The first 7 words are printed one at a time for the first 7 loops.
            print(str(" ".join(readList[:z])))
        else : #This is where the scrolling text starts dropping words from the beginning of the list.
            print(str(" ".join(readList[b:z])))
            b += 1 #Drop the first word the next time around.

        #Print the word number order value followed by the corresponding word.
        print("\n\n" + str(z) + ':' + str(len(readList) - z) + "               " + readList[z])

        #If the end of a word does not end a sentence, take a short brake.
        if endOfSentence.search(readList[z]) == None :
            sleep(speed)
        else : #If a word does end a sentence, take a longer break.
            sleep(pause)

        os.system('clear')
        z += 1

    stopTime = time.time()
    totalTime = stopTime - startTime

    print("Report")
    print("# of words: " + str(len(readList)) )
    print("Time taken: " + str(totalTime))
    return

#Check to see if a file or speed was specified.
if argFile is not None :
    if os.path.exists(argFile) == True :
        # Basic import of the specified text file.
        openFile = open(argFile)
        fileList = openFile.read()
        fileWordList = fileList.split() # Make a list out out of it.
    else :
        print("Sorry, the file does not exist.")
        exit(1)
else :
    print("Please provide a file.")
    exit(1)

if argSpeed is not None :
    displaySpeed = 60 / argSpeed # 60 seconds divided by the desired words per minute.

else :
    displaySpeed = .19 # Set a default display speed if none is specified.

if argPause is not None : # Check for a pause length.
    pauseSpeed = argPause
else :
    pauseSpeed = displaySpeed # Set pause length to display speed if no pause is specified.

reader(fileWordList, displaySpeed, pauseSpeed)

if argExit is True :
    exit(0)
else :
    exitValue = input("\nPress 'X' to exit or 'R' to repeat.")

    if exitValue == 'x' or exitValue == 'X' :
        openFile.close()
        exit(0)
    elif exitValue == 'r' or exitValue == 'R' :
        reader(fileWordList, displaySpeed, pauseSpeed)
    else :
        exit(1)
