from tkinter import *
root=Tk()
root.title('Totra Security Systems')
   
########## SEARCH ##########
    
def search():
    global e11;
    global l1;
    global f12;
    global root1
    
    root1=Tk();
    root1.title('Search')

    ###
    f11=Frame(root1);
    f11.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);
    
    l11=Label(f11,text='Enter ID:')
    l11.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
    
    e11=Entry(f11);
    e11.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5);
    
    b11=Button(f11,text='Enter',bg='GOLD',command=try1)
    b11.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)
    
    ###
    f12=Frame(root1);
    f12.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);
    
    b11=Button(f12,text='Clear',bg='red',command=clear1)
    b11.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

    b12=Button(f12,text='Close',bg='red',command=root1.destroy)
    b12.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

def try1():
    global l12
    s1=int(e11.get());

    root11=Tk()

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import time
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('x.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("log").sheet1
    x = sheet.get_all_records()
    t=time.localtime()
    a=t[2]
    b=t[1]
    c=t[0]
    d=[]
    for i in range(len(x)):
        y=x[i]['Date'].split('.')
        if int(y[0])==a and int(y[1])==b and int(y[2])==c and x[i]['ID']==s1:
            d.append(x[i]['Time'])
    d.reverse()
    if len(d)!=0:
        root11.title('Timings')
        
        f111=Frame(root11);
        f111.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);
        
        b111=Label(f111,text='Timings')
        b111.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

        Lb111=Listbox(root11)
        for ii in range(len(d)):
            Lb111.insert(ii,d[ii])
        Lb111.pack()
    else:
        root11.title('ERROR!')
        l111=Label(root11,bg='white',text='Possible Cause of Error : 1. This Person Hasnt Entered yet. 2. Not A Valid ID. 3. No Entries Today.')
        l111.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

def clear1():
    e11.delete(0,END)        

########## LAST ENTRY ##########
    
def last_entry():
    global root2
    root2=Tk();
    root2.title('Last Entry')

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('x.json', scope)
    client = gspread.authorize(creds)
    sheet1 = client.open("log").sheet1
    x = sheet1.get_all_records()

    aa=x[0]['Time']
    bb=x[0]['ID']
    cc=x[0]['Date']

    sheet2 = client.open("profile").sheet1
    y = sheet2.get_all_records()

    d=[]
    for i in range(len(y)):
        if y[i]['ID']==bb:
            d.append(y[i]['Name'])
            
    ###
    f21=Frame(root2);
    f21.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l21=Label(f21,text='Last Entry',bg='light blue')
    l21.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)
    
    ###
    f22=Frame(root2);
    f22.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l22=Label(f22,text='Name :',bg='light green')
    l22.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l23=Label(f22,text=d[0])
    l23.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f23=Frame(root2);
    f23.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l24=Label(f23,text='ID :',bg='light green')
    l24.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l25=Label(f23,text=bb)
    l25.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f24=Frame(root2);
    f24.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l26=Label(f24,text='Date :',bg='light green')
    l26.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l27=Label(f24,text=cc)
    l27.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f25=Frame(root2);
    f25.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l28=Label(f25,text='Time :',bg='light green')
    l28.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

    l29=Label(f25,text=aa)
    l29.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

    ###
    f26=Frame(root2);
    f26.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    b21=Button(f26,text='Close',bg='red',command=root2.destroy)
    b21.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

########## PROFILE ##########
    
def profile():
    global root3
    global e31
    global l32
    global l34
    global l36
    global l38
    global l40
    global l42
    global l44

    root3=Tk();
    root3.title('Profile')

    ###
    f31=Frame(root3);
    f31.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);
    
    l31=Label(f31,text='Enter ID:')
    l31.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
    
    e31=Entry(f31);
    e31.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5);
    
    b31=Button(f31,text='Enter',bg='GOLD',command=try3)
    b31.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

    ###
    f32=Frame(root3);
    f32.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l32=Label(f32,text='Profile',bg='LIGHT BLUE')
    l32.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f33=Frame(root3);
    f33.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l33=Label(f33,text='ID :',bg='LIGHT Green')
    l33.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l34=Label(f33)
    l34.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f34=Frame(root3);
    f34.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l35=Label(f34,text='Name :',bg='LIGHT Green')
    l35.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l36=Label(f34)
    l36.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f35=Frame(root3);
    f35.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l37=Label(f35,text='Age :',bg='light Green')
    l37.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l38=Label(f35)
    l38.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f36=Frame(root3);
    f36.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l39=Label(f36,text='DoB :',bg='light Green')
    l39.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l40=Label(f36)
    l40.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f37=Frame(root3);
    f37.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);

    l41=Label(f37,text='Height :',bg='light Green')
    l41.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    l42=Label(f37)
    l42.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

    ###
    f38=Frame(root3);
    f38.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES);
    
    b32=Button(f38,text='Clear',bg='red',command=clear3)
    b32.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

    b33=Button(f38,text='Close',bg='red',command=root3.destroy)
    b33.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)
    
