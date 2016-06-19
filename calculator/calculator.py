#!/usr/bin/python3.4

from tkinter import *
import tkinter.messagebox as box

__author__ = "Youssef Seddik"
__version__ = '0.1'
__license__ = 'GNU GPLv3'

# Fonts used in the application(Constants)
OPS_FONT = ("Verdana", "16")
INTRM_FONT = ("Verdana", "11")
RES_FONT = ("Helvetica", "16", "bold")
DIGS_FONT = ("Helvetica", "10", "bold")


class Calculator(object):
    """
    A simple graphical calculator made with Tkinter v8.5 and Python 3.4, it
    contains the four basic operations on integers.
    In order to start the application, all we have to do is to import the
    Calculator class from the package calculator and instantiate
    the Calculator class.
    For example:
        >>> from calculator import Calculator
        >>> c = Calculator()
    """

    def __init__(self):
        """
        The initiator method wraps up all the application
        """
        self.window = Tk(className='Calculator')
        self.window.title('Calculator')
        self.window.resizable(0, 0)
        self.buildInterface()
        self.window.mainloop()

    def exitc(self):
        """
        Treatment for the Exit button.
        """
        var = box.askyesno('Quit', 'Are you sure you want to quit ?')
        if var == 1:
            # exit
            self.window.quit()
        else:
            pass

    def run(self):
        """
        Treatment for the Run button, which will run operation after entering
        operands and operators.
        """
        v1 = self.result.cget('text')
        v2 = self.intermediary.cget('text')
        self.result.configure(text='0')
        self.intermediary.configure(text=v2 + ' ' + v1)

        tmp = str(self.intermediary.cget('text'))
        tmp = tmp.split(" ")
        res = 0
        if len(tmp) == 3:
            for i in range(0, len(tmp) - 2):
                if tmp[i + 1] == '+':
                    res = res + int(tmp[i]) + int(tmp[i + 2])
                if tmp[i + 1] == '-':
                    res = res + int(tmp[i]) - int(tmp[i + 2])
                if tmp[i + 1] == '*':
                    res = res + int(tmp[i]) * int(tmp[i + 2])
                if tmp[i + 1] == '/':
                    res = res + int(tmp[i]) / int(tmp[i + 2])
        elif len(tmp) > 3:
            for i in range(0, len(tmp) - 2, 2):
                if i >= 2:
                    if tmp[i + 1] == '+':
                        res = res + int(tmp[i + 2])
                    if tmp[i + 1] == '-':
                        res = res - int(tmp[i + 2])
                    if tmp[i + 1] == '*':
                        res = res * int(tmp[i + 2])
                    if tmp[i + 1] == '/':
                        res = res / int(tmp[i + 2])
                elif i < 2:
                    if tmp[i + 1] == '+':
                        res = res + int(tmp[i]) + int(tmp[i + 2])
                    if tmp[i + 1] == '-':
                        res = res + int(tmp[i]) - int(tmp[i + 2])
                    if tmp[i + 1] == '*':
                        res = res + int(tmp[i]) * int(tmp[i + 2])
                    if tmp[i + 1] == '/':
                        res = res + int(tmp[i]) / int(tmp[i + 2])
        self.result.configure(text=res)

    def buildInterface(self):
        """
        Adds buttons and configures the geometry settings and layout
        """
        # result_frame = Frame(window, height = 10, width = 45)
        # digits_frame = Frame(window, height = 40, width = 35)
        # func_frame = Frame(window, height = 40, width = 10)
        self.intermediary = Label(self.window, width='33', height=2,
                                  font=INTRM_FONT, borderwidth=0, bg='#89b3cf',
                                  text='')
        self.result = Label(self.window, width='29', height=3,
                            font=RES_FONT, borderwidth=0, bg='#628997',
                            text='')
        dig_0 = Button(self.window, text='0', command=self.insert0,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_1 = Button(self.window, text='1', command=self.insert1,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_2 = Button(self.window, text='2', command=self.insert2,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_3 = Button(self.window, text='3', command=self.insert3,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_4 = Button(self.window, text='4', command=self.insert4,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_5 = Button(self.window, text='5', command=self.insert5,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_6 = Button(self.window, text='6', command=self.insert6,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_7 = Button(self.window, text='7', command=self.insert7,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_8 = Button(self.window, text='8', command=self.insert8,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        dig_9 = Button(self.window, text='9', command=self.insert9,
                       width=3, height=2, bd=4, fg='black', bg='#0066ff',
                       font='DIGS_FONT', relief=RIDGE)
        # dig_0.bind("<Left>", insert0)
        bt_c = Button(self.window, text='C', command=self.clear,
                      width=3, height=2, bd=4, bg='#0606ff', fg='black',
                      font='helvetica')
        bt_ce = Button(self.window, text="CE", command=self.clearE,
                       width=3, height=2, bd=4, bg='#0606ff', fg='black',
                       font='helvetica')
        bt_add = Button(self.window, text='+', command=self.add,
                        width=3, height=2, bd=4, fg='black', bg='#0ee618',
                        font=OPS_FONT, relief=GROOVE)
        bt_mul = Button(self.window, text='x', command=self.multiply,
                        width=3, height=2, bd=4, fg='black', bg='#0ee618',
                        font=OPS_FONT, relief=GROOVE)
        bt_div = Button(self.window, text='/', command=self.divide,
                        width=3, height=2, bd=4, fg='black', bg='#0ee618',
                        font=OPS_FONT, relief=GROOVE)
        bt_sub = Button(self.window, text='-', command=self.sub,
                        width=3, height=2, bd=4, fg='black', bg='#0ee618',
                        font=OPS_FONT, relief=GROOVE)

        bt_run = Button(self.window, text='Run', command=self.run,
                        width=12, height=2, bd=4, fg='green',
                        font='helvetica', relief=GROOVE)
        bt_exit = Button(self.window, text='Exit', command=self.exitc,
                         width=12, height=2, bd=4, fg='red',
                         font='helvetica', relief=GROOVE)
        # Geometry settings
        self.intermediary.grid(row=1, column=1, columnspan=4)
        self.result.grid(row=2, column=1, columnspan=4)
        dig_0.grid(row=6, column=2, padx=3, pady=2)
        dig_1.grid(row=3, column=1, padx=3, pady=2)
        dig_2.grid(row=3, column=2, padx=3, pady=2)
        dig_3.grid(row=3, column=3, padx=3, pady=2)
        dig_4.grid(row=4, column=1, padx=3, pady=2)
        dig_5.grid(row=4, column=2, padx=3, pady=2)
        dig_6.grid(row=4, column=3, padx=3, pady=2)
        dig_7.grid(row=5, column=1, padx=3, pady=2)
        dig_8.grid(row=5, column=2, padx=3, pady=2)
        dig_9.grid(row=5, column=3, padx=3, pady=2)
        bt_c.grid(row=6, column=3, padx=3, pady=2)
        bt_ce.grid(row=6, column=1, padx=3, pady=2)
        bt_add.grid(row=5, column=4, padx=3, pady=2)
        bt_mul.grid(row=3, column=4, padx=3, pady=2)
        bt_sub.grid(row=4, column=4, padx=3, pady=2)
        bt_div.grid(row=6, column=4, padx=3, pady=2)
        bt_run.grid(row=7, column=3, columnspan=2, padx=3, pady=2)
        bt_exit.grid(row=7, column=1, columnspan=2, padx=3, pady=2)

    # The 10 following functions are the instructions of buttons' actions
    def insert0(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '0')
        elif (len(v) == 0):
            self.result.configure(text='0')
        if (v == '0'):
            self.result.configure(text='0')

    def insert1(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '1')
        elif (len(v) == 0):
            self.result.configure(text='1')
        if (v == '0'):
            self.result.configure(text='1')

    def insert2(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '2')
        elif (len(v) == 0):
            self.result.configure(text='2')
        if (v == '0'):
            self.result.configure(text='2')

    def insert3(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '3')
        elif (len(v) == 0):
            self.result.configure(text='3')
        if (v == '0'):
            self.result.configure(text='3')

    def insert4(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '4')
        elif (len(v) == 0):
            self.result.configure(text='4')
        if (v == '0'):
            self.result.configure(text='4')

    def insert5(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '5')
        elif (len(v) == 0):
            self.result.configure(text='5')
        if (v == '0'):
            self.result.configure(text='5')

    def insert6(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '6')
        elif (len(v) == 0):
            self.result.configure(text='6')
        if (v == '0'):
            self.result.configure(text='6')

    def insert7(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '7')
        elif (len(v) == 0):
            self.result.configure(text='7')
        if (v == '0'):
            self.result.configure(text='7')

    def insert8(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '8')
        elif (len(v) == 0):
            self.result.configure(text='8')
        if (v == '0'):
            self.result.configure(text='8')

    def insert9(self):
        v = self.result.cget('text')
        if (len(v) > 0):
            self.result.configure(text=v + '9')
        elif (len(v) == 0):
            self.result.configure(text='9')
        if (v == '0'):
            self.result.configure(text='9')

    def clear(self):
        """
        Treatment for the Clear(C) button, which clears the two labels: the
        result label and the intermediary label.
        """
        self.result.configure(text='0')
        self.intermediary.configure(text='')

    def clearE(self):
        """
        Treatment for the ClearE(CE) button, which clears the last entered
        element to the intermediary label
        """
        v = self.result.cget('text')
        if (len(v) == 1):
            self.result.configure(text='0')
        elif (len(v) > 1):
            l = len(v)
            tmp = v[0: l - 1]
            self.result.configure(text=tmp)

    def add(self):
        """
        This method is used by the sum(+) button to insert the operation
        sign to the intermediary label
        """
        v1 = self.result.cget('text')
        v2 = self.intermediary.cget('text')
        op1 = v1
        op2 = '+'
        self.result.configure(text='0')
        if (v2 == ''):
            self.intermediary.configure(text=op1 + ' ' + op2)
        else:
            self.intermediary.configure(text=v2 + ' ' + op1 + ' ' + op2)

    def multiply(self):
        """
        This method is used by the multiply(*) button to insert the
        operation sign to the intermediary label
        """
        v1 = self.result.cget('text')
        v2 = self.intermediary.cget('text')
        op1 = v1
        op2 = '*'
        self.result.configure(text='0')
        if (v2 == ''):
            self.intermediary.configure(text=op1 + ' ' + op2)
        else:
            self.intermediary.configure(text=v2 + ' ' + op1 + ' ' + op2)

    def divide(self):
        """
        This method is used by the divide(/) button to insert the operation
        sign to	the intermediary label
        """
        v1 = self.result.cget('text')
        v2 = self.intermediary.cget('text')
        op1 = v1
        op2 = '/'
        self.result.configure(text='0')
        if (v2 == ''):
            self.intermediary.configure(text=op1 + ' ' + op2)
        else:
            self.intermediary.configure(text=v2 + ' ' + op1 + ' ' + op2)

    def sub(self):
        """
        This method is used by the sub(-) button to insert the operation
        sign to the intermediary label
        """
        v1 = self.result.cget('text')
        v2 = self.intermediary.cget('text')
        op1 = v1
        op2 = '-'
        self.result.configure(text='0')
        if (v2 == ''):
            self.intermediary.configure(text=op1 + ' ' + op2)
        else:
            self.intermediary.configure(text=v2 + ' ' + op1 + ' ' + op2)
