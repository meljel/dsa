#
#Melody Jing
#
#

from graphics import *

class Button:

    """Inputs window, center, dimensions, text, and color to create an interactive
       button which can be clicked, activated/deactivated, mutated, and accessed"""
    
    def __init__(self, window, center, height, width, text,
                 textColor, inacColor, bkColor):

        """draws button, sets colors as indicated"""

        x,y=center.getX(), center.getY()
        self.x0, self.x1, self.y0, self.y1=x-0.5*width,x+0.5*width,y-0.5*height,y+0.5*height
        a=Point(self.x0,self.y0)
        b=Point(self.x1,self.y1)

        self.textColor = textColor
        self.box = Rectangle(a,b)
        self.box.setFill(bkColor)
        self.box.draw(window)
        self.label = Text(center, text)
        self.label.setFill(textColor)
        self.label.draw(window)
        self.deactivate()

    def getLabel(self):

        """returns label of the button"""

        return self.label.getText()

    def changeLabel(self,newLabel):

        """sets button label according to input"""

        self.label.setText(str(newLabel))

    def setLabelColor(self, newColor):

        """sets button label color according to input"""
        
        self.textColor = newColor
        self.label.setFill(self.textColor)
        
    def getLabelColor(self):

        """returns button label color"""
        
        return self.textColor
    
    def clicked(self, p):

        """returns true if button is active and is clicked"""
        
        return (self.active and self.x0<=p.getX()<=self.x1
                and self.y0<=p.getY()<=self.y1)

    def undraw(self):

        """undraws button"""

        self.box.undraw()
        self.label.undraw()

    def activate(self):

        """makes button clickable"""

        self.label.setFill(self.textColor)
        self.box.setWidth(2)
        self.active = True

    def deactivate(self):

        """makes button unclickable"""

        self.label.setFill(self.textColor)
        self.box.setWidth(1)
        self.active = False

    
