import wpf
import math

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf3Numbers.xaml')

    
    def calculatePayment(self):
        L = self.textBox.Text           #local variable stored value entered into textBox
        i = self.textBox1.Text
        n = self.textBox2.Text
        L = int(L)                      #cast string value stored in local variable to int
        i = float(i)/12                 #cast string to float and divide by 12
        n = int(n)

        M=L*(i*(1+i)**n)/((1+i)**n-1)
        return M

    def button_Click(self, sender, e):      #button click event trigger
        result = self.calculatePayment()    #call calculatePayment function store return value in result
        self.resultLabel.Content = ("Monthly payments = " + str(result)) 
    

if __name__ == '__main__':
    Application().Run(MyWindow())
