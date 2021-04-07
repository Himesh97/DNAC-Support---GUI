from tkinter import *
from dnac_config import *
from tkinter import messagebox
from get_token import *
#from isclicked import isClicked
from get_device_info import *
from  print_device_info import *
from tkinter.ttk import Progressbar 


#DNAC Info

#f.readlines(1)
#isClicked = 0

#clicked = 0
device_list=""
params_ip = "" 
def dnac_details_popup():
    #global isClicked
    #isClicked = 0
    
    
    window_popup = Tk()
    window_popup.title("DNA Center Information")

    w = 400
    h = 600

    sw = window_popup.winfo_screenwidth()
    sh = window_popup.winfo_screenheight()

    x = (sw - w)/2
    y = (sh - h)/2
    window_popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
     
    #alert_btn = PhotoImage(file ="alert.png")
    #button = Label(window, image = alert_btn, borderwidth = 0 )
    #button.pack()
    
    #msg_keys = ["IP Address : " , "Port : " , "User Name : " , "Password : "]
    #info = [ ip ,port , usrname , pw ]
    #content = " "
    
     
        
    msg = "Alert !!! " + "\n" + "Please check the DNA Center Information"
    
    w = Label(window_popup , text=msg, width=120, height=10 , font=("Arial Bold", 12) , fg = "red")
    w.pack()

    
    L1 = Label(window_popup, text="Domain Name" , font = ('calibre',10,'bold'))
    L1.pack( )
    E1 = Entry(window_popup,bd =2,width=35)    
    E1.insert(0,DNAC_IP)
    E1.pack()
    #dname - Domain Name
    dname = E1.get()

    L2 = Label(window_popup, text="Port Number" , font = ('calibre',10,'bold'))
    L2.pack( )
    E2 = Entry(window_popup, bd =2,width=35)
    E2.insert(0,DNAC_PORT)
    E2.pack()
    #port - Port Number
    port = E2.get()

    L3 = Label(window_popup, text="Username" , font = ('calibre',10,'bold'))
    L3.pack( )
    E3 = Entry(window_popup,bd =2,width=35)
    E3.insert(0,USERNAME)
    E3.pack()
    #usrname - User Name
    usrname = E3.get()

    L4 = Label(window_popup, text="Password" , font = ('calibre',10,'bold'))
    L4.pack( )
    E4 = Entry(window_popup, bd =2,width=35)
    E4.insert(0,PASSWORD)
    E4.pack()
    #pw - Password
    pw = E4.get()

    L5 = Label(window_popup, text="Version" , font = ('calibre',10,'bold'))
    L5.pack( )
    E5 = Entry(window_popup, bd =2,width=35)
    E5.insert(0,VERSION)
    E5.pack()
    #v - Version
    v = E5.get()
       
        
    #content = Label(window_popup , text=ip)
    #content.pack()

    #print(content)
    
    b = Button(window_popup , text="OK", command=lambda:hide_button(b), width=10)
    b1 = Button(window_popup , text="Proceed" ,command=lambda:[token_window(),window_popup.destroy()],width=10)
    #isClicked = 0
   
    #flag = True
    #while flag:
        #b1 = Button(window_popup , text="Proceed" ,command=window_popup.destroy,width=10)
        #flag = False
        #isClicked = 0
    #print(isClicked)
       
    
    #b.pack(side = LEFT , padx =85)
    #b1.pack(side = LEFT )
    b.place(x=100,y=470)
    b1.place(x=220,y=470)
    #isClicked = 0
    #print(isClicked)

    mainloop()
    #print(x)
 

#def wish():
    #messagebox.showwarning("Confirmation", "Are you wish to proceed? ")
    #grid_forget()

def hide_button(button):
    messagebox.showwarning("Confirmation", "Are you wish to proceed? ")
    button.place_forget()

def is_clicked():
    f = open("clicked.txt" , "w")
    #global isClicked
    #global clicked
    #isClicked = 1
    clicked = 1
    f.write(str(clicked))
    f.close
    
def get_token():
    messagebox.showwarning("Confirmation", "Are you wish to proceed? ")
    #get_auth_token()
    
