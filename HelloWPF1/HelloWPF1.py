import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'HelloWPF1.xaml')
    
    def button_Click(self, sender, e):
        self.label.Content = "Hello WPF"
    

if __name__ == '__main__':
    Application().Run(MyWindow())