def try3():
    s31=int(e31.get());
    
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('x.json', scope)
    client = gspread.authorize(creds)

    sheet2 = client.open("profile").sheet1
    y = sheet2.get_all_records()

    d=[]
    try:
        for i in range(len(y)):
            if y[i]['ID']==s31:
                d.append(y[i])
            
        l34.config(text=d[0]['ID'])
        l36.config(text=d[0]['Name'])
        l38.config(text=d[0]['Age'])
        l40.config(text=d[0]['DoB'])
        l42.config(text=d[0]['Height'])
    except:
        root32=Tk()
        root32.title('ERROR!')
        l321=Label(root32,text='THIS ID DOES NOT EXIST')
        l321.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

def clear3():
    e31.delete(0,END)
    l34.config(text="")
    l36.config(text="")
    l38.config(text="")
    l40.config(text="")
    l42.config(text="")

########## HISTORY ##########
    
def history():
    global root4
    import time
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    root4=Tk();
    root4.title('History')

    ###
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('x.json', scope)
    client = gspread.authorize(creds)

    sheet2 = client.open("log").sheet1
    x = sheet2.get_all_records()

    sheet1 = client.open("profile").sheet1
    z = sheet1.get_all_records()

    t=time.localtime()
    a=t[2]
    b=t[1]
    c=t[0]

    d=[]

    for i in range(len(x)):
        str1={}
        y=x[i]['Date'].split('.')
        if int(y[0])==a and int(y[1])==b and int(y[2])==c:
            for j in range(len(z)):
                if x[i]['ID']==z[j]['ID']:
                    str1={"Name":z[j]['Name'],"Date":x[i]['Date'],"Time":x[i]['Time']}
                    d.append(str1)
                    del(str1)
    if len(d)!=0:
        d.reverse()
        height = int(len(d)+1)
        width = 3
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = Label(root4, text="")
                b.grid(row=i, column=j)

        Label(root4,text='Serial No.',bg='light blue').grid(row=0,column=0)
        Label(root4,text='Name',bg='light blue').grid(row=0,column=1)
        Label(root4,text='Time',bg='light blue').grid(row=0,column=2)

        for ii in range(1,len(d)+1):
            Label(root4,text=ii).grid(row=ii,column=0)
            Label(root4,text=d[ii-1]['Name']).grid(row=ii,column=1)
            Label(root4,text=d[ii-1]['Time']).grid(row=ii,column=2)

    else:
        root4.title('ERROR!')
        l42=Label(root4,text='NO ENTRIES TODAY')
        l42.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

########## MAIN WINDOW ##########
    
f1=Frame(root)
f1.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

l1=Label(f1,text='TOTRA SECURITY SYSTEMS',font=50,fg='black')
l1.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)


###
f2=Frame(root)
f2.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

l2=Label(f2)
l2.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

b1=Button(f2,text='Search',bg='LIGHT blue',width=15,padx=5,pady=5,command=search)
b1.pack(side=LEFT)

l4=Label(f2)
l4.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

###
f3=Frame(root)
f3.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

l5=Label(f3)
l5.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

b2=Button(f3,text='Last Entry',bg='LIGHT blue',width=15,padx=5,pady=5,command=last_entry)
b2.pack(side=LEFT)

l6=Label(f3)
l6.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

###
f4=Frame(root)
f4.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

l7=Label(f4)
l7.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

b3=Button(f4,text='Profile',bg='LIGHT green',width=15,padx=5,pady=5,command=profile)
b3.pack(side=LEFT)

l8=Label(f4)
l8.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

###
f5=Frame(root)
f5.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

l9=Label(f5)
l9.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

b4=Button(f5,text='History',bg='LIGHT green',width=15,padx=5,pady=5,command=history)
b4.pack(side=LEFT)

l10=Label(f5)
l10.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

###
f6=Frame(root)
f6.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

b5=Button(f6,text='Close',bg='RED',command=root.destroy)
b5.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)












