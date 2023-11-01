import ds
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pygame
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
smtp_server = "smtp.gmail.com"
sender_email = "architgupta0609@gmail.com"
port = 587  # For starttls

font_style = ("Helvetica", 20, "bold")
font_style3 = ("Helvetica", 25, "bold")

pygame.mixer.init()
pygame.mixer.music.load("restaurant-music-110483.mp3")
pygame.mixer.music.play()


root = Tk()
root.title("icecream parlour billing counter")
root.geometry("1000x600")
color = "#fcdcb1"
root.config(background="#fcdcb1")

date_label = Label(root,text=f"{ds.current_date}",font=font_style,background=color)
date_label.place(x=0,y=0)
day_label = Label(root,text=f"{ds.current_day1}",font=font_style,background=color)
day_label.place(x=0,y=25)

root1 = Toplevel(root)
root1.title("place order")
root1.geometry("1000x600")
root1.withdraw()
root1.config(background=color)

image = PhotoImage(file="png-transparent-ice-cream-parlor-milk-amul-ice-cream-shop-x-chin-cream-food-frozen-dessert-thumbnail.png")
image_label = Label(root, image=image)
image_label.place(x = 320,y=250)

# root.config(background='black')  # Green color using RGB value
font_style = ("Helvetica", 20, "bold")
font_style3 = ("Helvetica", 25, "bold")

# file = open("ice_parlour.csv", 'w')
# file.write("date ,Day ,Name ,items ,total amount\n")
# file.close()

ice = ['chocolate','Vanilla','Strawberry','butterscotch','tutti-fruity']
l = []
e = []
label1 = Label(root, text="WELCOME TO THE FABBRI ICECREAM PARLOUR",font=font_style,background=color)
label1.pack()
label2 = Label(root,text = "SELECT A OPTION :",font=font_style,background=color)
label2.place(x = 420, y = 50)
order = ds.queue()

def selected():
    qc,qv,qs,qb,qt = 0,0,0,0,0
    qc += int(s1.get())
    qv += int(s2.get())
    qs += int(s3.get())
    qb += int(s4.get())
    qt += int(s5.get())
    if(qc > 0):
        order.update1('chocolate',qc,100)
            # print(order.a)
    if(qv > 0):
        order.update1('Vanilla',qv,70)
    if(qs > 0):
        order.update1('Strawberry',qs,80)
    if(qb > 0):
        order.update1('Butterscotch',qb,110)
    if(qt > 0):
        order.update1('Tutti-fruity',qt,120)
    s1.delete(0,END)
    s1.insert(0, "0")
    s2.delete(0,END)
    s2.insert(0, "0")
    s3.delete(0,END)
    s3.insert(0, "0")
    s4.delete(0,END)
    s4.insert(0, "0")
    s5.delete(0,END)
    s5.insert(0, "0")
    
def final_order():
    if (order.a=={} or entry_name.get() == '' or entry_mail.get() == ''):
        messagebox.showerror("no orders found, try again!")
    else:
        order.total()
        order.final()
        l.append(entry_name.get())
        e.append(entry_mail.get())
        s1.delete(0,END)
        s1.insert(0, "0")
        s2.delete(0,END)
        s2.insert(0, "0")
        s3.delete(0,END)
        s3.insert(0, "0")
        s4.delete(0,END)
        s4.insert(0, "0")
        s5.delete(0,END)
        s5.insert(0, "0")
        entry_name.delete(0,END)
        entry_mail.delete(0,END)
def go_back():
    root1.withdraw()
    root.deiconify()
    s1.delete(0,END)
    s1.insert(0, "0")
    s2.delete(0,END)
    s2.insert(0, "0")
    s3.delete(0,END)
    s3.insert(0, "0")
    s4.delete(0,END)
    s4.insert(0, "0")
    s5.delete(0,END)
    s5.insert(0, "0")
    entry_name.delete(0,END)
    entry_mail.delete(0,END)
    
def place_order():
    root.withdraw()
    root1.deiconify()
    
def delivery():
    if(order.q == []):
        messagebox.showerror("no orders found, try again!")
    else:
        order.delete()
        file = open("ice_parlour.csv",'a')
        file.write(f"{ds.current_date} ,{ds.current_day1} ,{l[0]},{e[0]},")
        for i in order.q[0].items():
            file.write(f"{i[0]} : {i[1][0]}  ")
        file.write(f',{order.sum}\n')
        file.close() 
        l.pop(0)
        e.pop(0)
        order.q.pop(0)
        
def display_queue():
    if (order.q == []):
        messagebox.showerror("no order found")
    else:
        root4 = Toplevel(root)
        root4.title("display queue")
        root4.geometry("1000x600")
        root4.config(background=color)
        label_1 = Label(root4,text="**************************************************",font=font_style3,background=color)
        label_1.pack()
        label_2 = Label(root4,text="waiting orders :",font=font_style3,background=color)
        label_2.pack()
        for i in range(len(order.q)):
            label1 = Label(root4,text=f"{l[i]}",font=font_style3,background=color)
            label1.pack()
            label_3 = Label(root4,text=f"{order.q[i]}\n",font=font_style3,background=color)
            label_3.pack()
        label_4 = Label(root4,text="**************************************************",font=font_style3,background=color)
        label_4.pack()
        print(order.q)

        label_5 = Label(root4,text="THANKYOU FOR ORDERING IN FABBRI",font=font_style3,background=color)
        label_5.pack()
        
