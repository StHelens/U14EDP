""" simple program accepts a value and adds VAT based on country
http://www.retailresearch.org/eurovat.php """

import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf6Complex.xaml')
        europe = ["France", "Germany", "UK"]    # a list of strings
        area = ["Mainland", "Guernsey", "Jersey"]
        self.label.Content = "Enter total before Tax"
        self.label1.Content = "Select destination country "
        self.textBox.Text = "0"                                         # anything other than a number will crash the program
        self.listBox.ItemsSource = europe                               # listBox item source populated with a list 
        self.label2.Content = "Total cost including Tax = "    
        self.listBox1.ItemsSource = area

    
    def button_Click(self, sender, e):
        subTotal = float(self.textBox.Text)                             # cast the value of the text box to a local variable with float data type

        if self.listBox.SelectedItem == "UK":                           # selection using listBox.SelectedItem
            if self.listBox1.SelectedItem == "Mainland":                # nested if using listBox1
               total = subTotal * 1.2
            elif self.listBox1.SelectedItem == "Guernsey":
                total = subTotal
            elif self.listBox1.SelectedItem == "Jersey":
                total = subTotal * 1.05
        elif self.listBox.SelectedItem == "France":                     # drop out of nested if with indentation
            total = subTotal * 1.2
        elif self.listBox.SelectedItem == "Germany":
            total = subTotal * 1.19
        else:
            total = subTotal

        self.label2.Content = ("Total cost including Tax = %.2f" % total)     # print the output of the above calculation
    
    def listBox_SelectionChanged(self, sender, e):
        if self.listBox.SelectedItem == "UK":
            self.listBox1.Visibility = self.listBox1.Visibility.Visible
        else:
            self.listBox1.Visibility = self.listBox1.Visibility.Collapsed



    

if __name__ == '__main__':
    Application().Run(MyWindow())
