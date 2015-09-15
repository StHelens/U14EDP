import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf1Buttons.xaml')
        self.message = "Group %s is the best"
    
    def Group2_Click(self, sender, e):
        self.label.Content = self.message % 2
    
    def Group3_Click(self, sender, e):
        self.label.Content = self.message % 3
    
    def Group4_Click(self, sender, e):
        self.label.Content = self.message % 4
    
    def Group5_Click(self, sender, e):
        self.label.Content = self.message % 5

if __name__ == '__main__':
    Application().Run(MyWindow())
