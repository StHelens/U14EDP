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
        self.myCanvas.Children.Clear
        h = self.myCanvas.Width/2
        k = self.myCanvas.Height/2
        r = 100
        step = 2*math.pi/sides
        theta = 0
        polyline = Polyline()
        polyline.StrokeThickness = 5
        polyline.Stroke = Brushes.Blue

        while theta <= 360:
            _x  =  h + r * math.cos(theta)
            _y  =  k + r * math.sin(theta)
            theta = theta + step
            polyline.Points.Add(Point(_x,_y))

        self.myCanvas.Children.Add(polyline)
    
    def button_Click(self, sender, e):
        self.polylineShape(3)
    
    def button1_Click(self, sender, e):
        self.polylineShape(4)
    
    def button2_Click(self, sender, e):
        self.polylineShape(8)
    
    def button3_Click(self, sender, e):
        self.polylineShape(360)


if __name__ == '__main__':
    Application().Run(MyWindow())
