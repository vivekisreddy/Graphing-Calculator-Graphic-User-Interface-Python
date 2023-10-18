import tkinter as tk
import functionClass as graphCalc

#making a class that creates a function box
class functionEntryBox:

    
    #when a function entry box is made create the things
    #parameters:
    # wn = tk window where the boxes should be
    # place X, the coordinate it should be placed on
    # place Y, the y coordinate it should be placed on
    # function Num, the number associated with the function (Ex: function 1, 2 or 3)
    #target plane, the coordinate plane the function will be drawn on
    #function color, the color the function will be in the menu and when graphed
    def __init__(self, wn, placeX,placeY, functionNum, targetPlane, functionColor):
        #set function num property as the given one
        self.functionNum=functionNum
        
        #create a frame where the function box elements will be contained
        self.fncFrame = tk.Frame(wn, pady=5,  bg="black")
        self.fncFrame.pack()
        self.fncFrame.place(x = placeX, y = placeY)
        #create a label that will say Function 1: or Function 2:
        self.fncLabel = tk.Label(self.fncFrame, text="Function" + str(functionNum) + ": ",
   compound="center",
   font=("comic sans", 12),
   bd=0,
   relief=tk.FLAT,
   fg=functionColor,
   bg="black")

        self.fncLabel.pack(side=tk.LEFT)
        
        #Create an entry box so the user can type in their function
        self.fncEntry= tk.Entry(self.fncFrame, font=("comic sans", 10), width = 18) 
        self.fncEntry.pack(side=tk.LEFT, padx=(0, 5))

        #create a button so the user can click on it to submit their equation
        #When clicked it will update the equation
        self.EnterBtn = tk.Button(wn, text="Enter", bd = '2', command= self.updateEq )
        self.EnterBtn.pack()
        self.EnterBtn.place(x = placeX+245, y = placeY+5)
 
        #Create an equation object for this function box to submit to.
        #It defaults to x**2 but the user will never notice this
        self.targetEq=graphCalc.equation("x**2", targetPlane, functionColor)

    #Method to update the equation on the graph
    def updateEq(self):
        #it gets what the user typed in the box
        newEq = self.fncEntry.get()
        #sets the target equation to the one typed in
        self.targetEq.setEq(newEq)
        #calculates the new coordinates and plots them
        self.targetEq.calculateCoords()
        self.targetEq.plotCoords()
    
######################
# MENU CLASSES
#####################

#Derivative menu

