import tkinter as tkn
app=tkn.Tk()
app.title('calculator')
app.geometry('600x600')


tkn.Label(app,text='A',textvariable='A',font=('',25)).place(x=0,y=0)
tkn.Label(app,text='B',textvariable='B',font=('',25)).place(x=0,y=90)
tkn.Label(app,text='RESULT',textvariable='res',font=('',25)).place(x=250,y=540)


a=tkn.Variable(app)
tkn.Entry(app,textvariable=a).place(x=50,y=15)
b=tkn.Variable(app)
tkn.Entry(app,textvariable=b).place(x=50,y=100)
res=tkn.Variable(app)
tkn.Entry(app,textvariable=res).place(x=400,y=550)


def calculator(op):
    res.set(eval(a.get()+op+b.get()))
    
    
tkn.Button(app,text='+',font=('',20),command=lambda:calculator('+'),bg='pink').place(x=0,y=150)
tkn.Button(app,text='-',font=('',20),command=lambda:calculator('-'),bg='pink').place(x=150,y=250)
tkn.Button(app,text='x',font=('',20),command=lambda:calculator('*'),bg='pink').place(x=300,y=350)
tkn.Button(app,text='/',font=('',20),command=lambda:calculator('/'),bg='pink').place(x=450,y=450)


app.mainloop()

