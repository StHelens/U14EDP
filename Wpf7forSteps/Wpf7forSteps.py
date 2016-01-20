import wpf

from System.Windows import Application, Window, Point
from System.Windows.Shapes import Polyline
from System.Windows.Media import Brushes


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf7forSteps.xaml')
        self.polylineShape()
    
    def polylineShape(self):
        x = 0                                                               #initialise local variables
        y = 0

        for steps in [Brushes.SteelBlue, Brushes.DarkOrange, Brushes.DarkSeaGreen, Brushes.Honeydew]:   #for loop completes one iteration for each brush colour
            polyline = Polyline()                                           #New Polyline for each iteration 
            polyline.StrokeThickness = self.myCanvas.Height/4               #Calculate the width of the line 
                
            x = 0                                                           
            y = y + self.myCanvas.Height/4                                  #Move the y coordinate down
            polyline.Points.Add(Point(x,y))                                 #Add x,y start point
            
            x = self.myCanvas.Width                                         #Move x coordinate to the end of canvas
            polyline.Points.Add(Point(x,y))                                 #Add x,y end point

            polyline.Stroke = steps                                         #Set the brush colour based on the steps value
                        
            self.myCanvas.Children.Add(polyline)                            #Draw the line on the canvas, adding the polyline as a child of the canvas


if __name__ == '__main__':
    Application().Run(MyWindow())
