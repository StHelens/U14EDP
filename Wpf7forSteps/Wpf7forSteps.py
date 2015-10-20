import wpf
import math

from System.Windows import Application, Window
from System.Windows.Shapes import Polyline
from System.Windows.Media import Brushes
from System.Windows import Point


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf7forSteps.xaml')
        self.polylineShape(20)
    
    def polylineShape(self, sides):
        
        h = self.myCanvas.Width/2
        k = self.myCanvas.Height/2
        r = 100
        step = 360
        theta = 0
        polyline = Polyline()
        polyline.StrokeThickness = 5
        polyline.Stroke = Brushes.Blue

        for steps in range(sides):
            _x  =  h + sides
            _y  =  k + sides
            polyline.Points.Add(Point(_x,_y))

        self.myCanvas.Children.Add(polyline)

if __name__ == '__main__':
    Application().Run(MyWindow())
