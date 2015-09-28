import wpf
import datetime

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf4Dates.xaml')
        self.label.Content = "Please enter the deadline date (d/m/yyyy)"
        self.textBox.Text = ""
        self.button.Content = "Calculate"
    
    def dateFunction(self):
        deadlineDate = datetime.datetime.strptime(self.textBox.Text,'%d/%m/%Y').date()
        currentDate = datetime.date.today()
        result = deadlineDate - currentDate
        result = str(result.days)
        return result
        
    def button_Click(self, sender, e):
        deadline = self.dateFunction()
        self.label.Content = (deadline + " days until the deadline")

if __name__ == '__main__':
    Application().Run(MyWindow())
