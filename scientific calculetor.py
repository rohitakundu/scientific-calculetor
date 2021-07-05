from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("scientific Calculetor")
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc=Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=textDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
    
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(textDisplay.get())
    
    def display(self, value):
        textDisplay.delete(0, END)
        textDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(textDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(textDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(textDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(textDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(textDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(textDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(textDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(textDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(textDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(textDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(textDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(textDisplay.get()))
        self.display(self.current)

added_value = Calc()
        




# Code for Display of Calculator.

textDisplay = Entry(calc,font=('Helvetica',20,'bold'),bg="powder blue",fg="black",bd=30,width=29,justify=RIGHT)
textDisplay.grid(row=0,column=0,columnspan=4,pady=1)
textDisplay.insert(0,"0")






#Code for NUMBER PAD in Calculator.

numberpad = "789456123"
i=0
btn = []
for j in range (2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('Helvetica',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] =lambda x =numberpad[i]:added_value.numberEnter(x)

        i += 1






# Cod e for Button of Standard Calulator.

btnClear = Button(calc, text=chr(67), width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.Clear_Entry)
btnClear.grid(row=1,column=0,pady=1)

btnAllClear = Button(calc, text=chr(67)+chr(69), width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.All_Clear_Entry)
btnAllClear.grid(row=1,column=1,pady=1)

btnSq = Button(calc, text="\u221A", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.squared)
btnSq.grid(row=1,column=2,pady=1)

btnAdd = Button(calc, text="+", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.operation("add"))
btnAdd.grid(row=1,column=3,pady=1)

btnSub = Button(calc, text="-", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.operation("sub"))
btnSub.grid(row=2,column=3,pady=1)

btnMul = Button(calc, text="*", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.operation("multi"))
btnMul.grid(row=3,column=3,pady=1)

btnDiv = Button(calc, text=chr(247), width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.operation("divide"))
btnDiv.grid(row=4,column=3,pady=1)

btnZero = Button(calc, text="0", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="white",command=lambda:added_value.numberEnter(0))
btnZero.grid(row=5,column=0,pady=1)

btnDot = Button(calc, text=".", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.numberEnter("."))
btnDot.grid(row=5,column=1,pady=1)

btnPM = Button(calc, text=chr(177), width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.numberEnter("."))
btnPM.grid(row=5,column=2,pady=1)

btnEquals = Button(calc, text="=", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.sum_of_total)
btnEquals.grid(row=5,column=3,pady=1)







#=====================================================================================================================================
# Code for Buttons of Scientific Calulator.
# The rows for the Button of Scientific Calulator.
#row: 1

btnPi = Button(calc, text="n", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.pi)
btnPi.grid(row=1,column=4,pady=1)

btnCos = Button(calc, text="Cos", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.cos)
btnCos.grid(row=1,column=5,pady=1)

btntan = Button(calc, text="tan", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.tan)
btntan.grid(row=1,column=6,pady=1)

btnSin = Button(calc, text="Sin", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.sin)
btnSin.grid(row=1,column=7,pady=1)

#row: 2

btn2Pi = Button(calc, text="2pi", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.tau)
btn2Pi.grid(row=2,column=4,pady=1)

btnCosh = Button(calc, text="cosh", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.cosh)
btnCosh.grid(row=2,column=5,pady=1)

btntanh = Button(calc, text="tanh", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.tanh)
btntanh.grid(row=2,column=6,pady=1)

btnSinh = Button(calc, text="sinh", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.sinh)
btnSinh.grid(row=2,column=7,pady=1)

#row: 3

btnlog = Button(calc, text="log", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.log)
btnlog.grid(row=3,column=4,pady=1)

btnExp = Button(calc, text="Exp", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.exp)
btnExp.grid(row=3,column=5,pady=1)

btnMod = Button(calc, text="Mod", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=lambda:added_value.operation("mod"))
btnMod.grid(row=3,column=6,pady=1)

btnE = Button(calc, text="e", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.e)
btnE.grid(row=3,column=7,pady=1)

#row: 4

btnlog10 = Button(calc, text="log10", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.log10)
btnlog10.grid(row=4,column=4,pady=1)

btncos = Button(calc, text="deg", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.cos)
btncos.grid(row=4,column=5,pady=1)

btnexpm1 = Button(calc, text="expm1", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.expm1)
btnexpm1.grid(row=4,column=6,pady=1)

btngamma = Button(calc, text="gamma", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.lgamma)
btngamma.grid(row=4,column=7,pady=1)

#row: 5

btnlog2 = Button(calc, text="log2", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.log2)
btnlog2.grid(row=5,column=4,pady=1)

btndeg = Button(calc, text="deg", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.degrees)
btndeg.grid(row=5,column=5,pady=1)

btnacosh = Button(calc, text="acosh", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.acosh)
btnacosh.grid(row=5,column=6,pady=1)

btnasinh = Button(calc, text="asinh", width=6,height=2,font=('Helvetica',20,'bold'),bd=4, bg="powder blue",command=added_value.asinh)
btnasinh.grid(row=5,column=7,pady=1)

lbDisplay = Label(calc,text="Scientific Calculetor",font=('Helivetica',30,'bold'),bg='powder blue',fg='black',justify=CENTER)
lbDisplay.grid(row=0,column=4,columnspan=4)




#=======================================================================================================================================================

# Here are the fucntions for ManuBar.

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

#menuber1:

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="standerd",command=Standard)
filemenu.add_command(label="scientific",command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit",command = iExit)

#menuber2:

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Pest")

#menuber3:

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help")

root.configure(menu=menubar)



root.mainloop()