def token_window():
    
    window_sub = Tk()
    window_sub.title("Token")
    window_sub.geometry('1500x400')

    header_sub= Label(window_sub , text="Token" , font=("Tekton Pro", 24) , fg = "blue" )
    header_sub.pack()

    token = get_auth_token()
    len_token = len(token)
    x = len_token//10
    s = str(token[0: x]) + "\n" + str(token[x:x+70]) + "\n" + str(token[x+70:x+140]) + "\n" + str(token[x+140:x+210]) + str(token[x+210:x+280]) + "\n" + str(token[x+280:x+350])+ str(token[x+350:x+420]) + "\n" + str(token[x+420:x+510])+ str(token[x+510:x+580]) + "\n" + str(token[x+580:x+650]) + str(token[x+650:]) 
    text_Field_test = Label(window_sub , text=s, font=("Arial",12), bg="sky blue")#width=50 , height=10,)
    text_Field_test.pack()

    line_break = Label(window_sub , text="\n")
    line_break.pack()
    
    get_btn_2 = PhotoImage(file ="img/4.png")
    #a=[(1,'Raj','Mumbai',19),(2,'Aaryan','Pune',18),(3,'Vaishnavi','Mumbai',20)]

    a = get_dev_info()
    button = Button(window_sub, text = "Show Devices", width = 10 , command = lambda:[show_devices(a),window_sub.destroy()], bg="green" )
    button.pack()
    #print(type(s))
    #print(len_token)
    #print(token[0: x])
    #window_sub.mainloop()

#def check_close():
    #return 1


#dnac_details_popup()
#print(clicked)

#token_window()

