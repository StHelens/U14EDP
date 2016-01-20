import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WPF2Input.xaml')  #Initialise the WPF form .xaml component
        self.label.Content = "Enter your name"      #Initialise the content property of the label object
        self.textBox.Text = ""                      #Initialise the text properties textBox object 
    
    def inputName(self):                            #declare function inputName
        userName = self.textBox.Text                #local variable userName 
        return userName                             #returns text value entered into textbox

    def button_Click(self, sender, e):              #button click event trigger
        userName = self.inputName()                 #event handler calls inputName function
        self.label.Content = ("Welcome " + userName.capitalize() + " you're using a function")
    
if __name__ == '__main__':
    Application().Run(MyWindow())