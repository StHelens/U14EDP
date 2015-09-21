import wpf
import math

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf3Numbers.xaml')

    
    def calculatePayment(self):
        L = self.textBox.Text
        i = self.textBox1.Text
        n = self.textBox2.Text
        L = int(L)
        i = float(i)/12
        n = int(n)

        M=L*(i*(1+i)**n)/((1+i)**n-1)
        return M

    def button_Click(self, sender, e):
        result = self.calculatePayment()
        self.resultLabel.Content = ("Monthly payments = " + str(result)) 
    

if __name__ == '__main__':
    Application().Run(MyWindow())
