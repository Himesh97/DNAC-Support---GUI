from tkinter import *
from DNAC_info_popup import *
import atexit
from  file_ops import *

window = Tk()

window.title("DNAC Center GUI")
window.geometry('1000x500')

header = Label(window , text="DNAC Support Center" , font=("Arial Bold", 50) , fg = "red" )
header.pack()
############

#############
doted_Field_1 = Label(window, text="...............................................................................................................................................................................................................................................")
doted_Field_1.pack()

text_Field_1 = Label(window , text="This will help you to get devices information in your network" , font=("Times",14))
text_Field_1.pack()

doted_Field_2 = Label(window, text="...............................................................................................................................................................................................................................................")
doted_Field_2.pack()

line_break = Label(window , text="\n")
line_break.pack()

get_btn = PhotoImage(file ="img/3.png") 
button = Button(window, image =get_btn, borderwidth = 0, command = dnac_details_popup )
button.pack()

line_break = Label(window , text="\n")
line_break.pack()





    
    
if __name__ == '__main__':
    
    x=isClicked()
    if(x==1):
        text_Field_test = Label(window , text="hello", font=("Times",14), width=50 , height=10,bg="blue")
        text_Field_test.pack()
    
    window.mainloop()
    #print(x)

#f.grid(row=3, column=0)


