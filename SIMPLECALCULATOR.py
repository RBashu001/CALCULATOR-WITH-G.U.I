#JAI SRI RAM
#SIMPLE CALCULATOR WITH G.U.I
from tkinter import*
#working with backend things-->
#display....
#................ 
def get_digit(digit):
    result_label.config(text=result_label['text']+str(digit))
#functions for operators....
#................
def clr():
    result_label.config(text='')
def get_oprtr(op):
    global oprnd1,oprt,sizeo1
    oprnd1=float(result_label['text'])
    oprt=op
    result_label.config(text=result_label['text']+str(op))
    sizeo1=len(result_label['text'])
def result():
    global oprnd1,oprt,oprnd2,sizeo1
    result=0
    temp=result_label['text']
    temp=temp[sizeo1:len(result_label['text'])]
    oprnd2=float(temp)
    if oprt=='+':
        result=oprnd1+oprnd2
    elif oprt=='-':
        result=oprnd1-oprnd2
    elif oprt=='*':
        result=oprnd1*oprnd2
    elif oprt=='/':
        result=oprnd1/oprnd2
    result_label.config(text=result)   
#UI PART....
#................
root=Tk()
root.title('Calculator')
root.geometry('280x380')#it fixes the initial appearance size of window
root.resizable(0,0)#it doesn't allow you to alter size of the window
root.config(background='black')
result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.configure(font=('verdana',30,'bold'))
#operand_buttons....
#................
btn7=Button(root,text='7',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(7))
btn7.grid(row=1,column=0,sticky='w')
btn7.config(font=('verdana',14))
btn8=Button(root,text='8',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(8))
btn8.grid(row=1,column=1,sticky='w')
btn8.config(font=('verdana',14))
btn9=Button(root,text='9',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(9))
btn9.grid(row=1,column=2,sticky='w')
btn9.config(font=('verdana',14))
btn4=Button(root,text='4',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(4))
btn4.grid(row=2,column=0,sticky='w')
btn4.config(font=('verdana',14))
btn5=Button(root,text='5',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(5))
btn5.grid(row=2,column=1,sticky='w')
btn5.config(font=('verdana',14))
btn6=Button(root,text='6',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(6))
btn6.grid(row=2,column=2,sticky='w')
btn6.config(font=('verdana',14))
btn3=Button(root,text='3',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(3))
btn3.grid(row=3,column=0,sticky='w')
btn3.config(font=('verdana',14))
btn2=Button(root,text='2',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(2))
btn2.grid(row=3,column=1,sticky='w')
btn2.config(font=('verdana',14))
btn1=Button(root,text='1',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(1))
btn1.grid(row=3,column=2,sticky='w')
btn1.config(font=('verdana',14))
btn0=Button(root,text='0',bg='#838B8B',fg="black",width='5',height='2',command=lambda: get_digit(0))
btn0.grid(row=4,column=0,sticky='w')
btn0.config(font=('verdana',14))
#OPERATORS....
#................
btns=Button(root,text='+',bg='#838B8B',fg="black",width='5',height='2',command=lambda :get_oprtr("+"))
btns.grid(row=1,column=3,sticky='w')
btns.config(font=('verdana',14))
btnd=Button(root,text='-',bg='#838B8B',fg="black",width='5',height='2',command=lambda :get_oprtr("-"))
btnd.grid(row=2,column=3,sticky='w')
btnd.config(font=('verdana',14))
btnm=Button(root,text='*',bg='#838B8B',fg="black",width='5',height='2',command=lambda :get_oprtr("*"))
btnm.grid(row=3,column=3,sticky='w')
btnm.config(font=('verdana',14))
btnf=Button(root,text='/',bg='#838B8B',fg="black",width='5',height='2',command=lambda :get_oprtr("/"))
btnf.grid(row=4,column=3,sticky='w')
btnf.config(font=('verdana',14))
#anonomys....
#................
btneq=Button(root,text='=',bg='#838B8B',fg="black",width='5',height='2',command=lambda :result())
btneq.grid(row=4,column=1,sticky='w')
btneq.config(font=('verdana',14))
btnclr=Button(root,text='CLR',bg='#838B8B',fg="black",width='5',height='2',command=lambda: clr())
btnclr.grid(row=4,column=2,sticky='w')
btnclr.config(font=('verdana',14))
root.mainloop()