import wpf
import math

from System.Windows import Application, Window
from System.Windows.Shapes import Polyline
from System.Windows.Media import Brushes
from System.Windows import Point

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf7While.xaml')
    
    def polylineShape(self, sides):
        self.myCanvas.Children.Clear()
        h = self.myCanvas.Width/2
        k = self.myCanvas.Height/2              #Calculate the center of the canvas
        r = 100                                 #r is the radius from the center of the canvas
        step = math.pi/sides                    #the location of each point around the circumference
        theta = 0                               #theta starts at 0' anticlockwise to 360'
        polyline = Polyline()
        polyline.StrokeThickness = 5
        polyline.Stroke = Brushes.Blue

        while theta <= 360:                     #While loop, terminates after one rotation
            _x  =  h + r * math.cos(theta)
            _y  =  k + r * math.sin(theta)
            polyline.Points.Add(Point(_x,_y))   #add the new x and y point to the line drawing
            theta = theta + step

        self.myCanvas.Children.Add(polyline)    #finaly add the line we've generated to the canvas
    
    def button_Click(self, sender, e):          #Triangle
        self.polylineShape(3)
    
    def button1_Click(self, sender, e):         #Square
        self.polylineShape(4)
    
    def button2_Click(self, sender, e):         #Octagon
        self.polylineShape(8)
    
    def button3_Click(self, sender, e):         #Circle
        self.polylineShape(360)


if __name__ == '__main__':
    Application().Run(MyWindow())
