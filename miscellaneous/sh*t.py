import tkinter

class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)

        self.principal = tkinter.DoubleVar()
        self.principal.set(1000.0)

        self.rate = tkinter.DoubleVar()
        self.rate.set(5.0)
        self.years = tkinter.IntVar()
        self.amount = tkinter.StringVar()

        principalLabel = tkinter.Label(self, text = "Principal $: ", anchor = tkinter.W, underline = 0)
        principalScale = tkinter.Scale(self, variable = self.principal, command = self.updateUI, from_ = 100, to = 1000000, resolution = 100, orient = tkinter.HORIZONTAL)
        rateLabel  = tkinter.Label(self, text = "Rate %: ", underline = 0, anchor = tkinter.W)
        rateScale = tkinter.Scale(self, variable = self.rate, command = self.updateUI, from_ = 1, to = 100, resolution = 0.25, digits = 5, orient = tkinter.HORIZONTAL)
        yearsLabel = tkinter.Label(self, text = "Years: ", underline = 0, anchor = tkinter.W)
        yearsScale = tkinter.Scale(self, variable = self.years, command = updateUI, from_ = 1, to = 50, orient = tkinter.HORIZONTAL)
        amountLabel = tkinter.Label(self, text = "Amount $", anchor = tkinter.W)
        actualAmountLabel = tkinter.Label(self, textvariable = self.amount, relief = tkinter.SUNKEN, anchor = tkinter.E)

        principalLabel.grid(row=0, column=0, padx=2, pady=2,
                            sticky=tkinter.W)
        principalScale.grid(row=0, column=1, padx=2, pady=2,
                        sticky=tkinter.EW)
        rateLabel.grid(row=1, column=0, padx=2, pady=2,
                    sticky=tkinter.W)
        rateScale.grid(row=1, column=1, padx=2, pady=2,
                     sticky=tkinter.EW)
        yearsLabel.grid(row=2, column=0, padx=2, pady=2,
                    sticky=tkinter.W)
        yearsScale.grid(row=2, column=1, padx=2, pady=2,
                    sticky=tkinter.EW)
        amountLabel.grid(row=3, column=0, padx=2, pady=2,
                    sticky=tkinter.W)
