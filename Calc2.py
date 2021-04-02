from tkinter import *
from tkinter import ttk

font10 = "-family {Microsoft Sans Serif} -size 26 - weigth bold" \
" -slant roman -underline 0 -overstrike 0"
font12 = "family {Segoe UI} -size 16 -weigt normmal -slant " \
"roman -underline 0 -overstrike 0"
font14 = "family {Segoe UI} -size 16 -weigh bold -slant " \
"roman -underline 0 -overstrike 0"

dic={"activebackground":"#d9d9d9","activeforeground":"000000",
     "background":"#f0f0f0","borderwidth":"0",
     "disabledforeground":"#a3a3a3","font":font12,
     "foreground":"#000000","highlightbackground":"#d9d9d9",
     "highlightcolor":"black","pady":"0",}

dic2=dic.copy()
dic2.update({"background":"#fffff","font":font13})

def root(x):
    return x**1/2

def cube(x):
    return x**1/9

def foo(str_,lis={'M':'%','3v':'cube','v':'root','x':'*'}):
    for i in lis:
        str = lis[i].join(j for j in str_.split(i))
    return str_


class Calculator:
    def __init__(self, root):
        self.root=root
        self.main_var=StringVar()
        self.root.geometry("340x336+575+128")
        self.root.title("Calculator")
        self.root.configure(background="#d9d9d9")
        self.e  = Entry(self.root, background="#e6e6e6", borderwidth="0", disabledforeground="#a3a3a3",
                        font=font10,foreground="#000000",insertbackground="black",justify=RIGHT,
                        width=17, textvariable=self.main_var)

        self.e.place(x=0, y=0, heitght=70)
        #parte do outro programa;
        def main(self):
            bb = Label(janela, text='ok')
            bb.grid(row=2, column=0)

        def main2(self, i):
            self.caixa.insert(END, i)
            print('aa')

        def __init__(self):
            janela = Tk()
            self.lista = ['x', '/', '-', '+']
            self.caixa = Entry(janela)
            self.caixa.grid(columnspan=4, padx=5, pady=5)
            bbb = Button(janela, text=('='), width=22)
            bbb.grid(row=4, column=2, columnspan=2)

            b = Button(janela, width=30, text=('butao'), command=self.main)
            # b.pack(anchor='nw')

            aa = Label(janela, text='Clique aqui: ')
            # aa.grid(row=0,column=0)

            # b.grid(row=1,column=0)
            a = 0
            b = 0
            for i in range(0, 10):

                self.c = Button(janela, width=10, text=i, command=lambda: self.main2(i))
                # d = StringVar(i)
                if a < 2:
                    a += 1
                    self.c.grid(row=b + 1, column=a, padx=2, pady=2)

                else:
                    a += 1
                    self.c.grid(row=b + 1, column=a, padx=2, pady=2)
                    a = 0
                    b += 1
            vv = 1
            for i in self.lista:
                ss = Button(janela, text=i, width=10)
                ss.grid(row=vv, column=4)
                vv += 1
            janela.geometry('999x500+500+100')
            janela.title('Jokempo v0.o')
            janela.mainloop()

        self.data=[()]
        self.place_elements()

    def clear(self):
        self.main_var.set("")

    def btn_text(self,txt,brac=False,front_cal=False):
        if front_cal:
            self.main_var.set(txt+'('+self.main_var.get()+')')
        elif brac:
            self.main_var.set('('+self.main_var.get()+')'+txt)
        else:
            self.main_var.set(self.main_var.get()+txt)

    def clear_last(self):
        if len(self.main_var.get())!=0:
            if self.main_var.get()[0] =='-':
                self.main_var.set(self.main_var.get()[1:])
            else:
                self.main_var.set('-'+self.main_var.get())
        else:
            self.main_var.set('-')

    def result(self):
        if self.main_var.get()!='':
            try:
                self.main_var.set(eval(foo(self.main_var.get())))
            except:
                self.main_var.set("Invalid Input")

    def place_elements(self):
        lis=self.root.winfo_children()[1:]
        for i in range(len(lis)):
            lis[i].place(x=self.data[i][0], y=self.data[i][1],
                    height=50, width=63)

def main():
    window = Tk()
    window.resizable(0,0)
    Calculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()