class derivativeMenu:

    #When a derivative menu is created this function will run to initialize it
    #Parameters:
    #self, the current instance of the derivative menu, can be ignored when constructing
    # wn, the tkinter window the derivative menu should be in
    #placeX, the x coordinate it should be placed on
    #placeY, the y coordinate it should be placed on
    #outputLabel, the label where it will print the calculated derivative
    #fncList, a list of all functionboxes so when the user types in function 1 2 or 3, the menu knows what that means
    def __init__(self,wn, title, placeX,placeY, outputLabel , fncList):
        self.title=title
        
        #create a frame the menu will be located in
        self.menuFrame = tk.Frame(wn, pady=5,  bg="cyan")
        self.menuFrame.pack(side=tk.TOP)
        self.menuFrame.place(x = placeX, y = placeY)
        
        #Create a label that says this is the derivative menu
        self.menuLabel = tk.Label(self.menuFrame, text=title,font=("comic sans", 10), bd=0, bg="white")
        self.menuLabel.grid(row=0,column=1)
        
        ###############################
        # CHOOSING WHICH FUNCTION TO TAKE THE DERIVATIVE OF
        #############################

        #Label saying, this is the textbox to type in to choose the textbox
        self.fncChooserLabel = tk.Label(self.menuFrame, text="Function",font=("comic sans", 10), bd=0, bg="white")
        self.fncChooserLabel.grid(row=1,column=0)

        #Box to actually type in to choose the function

        self.fncChooserEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 1) 
        self.fncChooserEntry.grid(row=2,column=0)
        

        ######################################
        # CHOOSING XVal to take derivative at
        ######################################

        #label saying, this is the place to type in the x value
        self.fncxValLabel = tk.Label(self.menuFrame, text="X-Value:",font=("comic sans", 10), bd=0, bg="white")
        self.fncxValLabel.grid(row=1,column=2)

        #box to type in to choose xValue
        self.fncxValEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 1) 
        self.fncxValEntry.grid(row=2,column=2)

       #button to submit and say "take the derivative"
        self.SubmitBtn = tk.Button(self.menuFrame, text="Submit", bd = '2', command=self.whenButtonClicked )
        self.SubmitBtn.grid(row=2,column=1)

        #save label to output to
        self.outPutLabel=outputLabel
        #save list of function boxes
        self.fncList=fncList

    ##################################
    #What Happens when Button Clicked#
    ##################################

    def whenButtonClicked(self):
        #the chosen function number, take it from the entry box
        chosenNum = self.fncChooserEntry.get()
        chosenNum=int(chosenNum)
        #the equation we're taking the derivative of, doing -1 because first in list is [0] but we want 1 to be first function to type in
        currentEquation = self.fncList[chosenNum-1]
        #get chosen x coordinate
        xCor= float(self.fncxValEntry.get())
        #get the derivative called
        derivativeValue= currentEquation.targetEq.calculateDerivative(xCor)
        #print for debugging purposes
        print(derivativeValue)
        #round it to 4 decimal places
        derivativeValue=round(derivativeValue,4)
        #create a string to output on the label
        outputString = "The derivative of function " + str(chosenNum)+"\n when x=" + self.fncxValEntry.get()+"\n is "+ str(derivativeValue)
        #change the text of the label to that string
        self.outPutLabel.config(text=outputString)


###############
#INTEGRAL MENU
###############

class integralMenu:

    #when the integral menu is created 
    def __init__(self,wn, title, placeX,placeY, outputLabel , fncList):
        
        #save the parameters as properties of the object
        self.title=title
        
        #create a fram for the menu to sit in
        self.menuFrame = tk.Frame(wn, pady=5,  bg="cyan")
        self.menuFrame.pack(side=tk.TOP)
        self.menuFrame.place(x = placeX, y = placeY)
        
        #Create label on the menu saying it's the integral menu
        self.menuLabel = tk.Label(self.menuFrame, text=title,font=("comic sans", 10), bd=0, bg="white")
        self.menuLabel.grid(row=0,column=1)

        #########################
        # BOX TO CHOOSE FUNCTION
        #########################

        #Label to say this box is the one to choose functions
        self.fncChooserLabel = tk.Label(self.menuFrame, text="Function",font=("comic sans", 10), bd=0, bg="white")
        self.fncChooserLabel.grid(row=1,column=0)

        
        #create box to type in to choose function
        self.fncChooserEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 1) 
        self.fncChooserEntry.grid(row=2,column=0)
        
        #############################
        # BOX TO CHOOSE LOWER X-BOUND
        ##############################

        #label the lower x box
        self.fnclowerxValLabel = tk.Label(self.menuFrame, text="Lower X-Value:",font=("comic sans", 10), bd=0, bg="white")
        self.fnclowerxValLabel.grid(row=1,column=2)

        # create box to type in the lower x value
        self.fnclowerxValEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 1) 
        self.fnclowerxValEntry.grid(row=2,column=2)

        ########################
        #CHOOSE HIGHER X-BOUND 
        ########################

        #label upper x box
        self.fncupperxValLabel = tk.Label(self.menuFrame, text="Upper X-Value:",font=("comic sans", 10), bd=0, bg="white")
        self.fncupperxValLabel.grid(row=1,column=3)

        #create box to type in upper x box
        self.fncupperxValEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 1) 
        self.fncupperxValEntry.grid(row=2,column=3)

        ######################
        # BUTTON TO SUBMIT
        #####################
        self.SubmitBtn = tk.Button(self.menuFrame, text="Submit", bd = '2', command=self.whenButtonClicked )
        self.SubmitBtn.grid(row=2,column=1)

        #save label to output to
        self.outPutLabel=outputLabel

        #save list of functions that can be accessed
        self.fncList=fncList

    #FUNCTION to respond to button press
    def whenButtonClicked(self):

        #get the function the user chose
        chosenNum = self.fncChooserEntry.get()
        chosenNum=int(chosenNum)
        currentEquation = self.fncList[chosenNum-1]

        #get the lower x bound from the box
        lowerxCor= float(self.fnclowerxValEntry.get())
        #get the higher x bound from the box
        upperxCor= float(self.fncupperxValEntry.get())
        
        #get the value of the integral using the calculateIntegral method
        integralValue= currentEquation.targetEq.calculateIntegral(lowerxCor,upperxCor)

        #print it into the terminal for debugging purposes
        print(integralValue)
        #round it to 4 decimal places
        integralValue=round(integralValue,4)
        #set the label to the desired message
        outputString = "The integral of function " + str(chosenNum)+"\n from x=" + str(lowerxCor)+" to x="+ str(upperxCor)+"\n is "+ str(integralValue)
        
        self.outPutLabel.config(text=outputString)
