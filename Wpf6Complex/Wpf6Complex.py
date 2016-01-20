""" simple program accepts a value and adds VAT based on country
http://www.retailresearch.org/eurovat.php """

import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Wpf6Complex.xaml')
        europe = ["France", "Germany", "UK"]                            # a list of strings
        area = ["Mainland", "Guernsey", "Jersey"]
        self.label.Content = "Enter total before Tax"
        self.label1.Content = "Select destination country "
        self.textBox.Text = "0"                                         # anything other than a number will crash the program
        self.listBox.ItemsSource = europe                               # populate the listBox - ItemsSource = europe (the list variable created above) 
        self.label2.Content = "Total cost including Tax = "    
        self.listBox1.ItemsSource = area                                # populate the listBox - ItemsSource = area (list created above) 

    
    def button_Click(self, sender, e):
        subTotal = float(self.textBox.Text)                             # cast the value of the text box to a local variable with float data type

        if self.listBox.SelectedItem == "UK":                           # selection using listBox.SelectedItem (europe)
            if self.listBox1.SelectedItem == "Mainland":                # nested if using listBox1 (area)
               total = subTotal * 1.2
            elif self.listBox1.SelectedItem == "Guernsey":
                total = subTotal
            elif self.listBox1.SelectedItem == "Jersey":
                total = subTotal * 1.05
        elif self.listBox.SelectedItem == "France":                     # drop out of nested if with indentation to selection on listBox (europe)
            total = subTotal * 1.2
        elif self.listBox.SelectedItem == "Germany":
            total = subTotal * 1.19
        else:
            total = subTotal

        self.label2.Content = ("Total cost including Tax = %.2f" % total)     # print the output of the above calculation
    
    def listBox_SelectionChanged(self, sender, e):                      #listbox selection changed event trigger                           
        if self.listBox.SelectedItem == "UK":                           #selection if selected item is UK
            self.listBox1.Visibility = self.listBox1.Visibility.Visible #set the visibility property of the listBox1 object to visible
        else:
            self.listBox1.Visibility = self.listBox1.Visibility.Collapsed   #set the listBox1 object visibility property to collapsed



    

if __name__ == '__main__':
    Application().Run(MyWindow())
