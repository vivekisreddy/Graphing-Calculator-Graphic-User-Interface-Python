
#import other files we programmed and the turtle and tkinter libraries
from turtle import bgcolor
import functionClass as graphCalc
import guiClass as guiElements
import tkinter as tk

##################
#CREATE TK WINDOW#
##################
#create main Tkinter window
mainWindow = tk.Tk()
#make it white and be 1000 wide by 800 tall
mainWindow.config(bg="white")
mainWindow.geometry("1000x800")


#############################
# CREATE COORDINATE PLANE ###
#############################

#Create a coordinate plane on the main tkinter window.
#At coordinates 0,0 on a canvas
mainPlane = graphCalc.coordinatePlane(mainWindow,0,0,500,500,3,1)


######################
# CREATE OUTPUT LABEL#
#####################

#create and place a label that will contain the outputs of some calculations
outPutLabel= tk.Label(mainWindow, text= "Output will appear here")
outPutLabel.pack()
outPutLabel.place(x=50,y=5)


###################
#CREATE FUNCTION BOXES
###################

#create a list that will contain the functionEntryBoxes, this will be recalled when an operation chooses "function1" or 2 or 3


#create a function box with a blue color at x=0,y=200
fncBox1= guiElements.functionEntryBox(mainWindow,0,200,1,mainPlane,"dodger blue")
#add it to the list of functionBoxes

#create a green second function Box just below it at x=0 y=300
fncBox2= guiElements.functionEntryBox(mainWindow,0,300,2,mainPlane,"green")
#add it to the list of function boxes

#create a third red function box just below the other two at x=0 y=400
fncBox3= guiElements.functionEntryBox(mainWindow,0,400,3,mainPlane,"red")
#add it to the list


functionBoxes=[fncBox1,fncBox2,fncBox3]


##############################
#CREATE MENUS FOR CALCULATIONS
##############################

#Create derivative menu at x=300, y =0
derivativeMenu= guiElements.derivativeMenu(mainWindow,"Derivative",300,0, outPutLabel, functionBoxes)

#create integral menu at x=500, y=0
integralMenu= guiElements.integralMenu(mainWindow,"Integral",500,0, outPutLabel, functionBoxes)

#create rotation menu at x= 800, y=0
rotationmenu= guiElements.rotationMenu(mainWindow,"Rotate",800,0, outPutLabel, functionBoxes)

#tell the plane to draw itself
mainPlane.createGraph()

#Run mainloop so the code actually starts
mainWindow.mainloop()



