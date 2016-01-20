import wpf
import math

from System.Windows import Application, Window
from System.Windows.Shapes import Polyline
from System.Windows.Media import Brushes
from System.Windows import Point

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf8While.xaml')
    
    def polylineShape(self, sides):
        self.myCanvas.Children.Clear()          #clear the canvas of any children with the clear() method.
        h = self.myCanvas.Width/2
        k = self.myCanvas.Height/2              #Calculate the center of the canvas
        r = 100                                 #r is the radius of 100
        step = 2 * math.pi/sides                #for each step calculate the location of each point around the circumference
        theta = 0                               #theta starts at 0' anticlockwise to 360'
        polyline = Polyline()
        polyline.StrokeThickness = 1
        polyline.Stroke = Brushes.Blue

        while theta <= 360:                     #While loop, terminates after plotting all the points around one rotation
            _x  =  h + r * math.cos(theta)
            _y  =  k + r * math.sin(theta)
            polyline.Points.Add(Point(_x,_y))   #add the new x and y point to the line drawing
            theta = theta + step                #increment theta for loop condition

        self.myCanvas.Children.Add(polyline)    #finaly add the line we've generated to the canvas
    
    def button_Click(self, sender, e):          #Triangle button event trigger
        self.polylineShape(3)                   #plot 3 points around the circumference
    
    def button1_Click(self, sender, e):         #Square button
        self.polylineShape(4)                   #plot 4 points around the circumference
    
    def button2_Click(self, sender, e):         #Octagon button
        self.polylineShape(8)                   #plot 8 points around the circumference
    
    def button3_Click(self, sender, e):         #Circle button
        self.polylineShape(360)                 #plot 360 points around the circumference


if __name__ == '__main__':
    Application().Run(MyWindow())
