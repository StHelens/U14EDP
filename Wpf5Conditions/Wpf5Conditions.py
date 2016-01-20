import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf5Conditions.xaml')  #creates object defined in the XAML
        self.battlefront = 43.99    
        self.halo = 41.99
        self.fifa = 44.99
        self.subtotal = 0
        self.label.Content = "Add items to basket below "
        self.checkBox.Content = ("Battlefront = %s" % self.battlefront)
        self.checkBox1.Content = ("Halo 5 = %s" % self.halo)
        self.checkBox2.Content = ("FIFA 16 = %s" % self.fifa)
        self.label4.Content = "Total"
        self.button.Content = "Calculate"
    
    def button_Click(self, sender, e):                  #button clicked even trigger
        if self.subtotal < 50 and self.subtotal > 0:    #selection, test the subtotal is less than 50
            self.label4.Content = ("Total = {0:.2f}".format(self.subtotal + 10) + " inc. shipping")     #add £10 for shipping
        elif self.subtotal >= 50:                                                                       #selecion, if subtotal is greater than or equal to 50
            self.label4.Content = ("Total = {0:.2f}".format(self.subtotal) + " free shipping")          #calculate total with no shipping costs
        else:                                                                                           #if the value is 0 or negative 
            self.label4.Content = ("Total = %.2f" %self.subtotal)

    
    def checkBox_Checked(self, sender, e):                                                              #checkbox checked event trigger
        self.subtotal += self.battlefront                                                               #event handler, add integer to subtotal

    def checkBox_Unchecked(self, sender, e):                                                            #checkbox unchecked event trigger
        self.subtotal -= self.battlefront                                                               #event handler, subtract integer from subtotal

    def checkBox1_Checked(self, sender, e):
        self.subtotal += self.halo 

    def checkBox1_Unchecked(self, sender, e):
        self.subtotal -= self.halo
    
    def checkBox2_Checked(self, sender, e):
        self.subtotal += self.fifa

    def checkBox2_Unchecked(self, sender, e):
        self.subtotal -= self.fifa

if __name__ == '__main__':
    Application().Run(MyWindow())           #Begins running a standard application message loop on the current thread. https://goo.gl/JLKB1D
