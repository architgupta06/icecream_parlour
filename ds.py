from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import ttk

current_datetime = datetime.now()
current_date = date.today()
current_day = current_date.weekday()
current_day1 = current_datetime.strftime('%A')
font_style = ("Helvetica", 20, "bold")
font_style2 = ("Helvetica", 15, "bold")
color = "#fcdcb1"
class queue:
    q = []
    a = {}
    sum = 0
    def update1(self,item,qty,price):
        queue.a.update({item : [qty,qty*price]})

    def final(self):
        queue.q.append(queue.a)
        root2 = Tk()
        root2.title("FINAL ORDER")
        root2.geometry("1000x600")
        root2.resizable(False,False)
        root2.config(background=color)
        label6 = Label(root2,text = 'YOUR FINAL ORDER IS :\n',font=font_style,background=color)
        label6.pack()
                # print("your final order is :")
        for i in queue.a.items():
            label7 = Label(root2,text=f"{i[0]} : {i[1][0]}\n",font=font_style,background=color)
            label7.pack()
        queue.a = {}
        label5 = Label(root2,text = '*******************************************************************************************************',font=font_style,background=color)
        label5.pack()
        label5 = Label(root2,text = 'THANKYOU FOR ORDERING IN FABRRI !',font=font_style,background=color)
        label5.pack()

    def display(self):
        print(queue.q)


    def total(self):
        for i in queue.a.values():
            queue.sum += i[1]

        
    def delete(self):
        root3 = Tk()
        root3.title("FINAL ORDER")
        root3.geometry("1000x600")
        root3.config(background=color)
        
        tree = ttk.Treeview(root3,height=(len(queue.q[0])))
        ready_label = Label(root3,text=f"your order is ready :",font=font_style,background=color)
        ready_label.pack()
        tree['columns'] = ('item', 'quantity', 'price')

        # Define column headings
        tree.heading('#0', text=None)
        tree.heading('item', text='item')
        tree.heading('quantity', text='qty')
        tree.heading('price', text='price')
        
        # tree.insert(values=('John Doe', '25', 'New York'))
        # tree.insert('', 'end', text='2', values=('Jane Smith', '30', 'London'))
        # tree.insert('', 'end', text='3', values=('Bob Johnson', '40', 'Paris'))
        for i in queue.q[0].items():
            # print_label = Label(root3,text=f"{i[0]}               {i[1][0]}        {i[1][1]}",font=font_style,background=color)
            # print_label.pack()
            tree.insert('', 'end',values=(f"{i[0]}", f"{i[1][0]}", f"{i[1][1]}"))
        tree.column('#0', width=0)
        tree.column('item', width=150)
        tree.column('quantity', width=150)
        tree.column('price', width=100)
        tree.pack()
        total = Label(root3,text=f"your total amount is {queue.sum}",font=font_style2,background=color)
        total.pack()

        if (queue.sum > 650):
            if (current_day == 1 or current_day == 5):
                l1 = Label(root3,text=f"Congratulations!, you have availed 10% discount",font=font_style2,background=color)
                l1.pack()
                queue.sum = queue.sum - queue.sum*(10 / 100)
                l2 = Label(root3,text=f"your total amount after discount is {queue.sum}",font=font_style2,background=color)
                l2.pack()
                # print("your total amount after discount is ", queue.sum)
                # print("**************************************************")
                l3 = Label(root3,text=f"**************************************************",font=font_style2,background=color)
                l3.pack()
            else:
                l1 = Label(root3,text=f"Congratulations!, you have availed 5% discount",font=font_style2,background=color)
                l1.pack()
                # print(f"you have availed 5% discount")
                queue.sum = queue.sum - queue.sum*(5 / 100)
                l2 = Label(root3,text=f"your total amount after discount is {queue.sum}",font=font_style2,background=color)
                l2.pack()
                # print("your total amount after discount is ", queue.sum)
                # print("**************************************************")
                l3 = Label(root3,text=f"**************************************************",font=font_style2,background=color)
                l3.pack()
        elif (current_day == 1 or current_day == 5):
                # print(f"you have availed 10% discount")
                l1 = Label(root3,text=f"Congratulations!, you have availed 5% discount",font=font_style2,background=color)
                l1.pack()
                queue.sum = queue.sum - queue.sum * (5 / 100)
                # print("your total amount after discount is ", queue.sum)
                l2 = Label(root3,text=f"your total amount after discount is {queue.sum}",font=font_style2,background=color)
                l2.pack()
                # print("**************************************************")
                l3 = Label(root3,text=f"**************************************************",font=font_style2,background=color)
                l3.pack()
        l4 = Label(root3,text="THANKYOU FOR ORDERING IN FABBRI",font=font_style,background=color)
        l4.pack()



# c1 = queue()
# c2 = queue()
# c3 = queue()
# c1.update('vanilla',2,70)
# c1.final()
# c2.update('chocolate',3,80)
# c3.update('tooti fruity',2,60)
# c3.final()
# c3.display()
# c3.delete()
# c3.display()
