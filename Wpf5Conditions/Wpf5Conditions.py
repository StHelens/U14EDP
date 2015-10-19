import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf5Conditions.xaml')
        self.battlefront = 43.99
        self.halo = 41.99
        self.fifa = 44.99
        self.subtotal = 0
        self.label.Content = "Add items to basket below "
        self.label1.Content = ("Battlefront = %s" % self.battlefront)
        self.label2.Content = ("Halo 5 = %s" % self.halo)
        self.label3.Content = ("FIFA 16 = %s" % self.fifa)
        self.label4.Content = "Total"
        self.button.Content = "Calculate"
    
    def button_Click(self, sender, e):
        if self.subtotal < 50 and self.subtotal > 0:
            self.label4.Content = ("Total = {0:.2f}".format(self.subtotal + 10) + " inc. shipping")
        elif self.subtotal >= 50:
            self.label4.Content = ("Total = {0:.2f}".format(self.subtotal) + " free shipping")
        else:
            self.label4.Content = ("Total = %.2f" %self.subtotal)

    
    def checkBox_Checked(self, sender, e):
        self.subtotal += self.battlefront    

    def checkBox_Unchecked(self, sender, e):
        self.subtotal -= self.battlefront

    def checkBox1_Checked(self, sender, e):
        self.subtotal += self.halo 

    def checkBox1_Unchecked(self, sender, e):
        self.subtotal -= self.halo
    
    def checkBox2_Checked(self, sender, e):
        self.subtotal += self.fifa

    def checkBox2_Unchecked(self, sender, e):
        self.subtotal -= self.fifa

if __name__ == '__main__':
    Application().Run(MyWindow())
