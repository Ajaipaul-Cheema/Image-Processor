# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Mohammad Haris Ahmad, Ajaipaul Cheema
# Date: December 7, 2020.
# Description: This is an Image Processor that will do manipulations based off the options you choose off of the interface

# import necessary modules, and pygame
import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog 
import pygame
pygame.display.init()
pygame.font.init()

# get the original image
originalImage = cmpt120imageProj.getImage("project-photo.jpg")

# list of system options
system = [
    "Q: Quit", "O: Open Image", "S : Save Current Image",
    "R: Reload Original Image"
]

# list of basic operation options
basic = [
    "I: Switch to Intermediate Functions", "A: Switch to Advanced Functions"
]

# list of intermediate operation options
intermediate = [
    "B: Switch to Basic Functions", "A: Switch to Advanced Functions"
]

# list of advanced operation options
advanced = [
    "B: Switch to Basic Functions", "I: Switch to Intermediate Functions"
]


# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    # append necessary lines including system dictionary
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("")  # an empty line
    menuString.append("Choose the following options:")
    menuString.append("")  # an empty line
    menuString += system
    menuString.append("")  # an empty line

    # build the list differently depending on the mode attribute & add basic dictionary
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString.append("1: Invert")
        menuString.append("2: Flip Horizontal")
        menuString.append("3: Flip Vertical")
        menuString += basic
        menuString.append("Enter your choice (Q/O/S/R or 1-3 or I/A)")
    
    # build the list differently depending on the mode attribute & add intermediate dictionary
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString.append("1: Remove Red Channel")
        menuString.append("2: Remove Green Channel")
        menuString.append("3: Remove Blue Channel")
        menuString.append("4: Convert to Grayscale")
        menuString.append("5: Apply Sepia Filter")
        menuString.append("6: Decrease Brightness")
        menuString.append("7: Increase Brigthness")
        menuString += intermediate
        menuString.append("Enter your choice (Q/O/S/R or 1-7 or B/A)")
    
    # build the list differently depending on the mode attribute & add advanced dictionary
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString.append("1: Rotate Image Counter-Clockwise")
        menuString.append("2: Rotate Image Clockwise")
        menuString.append("3: Pixelate")
        menuString.append("4: Binarize")
        menuString += advanced
        menuString.append("Enter your choice (Q/O/S/R or 1-4 or B/I)")
    
    # print out error if anything else is given as input
    else:
        menuString.append("Error: Unknown mode!")

    # return menuString
    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    '''
    Input:  state - a dictionary containing the state values of the application
    #img - the 2d array of RGB values to be operated on
    #Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    '''
    userInput = state["lastUserInput"].upper()

    # handle the system functionalities
    if userInput.isalpha():  # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        
        if userInput == "Q":  # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        
        # if user types O, open a file
        elif userInput == "O":
          tkinter.Tk().withdraw()
          openFilename = tkinter.filedialog.askopenfilename()

          appStateValues["lastOpenFilename"] = openFilename

          img = cmpt120imageProj.getImage(openFilename) 

          cmpt120imageProj.showInterface(img, "Opened Image", generateMenu(appStateValues))
            
        # if user types S, save the file
        elif userInput == "S":
          tkinter.Tk().withdraw()
          saveFilename = tkinter.filedialog.asksaveasfilename()

          appStateValues["lastSaveFilename"] = cmpt120imageProj.saveImage(img , saveFilename)

          cmpt120imageProj.showInterface(img, "Saved Image", generateMenu(appStateValues))
          
        # if user types R, reload the original file
        elif userInput == "R":
          img = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])   

          cmpt120imageProj.showInterface(img, "Reload Image", generateMenu(appStateValues))
          
        # if user types B, change state["mode"] to basic & show interface appropriately
        elif userInput == "B":
          state["mode"] = "basic"
          cmpt120imageProj.showInterface(img, "Basic", generateMenu(appStateValues))

        # if user types I, change state["mode"] to intermediate & show interface appropriately
        elif userInput == "I":
          state["mode"] = "intermediate"
          cmpt120imageProj.showInterface(img, "Intermediate", generateMenu(appStateValues))

        # if user types A, change state["mode"] to advanced & show interface appropriately
        elif userInput == "A":
          state["mode"] = "advanced"
          cmpt120imageProj.showInterface(img, "Advanced", generateMenu(appStateValues))

        else: # unrecognized user input
          print("Log: Unrecognized user input: " + userInput)

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit():  # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)

        # if state["mode"] is basic, perform appropriate manipulations
        if state['mode'] == "basic":
            
            # if user input is 1, perform invert manipulation & show interface
            if userInput == "1":
              img = cmpt120imageManip.invert(img)
              cmpt120imageProj.showInterface(img, "Inverted",generateMenu(appStateValues))
            
            # if user input is 2, perform flipHorizontal manipulation & show interface
            elif userInput == "2":
              img = cmpt120imageManip.flipHorizontal(img)
              cmpt120imageProj.showInterface(img, "Flipped Horizontal", generateMenu(appStateValues))

            # if user input is 3, perform flipVertical manipulation & show interface
            elif userInput == "3":
              img = cmpt120imageManip.flipVertical(img)
              cmpt120imageProj.showInterface(img, "Flipped Vertical",generateMenu(appStateValues))
            
            else: # unrecognized user input
        # check if state["mode"] is intermediate, then perform appropriate manipulations
        
              print("Log: Unrecognized user input: " + userInput)
        
        if state["mode"] == "intermediate":    
            # if user input is 1, perform noRed manipulation & show interface
            if userInput == "1":
              img = cmpt120imageManip.noRed(img)
              cmpt120imageProj.showInterface(img, "No Red", generateMenu(appStateValues))

            # if user input is 2, perform noGreen manipulation & show interface
            elif userInput == "2":
              img = cmpt120imageManip.noGreen(img)
              cmpt120imageProj.showInterface(img, "No Green",generateMenu(appStateValues))

            # if user input is 3, perform noBlue manipulation & show interface 
            elif userInput == "3":
              img = cmpt120imageManip.noBlue(img)
              cmpt120imageProj.showInterface(img, "No Blue",generateMenu(appStateValues))

            # if user input is 4, perform grayScale manipulation & show interface
            elif userInput == "4":
              img = cmpt120imageManip.grayScale(img)
              cmpt120imageProj.showInterface(img, "grayScale",generateMenu(appStateValues))

            # if user input is 5, perform sepia manipulation & show interface
            elif userInput == "5":
              img = cmpt120imageManip.sepia(img)
              cmpt120imageProj.showInterface(img, "Sepia",generateMenu(appStateValues))

            # if user input is 6, perform decrease Brightness manipulation & show interface
            elif userInput == "6":
              img = cmpt120imageManip.decreaseB(img)
              cmpt120imageProj.showInterface(img, "Decreased Brightness",generateMenu(appStateValues))
            
            # if user input is 7, perform increase Brightness manipulation & show interface
            elif userInput == "7":
              img = cmpt120imageManip.increaseB(img)
              cmpt120imageProj.showInterface(img, "Increased Brightness",generateMenu(appStateValues))

            else: # unrecognized user input
              print("Log: Unrecognized user input: " + userInput)
        
        # check if state["mode"] is advanced, then perform appropriate manipulations
        if state["mode"] == "advanced":
            
            # if user input is 1, perform rotateLeft manipulation & show interface
            if userInput == "1":
              img = cmpt120imageManip.rotateLeft(img)
              cmpt120imageProj.showInterface(img, "Rotate Left",generateMenu(appStateValues))
            
            # if user input is 2, perform rotateRight manipulation & show interface
            elif userInput == "2":
              img = cmpt120imageManip.rotateRight(img)
              cmpt120imageProj.showInterface(img, "Rotate Right",generateMenu(appStateValues))
            
            # if user input is 3, perform pixelate manipulation & show interface
            elif userInput == "3":
              img = cmpt120imageManip.pixelate(img)
              cmpt120imageProj.showInterface(img, "Pixelate", generateMenu(appStateValues))
             
            # if user input is 4, perform binarize manipulation & show interface
            elif userInput == "4":
              img = cmpt120imageManip.binarize(img)
              cmpt120imageProj.showInterface(img, "Binarize", generateMenu(appStateValues))
            
            else: # unrecognized user input
              print("Log: Unrecognized user input: " + userInput)
          
    else: # unrecognized user input
              print("Log: Unrecognized user input: " + userInput)        
    # return image
    return img

# use a dictionary to remember several state values of the application
appStateValues = {
    "mode": "basic",
    "lastOpenFilename": "",
    "lastSaveFilename": "",
    "lastUserInput": ""
}

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used


# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
            # otherwise let the helper function handle the input
        elif event.type == pygame.QUIT:  #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

# print statement
print("Log: Program Quit")