def send_email():
        message1 = f"hello Mr./Mrs.{l[-1]}\nThanks for ordering in Fabbri icecreams\nYour order on {ds.current_date} has been confirmed. Your order {order.q[-1]} will going to be delivered withing 10 - 15 minutes \ntotal amount : {order.sum}\nThanks,\nFABBRI ICECREAMS"
        msg =  MIMEMultipart() 
        msg['From']='architgupta0609@gmail.com'
        msg['To']= e[-1]
        msg['Subject']="FABBRI ICECREAMS"
        msg.attach(MIMEText(message1, 'plain'))
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls() # Secure the connection
        server.ehlo() # Can be omitted
        server.login('architgupta0609@gmail.com', 'enyvizrweszovmoi')
        server.send_message(msg)
        
        
def both():
    selected()
    final_order()
    send_email()
    
def exit():
    pygame.mixer.music.stop()
    root.quit()
#root
place_order_button = Button(root,text="PLACE ORDER",width=25,height=2,bg='green',command=place_order)
place_order_button.place(x = 30,y=100)


delivery_button = Button(root,text="ORDER TO BE DELIVERED",width=25,height=2,bg='green',command=delivery)
delivery_button.place(x = 380,y=100)

display_button = Button(root,text="DISPLAY QUEUE",width=25,height=2,bg='green',command=display_queue)
display_button.place(x = 700,y=100)

exit_button = Button(root,text="EXIT",width=25,height=2,bg='green',command=exit)
exit_button.place(x = 380,y=200)


#root1
label3 = Label(root1,text = 'SELECT WHAT YOU WANT TO HAVE :',font=font_style,background=color)
label3.pack()

clabel = Label(root1,text='chocolate :    Rs.100',font=font_style,background=color)
clabel.pack()

slabel = Label(root1,text='Vanilla :      Rs.70',font=font_style,background=color)
slabel.pack()

blabel = Label(root1,text='Strawberry :   Rs.80',font=font_style,background=color)
blabel.pack()

clabel = Label(root1,text='butterscotch : Rs.110',font=font_style,background=color)
clabel.pack()

tlabel = Label(root1,text='tooti-fruity : Rs.120',font=font_style,background=color)
tlabel.pack()

    
final_button = Button(root1,text="PLACE ORDER",width=25,height=2,bg='green',command=both)
final_button.place(x = 350,y=500)
    
s1 =Spinbox(root1,from_=0,to=20)
s1.place(x = 610,y=30)
    
s2 =Spinbox(root1,from_=0,to=20)
s2.place(x = 610,y=60)

s3 =Spinbox(root1,from_=0,to=20)
s3.place(x = 610,y=90)

s4 =Spinbox(root1,from_=0,to=20)
s4.place(x = 610,y=120)
    
s5 =Spinbox(root1,from_=0,to=20)
s5.place(x = 610,y=150)

go_back = Button(root1,text="GO BACK",width=25,height=2,bg='green',command=go_back)
go_back.place(x = 350,y=450)

email_label = Label(root1,text='ENTER YOUR EMAIL ID :',font=font_style,background=color)
email_label.place(x = 380,y = 200)

entry_mail = Entry(root1,width=20)
entry_mail.place(x = 400,y=250)

name_label = Label(root1,text='ENTER YOUR FULL NAME :',font=font_style,background=color)
name_label.place(x=370,y=300)


entry_name = Entry(root1,width=10)
entry_name.place(x = 450,y=350)
root.mainloop()
# chose = int(input("enter your choice(1...4) : "))
# print("**************************************************")
# while True
#     if(chose == 1):
#         while True:
#             print("""What would you like to have ?
#             1. chocolate          Rs 100/pc
#             2. Vanilla            Rs 70/pc
#             3. Strawberry         Rs 80/pc
#             4. Butterscotch       Rs 110/pc
#             5. Tutti-fruity       Rs 120/pc""")
#             choice = int(input("enter your choice (1...5) : "))
#             quantity = int(input("how many ice creams do you want? : "))


#             elif choice == 2:
#                 qv += quantity
#                 order.update('Vanilla', qv, 70)
#             elif choice == 3:
#                 qs += quantity
#                 order.update('Strawberry', qs, 80)
#             elif choice == 4:
#                 qb += quantity
#                 order.update('Butterscotch', qb, 110)
#             elif choice == 5:
#                 qt += quantity
#                 order.update('tutti-fruity', qt, 120)
#             else:
#                 print("enter a valid choice")
#             more = input("do you want to add more ?(y/n) : ")
#             if more == 'y':
#                 continue
#             else:
#                 order.total()
#                 order.final()
#                 break



#     elif(chose == 4):
#         print("THANKYOU FOR ORDERING")
#         print("**********************************")
#         break
#     else:
#         print("enter a valid choice, please try again!")

#     print("""welcome to icecream parlour
#     1. place order
#     2. order to be delivered
#     3. display queue
#     4. exit""")
#     chose = int(input("enter your(1...4) : "))