################
# ROTATION MENU
################

class rotationMenu:
    def __init__(self,wn, title, placeX,placeY, outputLabel , fncList):
        self.title=title
        #create and setup a frame for the menu to sit in
        self.menuFrame = tk.Frame(wn, pady=5,  bg="cyan")
        self.menuFrame.pack(side=tk.TOP)
        self.menuFrame.place(x = placeX, y = placeY)
        
        #create a label to say that this is the rotation menu
        self.menuLabel = tk.Label(self.menuFrame, text=title,font=("comic sans", 10), bd=0, bg="white")
        self.menuLabel.grid(row=0,column=1)

        #FUNCTION CHOOSER BOX
        
        #label it
        self.fncChooserLabel = tk.Label(self.menuFrame, text="Function",font=("comic sans", 10), bd=0, bg="white")
        self.fncChooserLabel.grid(row=1,column=0)

        #create box to type into
        self.fncChooserEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 1) 
        self.fncChooserEntry.grid(row=2,column=0)
       


        #CHOOSE ANGLE TO ROTATE BY
        
        #label the box as the place to enter an angle
        self.fncangleLabel = tk.Label(self.menuFrame, text="Angle:",font=("comic sans", 10), bd=0, bg="white")
        self.fncangleLabel.grid(row=1,column=2)

        #create box to type angle into
        self.fncangleEntry= tk.Entry(self.menuFrame, font=("comic sans", 15), width = 3) 
        self.fncangleEntry.grid(row=2,column=2)

        #Button to submit angle rotation
        self.SubmitBtn = tk.Button(self.menuFrame, text="Submit", bd = '2', command=self.whenButtonClicked )
        self.SubmitBtn.grid(row=2,column=1)

        #save label to output to
        self.outPutLabel=outputLabel
        #list of functions so the fncChooser can get the right function
        self.fncList=fncList


    #WHEN BUTTON CLICKED

    def whenButtonClicked(self):
        #get the function the user chose
        chosenNum = self.fncChooserEntry.get()
        chosenNum=int(chosenNum)
        currentEquation = self.fncList[chosenNum-1]

        #get the angle the user chose
        chosenAngle= float(self.fncangleEntry.get())
        #calculate the newly rotated points
        currentEquation.targetEq.calculateRotatedPoints(chosenAngle)
        #plot the new points
        currentEquation.targetEq.plotCoords()
        #output to the label that the function has been rotated
        outputString = "The function has been rotated"
        self.outPutLabel.config(text=outputString)
