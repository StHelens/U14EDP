import wpf
import math

from System.Windows import Application, Window
from System.Windows.Shapes import Polyline
from System.Windows.Media import Brushes
from System.Windows import Point
from System.Windows.Media import SolidColorBrush


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf7forSteps.xaml')
        self.polylineShape()
    
    def polylineShape(self):
        
        x = self.myCanvas.Width/2
        y = self.myCanvas.Height/2
        polyline = Polyline()
        polyline.StrokeThickness = 5


        for steps in ['Red','Blue','Green','Black']:
            x = x
            y = x            
            polyline.Points.Add(Point(x,y))
            x = x + 40
            polyline.Points.Add(Point(x,y))
            polyline.Stroke = Brushes.Red    #should change colour

        self.myCanvas.Children.Add(polyline)

if __name__ == '__main__':
    Application().Run(MyWindow())