def show_devices(devList):
    global device_list

    
    
    def returnEntry():
        
        global result
        result = find_entry.get()
       #resultLabel.config(text=result)
        #print(result)
        find_entry.delete(0,END)
        #print("i am here")
        #print(devList)
       #device_list = result
        #print(result)

        ## Searching ##
        index_y = len(devList)
        index_y_1 = len(devList[1])
        #print(index_y)
        print(index_y_1)

        for i in range(index_y):
            for j in range(index_y_1):
                if(devList[i][j] == result):
                    #print(devList[i][j])
                    #print(i)
                    space = Label(window_dev, text="     ")
                    hostname = Label(window_dev, text="Host Name", font=('Arial',10) , fg = "firebrick1" )
                    ip = Label(window_dev, text="IP Address", font=('Arial',10) , fg = "firebrick1")
                    serial = Label(window_dev, text="Serial Number", font=('Arial',10) , fg = "firebrick1")
                    platform = Label(window_dev, text="Platform ID", font=('Arial',10) , fg = "firebrick1")
                    ver = Label(window_dev, text="Software Version", font=('Arial',10) , fg = "firebrick1")
                    role = Label(window_dev, text="Role", font=('Arial',10) , fg = "firebrick1")
                    uptime = Label(window_dev, text="Up Time", font=('Arial',10), fg = "firebrick1")
    
                    space.grid(row=Lrows + 5, column = 4)
                    hostname.grid(row=Lrows + 6,column=4)
                    ip.grid(row=Lrows + 7,column=4)
                    serial.grid(row=Lrows + 8,column=4)
                    platform.grid(row=Lrows + 9,column=4)
                    ver.grid(row=Lrows + 10,column=4)
                    role.grid(row=Lrows + 11,column=4)
                    uptime.grid(row=Lrows + 12,column=4)

                    #values

                    hostname_val = devList[i][0]
                    ip_val = devList[i][1]
                    serial_val = devList[i][2]
                    platform_val = devList[i][3]
                    ver_val = devList[i][4]
                    role_val = devList[i][5]
                    uptime_val = devList[i][6]

                    hostname_val_lbl = Label(window_dev, text=hostname_val, font=('Arial',10), fg = "dark violet")
                    ip_val_lbl  = Label(window_dev, text=ip_val, font=('Arial',10), fg = "dark violet")
                    serial_val_lbl  = Label(window_dev, text=serial_val, font=('Arial',10), fg = "dark violet")
                    platform_val_lbl  = Label(window_dev, text=platform_val, font=('Arial',10), fg = "dark violet")
                    ver_val_lbl  = Label(window_dev, text=ver_val, font=('Arial',10), fg = "dark violet")
                    role_val_lbl  = Label(window_dev, text=role_val, font=('Arial',10), fg = "dark violet")
                    uptime_val_lbl  = Label(window_dev, text=uptime_val, font=('Arial',10), fg = "dark violet")
                    space = Label(window_dev, text="     ")

                    
                    hostname_val_lbl.grid(row=Lrows + 6,column=5)
                    ip_val_lbl.grid(row=Lrows + 7,column=5)
                    serial_val_lbl.grid(row=Lrows + 8,column=5)
                    platform_val_lbl.grid(row=Lrows + 9,column=5)
                    ver_val_lbl.grid(row=Lrows + 10,column=5)
                    role_val_lbl.grid(row=Lrows + 11,column=5)
                    uptime_val_lbl.grid(row=Lrows + 12,column=5)
                    space.grid(row=Lrows + 13, column = 4)

                    connect_btn = Button(window_dev,text="Connect" , width = 10 , bg = "lawn green" , fg = "white")
                    connect_btn.grid(row=Lrows + 14,column=4)

                    

        
        

    
    
    
       
    window_dev = Tk()
    window_dev.title("Devices")
    window_dev.geometry('1250x600')
    #header_dev= Label(window_dev , text="Devices" , font=("Tekton Pro", 24) )
    #header_dev.grid(row = 0 , column =3)
    line_break = Label(window_dev , text="\n")
    #line_break.grid(row = 0 , column =0)

    global params_ip
    Lrows = len(devList)
    Lcolumns = len(devList[0])

    for i in range(Lrows):
        for j in range(Lcolumns):
            name_lbl = Label(window_dev , text="Device Infomations",font=('Arial',14))
            name_lbl.grid(row = 0,column = 4)
            #line_break = Label(window_dev , text="\n")
            #line_break.grid(row = 1 , column =1)
            space_lbl = Label(window_dev,text="             ")
            e = Entry(window_dev , width = 22, font=('Arial',10))
            space_lbl.grid(row = 0,column = j)
            e.grid(row = i+1, column = j+1)
            e.insert(END, devList[i][j])


    #line_break = Label(window_dev , text="\n")
    #line_break.grid(row = Lrows+1 , column =0)

    line_break = Label(window_dev , text="\n")
    line_break.grid(row = Lrows+2 , column =0)
    
    find_lbl=Label(window_dev,text="Device IP " , font=('Arial',10))
    find_entry = Entry(window_dev ,width = 33)
    find_entry.focus()
    find_lbl.grid(row = Lrows + 3, column = 4)
    #e = find_entry.get()
    find_entry.grid(row = Lrows + 4, column = 4)
   # params_ip = find_entry.get()
    #test = Label(window_dev, text=str(params_ip))
   # test.grid(row = Lrows + 5, column = 4)

   

    #resultLabel = Label(window_dev, text = "")
   # resultLabel.grid(row = Lrows + 5, column = 6)

    

    #print(e)

    find_button = Button(window_dev,text="Find" , command=returnEntry, width = 10 , bg = "red" , fg = "white")
    find_button.grid(row = Lrows + 4, column = 5 )
    #return e
    #device_list = returnEntry()
    #x=returnEntry()
    #print(x)
    #print(result)
    window_dev.mainloop()

    #get_dev_info(params_ip)

def device_info_window():

    
    device_info_window = Tk()
    device_info_window.title("Devices")
    device_info_window.geometry('400x500')
    
    space = Label(device_info_window, text="     ")
    hostname = Label(device_info_window, text="     Host Name", font=('Arial',10))
    ip = Label(device_info_window, text="     IP Address", font=('Arial',10))
    serial = Label(device_info_window, text="     Serial Number", font=('Arial',10))
    platform = Label(device_info_window, text="     Platform ID", font=('Arial',10))
    ver = Label(device_info_window, text="     Software Version", font=('Arial',10))
    role = Label(device_info_window, text="     Role", font=('Arial',10))
    uptime = Label(device_info_window, text="     Up Time", font=('Arial',10))
    
    space.grid(row=0,column=0)
    hostname.grid(row=1,column=0)
    ip.grid(row=2,column=0)
    serial.grid(row=3,column=0)
    platform.grid(row=4,column=0)
    ver.grid(row=5,column=0)
    role.grid(row=6,column=0)
    uptime.grid(row=7,column=0)

    y = get_dev_info()
    #print(y)
    

         
    
            
#token_window()

