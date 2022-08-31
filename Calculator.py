#Libs
import tkinter as tk
from tkinter import ttk
#Init
current_value=''
#Calculation
def inserting_values(x):
    global current_value
    current_value+=x
    text_result.delete(1.0,'end')
    text_result.insert(1.0,current_value)

def calculating():
    global current_value
    try:
        result=str(eval(current_value))
        current_value=result
        text_result.delete(1.0,'end')
        text_result.insert(1.0,result)
    except:
        text_result.delete(1.0,'end')
        text_result.insert(1.0,'Error')
def clearing():
    global current_value
    text_result.delete(1.0,'end')
    current_value=''
#Display procedure
root=tk.Tk()
root.title('Calculator')
root.minsize(250,300)
root.wm_iconbitmap('C:/Users/grzeg/Documents/Python/Nauka/calculator_icon.ico')

label=ttk.Label(root,text='Standardowy')
label.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)

text_result = tk.Text(root, height=2, width=16)
text_result.grid(columnspan=5,row=1)

button_1=ttk.Button(root,text='1',command=lambda: inserting_values('1'))
button_1.grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)

button_2=ttk.Button(root,text='2',command=lambda: inserting_values('2'))
button_2.grid(column=1,row=6,padx=5,pady=5)

button_3=ttk.Button(root,text='3',command=lambda: inserting_values('3'))
button_3.grid(column=2,row=6,padx=5,pady=5)

button_4=ttk.Button(root,text='4',command=lambda: inserting_values('4'))
button_4.grid(column=0,row=5,sticky=tk.W,padx=5,pady=5)

button_5=ttk.Button(root,text='5',command=lambda: inserting_values('5'))
button_5.grid(column=1,row=5,sticky=tk.W,padx=5,pady=5)

button_6=ttk.Button(root,text='6',command=lambda: inserting_values('6'))
button_6.grid(column=2,row=5,sticky=tk.W,padx=5,pady=5)

button_7=ttk.Button(root,text='7',command=lambda: inserting_values('7'))
button_7.grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)

button_8=ttk.Button(root,text='8',command=lambda: inserting_values('8'))
button_8.grid(column=1,row=4,sticky=tk.W,padx=5,pady=5)

button_9=ttk.Button(root,text='9',command=lambda: inserting_values('9'))
button_9.grid(column=2,row=4,sticky=tk.W,padx=5,pady=5)

button_0=ttk.Button(root,text='0',command=lambda: inserting_values('0'))
button_0.grid(column=1,row=7,sticky=tk.W,padx=5,pady=5)

button_add=ttk.Button(root,text='+',command=lambda: inserting_values('+'))
button_add.grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)

button_substract=ttk.Button(root,text='-',command=lambda: inserting_values('-'))
button_substract.grid(column=1,row=3,sticky=tk.W,padx=5,pady=5)

button_multiplication=ttk.Button(root,text='*',command=lambda: inserting_values('*'))
button_multiplication.grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)

button_divide=ttk.Button(root,text='/',command=lambda: inserting_values('/'))
button_divide.grid(column=1,row=2,sticky=tk.W,padx=5,pady=5)

button_sum=ttk.Button(root,text='=',command= lambda:calculating())
button_sum.grid(column=2,row=2,sticky=tk.W,padx=5,pady=5)

button_del=ttk.Button(root,text='DEL',command= lambda:clearing())
button_del.grid(column=2,row=3,sticky=tk.W,padx=5,pady=5)

root.mainloop()
