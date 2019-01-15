# Demonstrates text and entry widgets, and the grid layout manager

from Tkinter import *
from fractions import Fraction

class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        self.inst_lbl = Label(self, text = "Enter all your data")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create label    
        self.pw_lbl = Label(self, text = "Probability: ")
        self.pw_lbl.grid(row = 3, column = 0, sticky = W)

        # create entry widget    
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 3, column = 1, columnspan = 2, sticky = W)
        
        # create label    
        self.ph_lb1 = Label(self, text = "Poisson %: ")
        self.ph_lb1.grid(row = 4, column = 0, sticky = W)

        # create entry widget      
        self.ph_ent = Entry(self)
        self.ph_ent.grid(row = 4, column = 1, sticky = W)
        
        

        # create label     
        self.oh_lb1 = Label(self, text = "Odds: ")
        self.oh_lb1.grid(row = 5, column = 0, sticky = W)

        # create entry widget    
        self.oh_ent = Entry(self)
        self.oh_ent.grid(row = 5, column = 1, sticky = W)

        # create instruction label
        Label(self,
              text = "Select one:"
              ).grid(row = 6, column = 0, sticky = W)

        # create variable
        self.b_ent = StringVar()
        self.b_ent.set(None)

        # create radio button
        Radiobutton(self,
                    text = "100",
                    variable = self.b_ent,
                    value = "100",
                    command = self.reveal
                    ).grid(row = 7, column = 0, sticky = W)

        # create radio button
        Radiobutton(self,
                    text = "105",
                    variable = self.b_ent,
                    value = "105",
                    command = self.reveal
                    ).grid(row = 8, column = 0, sticky = W)

        # create radio button
        Radiobutton(self,
                    text = "110",
                    variable = self.b_ent,
                    value = "110",
                    command = self.reveal
                    ).grid(row = 9, column = 0, sticky = W)
        # create radio button
        Radiobutton(self,
                    text = "115",
                    variable = self.b_ent,
                    value = "115",
                    command = self.reveal
                    ).grid(row = 10, column = 0, sticky = W)

        
        # create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 11, column = 0, sticky = W)

        # create text widget to display message
        self.secret_txt = Text(self, width = 45, height = 8, wrap = WORD)
        self.secret_txt.grid(row = 12, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """ Display message """
        prob = self.pw_ent.get()
        h_pois = self.ph_ent.get()
        d_pois = 01.00
        a_pois = 01.00
        h_odds = self.oh_ent.get()
        d_odds = 2.5
        a_odds = 2.5
        saldo = self.b_ent.get()
        h_victory = prob[0:5]
        h_victory = float(h_victory)
        draw = 01.00
        draw = float(draw)
        a_victory = 01.00
        a_victory = float(a_victory)
        saldo = float(saldo)
        h_odds = float(h_odds)
        a_odds = float(a_odds)
        d_odds = float(d_odds)
        h_pois = float(h_pois)
        d_pois = float(d_pois)
        a_pois = float(a_pois)
        altered_h = h_victory + h_pois
        altered_h = float(altered_h)
        altered_h = altered_h / 2
        altered_h1 = altered_h
        altered_h = "%.2f" % altered_h
        altered_h = str(altered_h)
        altered_a = a_victory + a_pois
        altered_a = float(altered_a)
        altered_a = altered_a / 2
        altered_a = "%.2f" % altered_a
        altered_a = str(altered_a)
        altered_d = draw + d_pois
        altered_d = float(altered_d)
        altered_d = altered_d / 2
        altered_d = "%.2f" % altered_d
        altered_d = str(altered_d)
        prob_h = 1 / h_odds
        prob_h = float(prob_h)
        prob_d = 1 / d_odds
        prob_d = float(prob_d)
        prob_a = 1 / a_odds
        prob_a = float(prob_a)
        prob_h = prob_h * 100
        prob_a = prob_a * 100
        prob_d = prob_d * 100
        prob_total = prob_d + prob_a + prob_h
        prob_total = float(prob_total)
        prob_total_2 = prob_total - 100
        prob_total_2 = float(prob_total_2)

        h_odds = h_odds - 1
        a_odds = a_odds - 1 
        d_odds = d_odds - 1
        dchance1x = h_victory + draw
        dchance12 = h_victory + a_victory
        dchancex2 = draw + a_victory
        h_victory = h_victory / 100
        altered_h1 = altered_h1 / 100
        draw = draw / 100
        a_victory = a_victory / 100

        h_calculation = h_odds * h_victory      # kelly dla zwyciestwa u siebie
        h_calculation = float(h_calculation)
        h_losing = 1 - h_victory
        h_losing = float(h_losing)
        h_calculation = h_calculation - h_losing
        h_calculation = h_calculation / h_odds
        h_calculation_sum = h_calculation * 100
        saldo_h = saldo * h_calculation
        saldo_h = float(saldo_h)
        
        h1_calculation = h_odds * altered_h1      # kelly dla zwyciestwa u siebie zmienione
        h1_calculation = float(h1_calculation)
        h1_losing = 1 - altered_h1
        h1_losing = float(h1_losing)
        h1_calculation = h1_calculation - h1_losing
        h1_calculation = h1_calculation / h_odds
        h1_calculation_sum = h1_calculation * 100
        saldo_h1 = saldo * h1_calculation
        saldo_h1 = float(saldo_h1)        
        

        d_calculation = d_odds * draw       # kelly remis
        d_calculation = float(d_calculation)
        d_losing = 1 - draw
        d_losing = float(d_losing)
        d_calculation = d_calculation - d_losing
        d_calculation = d_calculation / d_odds
        d_calculation_sum = d_calculation * 100
        saldo_d = saldo * d_calculation
        saldo_d = float(saldo_d)

        a_calculation = a_odds * a_victory      # kelly wyjazd
        a_calculation = float(a_calculation)
        a_losing = 1 - a_victory
        a_losing = float(a_losing)
        a_calculation = a_calculation - a_losing
        a_calculation = a_calculation / a_odds
        a_calculation_sum = a_calculation * 100
        saldo_a = saldo * a_calculation
        saldo_a = float(saldo_a)
        saldo_h = "%.2f" % saldo_h
        saldo_h1 = "%.2f" % saldo_h1
        saldo_d = "%.2f" % saldo_d
        saldo_a = "%.2f" % saldo_a
        prob_total_2 = "%.2f" % prob_total_2
        dchance1x = "%.2f" % dchance1x
        dchance12 = "%.2f" % dchance12
        dchancex2 = "%.2f" % dchancex2
        saldo_h = str(saldo_h)
        saldo_h1 = str(saldo_h1)
        saldo_d = str(saldo_d)
        saldo_a = str(saldo_a)
        prob_total_2 = str(prob_total_2)
        dchance1x = str(dchance1x)
        dchance12 = str(dchance12)
        dchancex2 = str(dchancex2)
       
        message = "You should bet "
        message += saldo_h
        message += ". \n"
        message += "Altered chance is "
        message += altered_h
        message += " %. \n"
        message += "After adjustment "
        message += saldo_h1
        message += ". \n"

        
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

# main
root = Tk()
root.title("Kcalculator")
root.geometry("375x395")

app = Application(root)

root.mainloop()
