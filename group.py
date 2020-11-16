from tkinter import *
from tkinter import messagebox


class Sick:
    def __init__(self, master):
        self.master = master
        master.title("Sick: Siphenkosi Salman")
        master.geometry("500x500")

        self.label1 = Label(master, text="SicknessCode")
        self.label1.grid(row=0, column=0, pady=5)

        self.code_entry = Entry(master)
        self.code_entry.grid(row=0, column=3, pady=5)

        self.label2 = Label(master, text="DurationOfTreatment")
        self.label2.grid(row=1, column=0, pady=5)

        self.duration_entry = Entry(master)
        self.duration_entry.grid(row=1, column=3, pady=5)

        self.label3 = Label(master, text="DoctorsPracticeNumber")
        self.label3.grid(row=2, column=0, pady=5)

        self.practice_number = Entry(master)
        self.practice_number.grid(row=2, column=3, pady=5)

        self.label4 = Label(master, text="Scan/Consultation Fee")
        self.label4.grid(row=3, column=0, pady=5)

        self.scan_fee = Entry(master)
        self.scan_fee.grid(row=3, column=3, pady=5)

        self.radio = IntVar()
        self.radio_button1 = Radiobutton(master, text='Cancer    ', variable=self.radio, value=1)
        self.radio_button1.grid(row=4, column=0, pady=5)

        self.radio_button2 = Radiobutton(master, text='Influenza', variable=self.radio, value=2)
        self.radio_button2.grid(row=5, column=0, pady=5)

        self.label5 = Label(master, text="Amount Paid For Treatment")
        self.label5.grid(row=6, column=0, pady=5)

        x = StringVar()
        self.output = Label(master, bg="pink", textvariable=x)
        self.output.grid(row=6, column=3, pady=5)

        self.calculate_btn = Button(master, text="Calculate", command=self.calculate)
        self.calculate_btn.grid(row=7, column=0, pady=5)

        self.clear_btn = Button(master, text="Clear", command=self.clear)
        self.clear_btn.grid(row=7, column=2, pady=5)

    def calculate(self):
        # This function is to redirect the calculation based on the radio button selected
        radio = self.radio.get()
        if radio == 1:
            can = Cancer(self.scan_fee.get())

        elif radio == 2:
            flu = Influenza(self.scan_fee.get())

    def clear(self):
        self.code_entry.delete(0, END)
        self.duration_entry.delete(0, END)
        self.practice_number.delete(0, END)
        self.scan_fee.delete(0, END)
        self.output.configure(text="")


class Cancer(Sick):

    def __init__(self, scan):
        self.output = Label(bg="pink")
        self.output.grid(row=6, column=3, pady=5)
        medication = 400
        self.scan = scan

        if float(scan) > 600:
            messagebox.showinfo("", "Sorry we cannot treat you")
        else:
            amount_paid = float(scan) + medication
            self.output.config(text="R"+str(round(amount_paid, 4)))


class Influenza(Sick):

    def __init__(self, consult):
        # x = StringVar()
        # amount_paid_display = Label(root, textvariable=x)
        # amount_paid_display.place(x=225, y=400)
        x = StringVar()
        self.output = Label(bg="pink", textvariable=x)
        self.output.grid(row=6, column=3, pady=5)
        medication = 350.50
        self.consult = consult
        consult = float(consult)

        if consult > 600:
            consult = 0.98*consult
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")
            # self.output.config(text="R" + str(round(amount_paid, 4)))
        else:
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")
            # self.output.config(text="R" + str(round(amount_paid, 4)))


root = Tk()
my_gui = Sick(root)
root.mainloop()
