from tkinter import *
from bs4 import BeautifulSoup
import requests

root=Tk()
value_text=Label(root)
numerical_text=Label(root)
procentual_text=Label(root)

def quit():
    root.destroy()

def click(link):

    delete()

    ''' Algorithm'''
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text,'lxml')

    raw_data = soup.find('div', { 'class' : 'D(ib) Mend(20px)' } ).text


    if raw_data.find('-') == -1 :
        last_pos_value = raw_data.find('+')
        
    else :
        last_pos_value = raw_data.find('-')

    value= raw_data [0 :last_pos_value]
    raw_data = raw_data [ last_pos_value : ]

    stop_num_variation = raw_data.find(' ')
    numerical_variation = raw_data [ 0 : stop_num_variation ]
    raw_data = raw_data [ stop_num_variation+2 : ]

    stop_procentual_variation = raw_data.find(')')
    procentual_variation = raw_data [0 : stop_procentual_variation ]

    ''' creating the interface '''

    value_title_text = Label(root,text = 'Price : ')
    my_canvas.create_window ( 30, 140, anchor="nw", window = value_title_text )
    
    global value_text 
    value_text= Label(root, text = value)
    my_canvas.create_window ( 30, 160, anchor="nw", window = value_text )

    num_var_title_text = Label(root,text = 'Numerical variation : ')
    my_canvas.create_window ( 150, 140, anchor="nw", window = num_var_title_text )

    global numerical_text 
    numerical_text= Label(root, text = numerical_variation)
    my_canvas.create_window ( 150, 160, anchor="nw", window = numerical_text )

    proc_var_title_text = Label(root,text = 'Procentual variation : ')
    my_canvas.create_window ( 320, 140, anchor="nw", window = proc_var_title_text )

    global procentual_text 
    procentual_text= Label(root, text = procentual_variation)
    my_canvas.create_window ( 320, 160, anchor="nw", window = procentual_text )

def delete():
    value_text.destroy()
    numerical_text.destroy()
    procentual_text.destroy()
    

root.title('Daily Evolution ')
root.geometry('500x370')
my_canvas = Canvas( root, width = 330 , height = 150)
my_canvas.pack(fill="both",expand=True)

button_sp = Button(root, text="S&P 500",command = lambda: click('https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC'))
button_window_sp = my_canvas.create_window( 140, 90 , anchor="nw", window = button_sp)

button_gold = Button(root, text="Gold",command = lambda: click('https://finance.yahoo.com/quote/GC=F?p=GC=F&.tsrc=fin-srch'))
button_window_gold = my_canvas.create_window( 70, 90 , anchor="nw", window = button_gold)

button_oil = Button(root, text="Oil",command = lambda: click('https://finance.yahoo.com/quote/CL=F?p=CL=F&.tsrc=fin-srch'))
button_window_oil = my_canvas.create_window( 240, 90 , anchor="nw", window = button_oil)

button_silver = Button(root, text="Silver",command = lambda: click('https://finance.yahoo.com/quote/SI=F?p=SI=F&.tsrc=fin-srch'))
button_window_silver = my_canvas.create_window( 310, 90 , anchor="nw", window = button_silver)

button_natural_Gas = Button(root, text="Natural Gas",command = lambda: click('https://finance.yahoo.com/quote/NG=F?p=NG=F&.tsrc=fin-srch'))
button_window_nat_gas = my_canvas.create_window( 380, 90 , anchor="nw", window = button_natural_Gas)

button_quit = Button(root, text="Quit",command = lambda: quit())
button_window_quit = my_canvas.create_window( 400, 300 , anchor="nw", window = button_quit)

Title_text = Label(root, text = "The Market : ", font =("Helvetica",12))
title_window = my_canvas.create_window ( 187, 40, anchor="nw", window=Title_text )
root.mainloop()