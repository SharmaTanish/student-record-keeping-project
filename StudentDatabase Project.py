from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import os,json
from tkinter import messagebox

win = Tk()
win.geometry("1200x650+0+0")
win.title("Student Record Keeping Application")
win.configure(background="black")




# FILE LINKING and getting values and updating Treeview


def Reset():
    tan1.set("")
    tan2.set("")
    var.set("radio1")
    tan3.set("")
    tan4.set("")
    var1.set(0)
    tan5.set("")




def recall():
    stu={}
    if os.path.isfile("student.json"):
        with open("student.json") as f:
            stu=json.load(f)
        for i in treev.get_children(): # FIRST CLEAR ALL TREEVIEW
            treev.delete(i)
        for i in stu["students"]: # THEN AGAIN INSERT ALL VALUES , AS THESE NEW VALUES CONTAIN NEW ENTRY AS WELL !
            treev.insert("","end",values=(i["name"],i["rollno"],i["gender"],i["phno"],i["gpno"],i["hostal"]))


def recall2():
    course={}
    if os.path.isfile("cor.json"):
        with open("cor.json") as f:
            course=json.load(f)
        for i in treev1.get_children(): # FIRST CLEAR ALL TREEVIEW
            treev1.delete(i)
        for i in course["courses"]: # THEN AGAIN INSERT ALL VALUES , AS THESE NEW VALUES CONTAIN NEW ENTRY AS WELL !
            treev1.insert("","end",values=(i["courseid"],i["coursename"]))


def recall3():
    allocate={}
    if os.path.isfile("all.json"):
        with open("all.json") as f:
            aloocate=json.load(f)
        for i in treev2.get_children(): # FIRST CLEAR ALL TREEVIEW
            treev2.delete(i)
        for i in aloocate["allocates"]: # THEN AGAIN INSERT ALL VALUES , AS THESE NEW VALUES CONTAIN NEW ENTRY AS WELL !
            treev2.insert("","end",values=(i["studentrollno"],i["coursenames"]))




def course():
    course={}
    course["courses"]=list()
    var1=e1.get()
    var2=e2.get()
    course1={}
    course1["courseid"]=var1
    course1["coursename"]=var2
    if os.path.isfile("cor.json"):
        with open("cor.json","r") as f:
            course=json.load(f)
            course["courses"].append(course1)
           

        with open("cor.json","w") as f:

            json.dump(course,f)
    else:
        with open("cor.json","w") as f:
            course["courses"].append(course1)
            json.dump(course,f)
    messagebox.showinfo("Success","New course has been created successfully")
    recall2()

def click():
    stu={}
    stu["students"]=list()
    name = tan1.get()
    rollno=tan2.get()

    

    rollnos=[]
    if os.path.isfile("student.json"):
        with open("student.json","r") as f:
            student=json.load(f)
            stu_list=student["students"]
            for i in stu_list:
                rollnos.append(i["rollno"])



    
    gender=var.get()
    address=tan3.get()
    phno=tan4.get()
    gpno=tan5.get()
    hostal=var1.get()
    stu1={}
    stu1["name"]=name
    stu1["rollno"]=rollno
    stu1["gender"]=gender
    stu1["phno"]=phno
    stu1["gpno"]=gpno
    stu1["hostal"]=hostal



    if stu1["rollno"] not in rollnos:
        if os.path.isfile("student.json"):
            with open("student.json","r") as f:
                stu=json.load(f)
                stu["students"].append(stu1)
            

            with open("student.json","w") as f:

                json.dump(stu,f)
        else:
            with open("student.json","w") as f:
                stu["students"].append(stu1)
                json.dump(stu,f)
        messagebox.showinfo("Save","Your record has been saved")
        recall()


    else:
        messagebox.showinfo("ERROR","Your Roll No is already existing ! ")


def allocate():   # IN BOTH COURSES AND ALLOCATES WALE FUNCTION , THE FUNCTION NAME AND THE MAIN DICTIONARY NAME IS SAME !
    allocate={}
    allocate["allocates"]=list()
    var11=et1.get()
    var22=e3.get()
    allocate1={}
    allocate1["studentrollno"]=var11
    allocate1["coursenames"]=var22
    if os.path.isfile("all.json"):
        with open("all.json","r") as f:
            allocate=json.load(f)
            allocate["allocates"].append(allocate1)
           

        with open("all.json","w") as f:

            json.dump(allocate,f)
    else:
        with open("all.json","w") as f:
            allocate["allocates"].append(allocate1)
            json.dump(allocate,f)
    messagebox.showinfo("Success","Course has been allocated successfully")
    recall3()



# MAIN HEADINGS



heading = Label( win , text = "Chitkara University" , font = ("normal" , 20 , "bold"),fg="white" ,bg="black")
heading.pack()

sub_heading = Label(win , text = "STUDENT DATABASE" , font = ("normal",20,"normal"),fg="white" ,bg="black",pady=30)
sub_heading.pack()

a=PhotoImage(file="image3.png")
b=Label(image=a)
b.pack(side="right",anchor="n")

a1=PhotoImage(file="image2.png")
b1=Label(image=a1)
b1.pack(side="left",anchor="n")


tabcontrol = Notebook(win,height=400,width=700)

tab1 = Frame(tabcontrol)
tab2 = Frame(tabcontrol)
tab3 = Frame(tabcontrol)
tab4 = Frame(tabcontrol)
tab5 = Frame(tabcontrol)
tab6 = Frame(tabcontrol)


tabcontrol.add(tab1,text="New Student")
tabcontrol.add(tab2,text="Display")
tabcontrol.add(tab3,text="Course Creation")
tabcontrol.add(tab4,text="Display Courses")
tabcontrol.add(tab5,text="Course Allocation")
tabcontrol.add(tab6,text="Display Allocation")


tabcontrol.pack()

#TAB 1

name = Label(tab1,text = " Enter Your Name",padx=80,pady=10)
name.grid(row = 0 , column = 0)

rollno= Label(tab1,text = " Enter Your Rollno",padx=80,pady=10)
rollno.grid(row = 1 , column = 0)

gender= Label(tab1,text = " Choose your Gender",padx=80,pady=10)
gender.grid(row = 2 , column = 0)

address= Label(tab1,text = "Address for Correspondence",padx=80,pady=10)
address.grid(row = 3 , column = 0)

phoneno = Label(tab1,text = " Phone No.",padx=80,pady=10)
phoneno.grid(row = 4 , column = 0)

batch= Label(tab1,text = " Your Batch",padx=80,pady=10)
batch.grid(row = 5, column = 0)

hostal= Label(tab1,text = " Hostal[Y/N]",padx=80,pady=10)
hostal.grid(row = 6 , column = 0)

# FORM VALUES
tan1=StringVar()
name_value = Entry(tab1,textvariable=tan1,width = 40)
name_value.grid(row = 0 , column = 1,columnspan=2)

tan2=StringVar()
rollno_value = Entry(tab1,textvariable=tan2,width = 40)
rollno_value.grid(row = 1 , column = 1,columnspan=2)


var=StringVar()
var.set("radio")
radio1=Radiobutton(tab1,text="Male",variable=var,value = "Male")
radio1.grid(row=2,column=1)
radio2=Radiobutton(tab1,text="Female",variable=var,value = "Female")
radio2.grid(row=2,column=2)

tan3=StringVar()
address_value = Entry(tab1,textvariable=tan3,width = 40)
address_value.grid(row = 3 , column = 1,columnspan=2)

tan4=StringVar()
phoneno_value = Entry(tab1,textvariable=tan4,width = 40)
phoneno_value.grid(row = 4 , column = 1,columnspan=2)

tan5=StringVar()
combo=Combobox(tab1,state="readonly",width=37,textvariable=tan5)
combo["values"]=("G1","G2","G3","G4","G5","G6","G7","G8","G9","G10")
combo.grid(row=5,column=1,columnspan=2)

var1=IntVar()
check=Checkbutton(tab1,text="Click if you want hostal facility",variable=var1)
check.grid(row=6,column=1)


save=Button(tab1,text="Save",width=30,command=click)
save.grid(row=7,column=0,pady=50,sticky="e")

reset=Button(tab1,text="Reset",width=30,command=Reset)
reset.grid(row=7,column=1,sticky="e",columnspan=2)

# TAB 2

frame1=Frame(tab2)
frame1.pack()
treev=Treeview(frame1,selectmode="browse")
treev.pack()

treev["columns"]=("RollNo","Name","Gender","PhoneNo","Batch","Hostal")
treev["show"]="headings"
treev.column("Name",width=100)
treev.column("RollNo",width=100)
treev.column("Gender",width=100)
treev.column("PhoneNo",width=100)
treev.column("Batch",width=100)
treev.column("Hostal",width=100)

treev.heading("Name",text="Name")
treev.heading("RollNo",text="Roll No")
treev.heading("Gender",text="Gender")
treev.heading("PhoneNo",text="Phone No")
treev.heading("Batch",text="Group No")
treev.heading("Hostal",text="Hostal")

stu={}
if os.path.isfile("student.json"):
    with open("student.json") as f:
        stu=json.load(f)
    for i in stu["students"]:
        treev.insert("","end",values=(i["name"],i["rollno"],i["gender"],i["phno"],i["gpno"],i["hostal"]))



# Tab 3

l1=Label(tab3,text="Course Id",font=("normal",15,"normal"))
l1.grid(column=0,row=0,padx=150,pady=60)

e1=Entry(tab3,width=30)
e1.grid(column=1,row=0)

l2=Label(tab3,text="Course Name",font=("normal",15,"normal"))
l2.grid(column=0,row=1)

e2=Entry(tab3,width=30)
e2.grid(column=1,row=1)

b1= Button(tab3,text="Save",command=course,width=30)
b1.grid(column=0,row=3,columnspan=2,padx=150,pady=60)


# Tab 4


treev1=Treeview(tab4,selectmode="browse")
treev1.pack()

treev1["columns"]=("courseid","coursename")
treev1["show"]="headings"
treev1.column("courseid",width=200)
treev1.column("coursename",width=200)

treev1.heading("courseid",text="Course Id")
treev1.heading("coursename",text="Course Name")


course={}
if os.path.isfile("cor.json"):
    with open("cor.json") as f:
        course=json.load(f)
    for i in course["courses"]:
        treev1.insert("","end",values=(i["courseid"],i["coursename"]))



# Tab 5


lb1=Label(tab5,text="Student RollNo",font=("normal",15,"normal"))
lb1.grid(column=0,row=0,padx=150,pady=60)

et1=Entry(tab5,width=30)
et1.grid(column=1,row=0)

lb2=Label(tab5,text="Course Name",font=("normal",15,"normal"))
lb2.grid(column=0,row=1)

e3=Combobox(tab5,state="readonly",width=30)
e3["values"]=("Intro to python","Web technologies","Cyber Security","Emergining Technologies","Java Programing","Matematics","Applied Physics","Apptitude")
e3.grid(column=1,row=1)

bt1= Button(tab5,text="Allocate",command=allocate,width=30)
bt1.grid(column=0,row=3,columnspan=2,padx=150,pady=60)



# Tab 6



treev2=Treeview(tab6,selectmode="browse")
treev2.pack()

treev2["columns"]=("studentrollno","coursenames")
treev2["show"]="headings"
treev2.column("studentrollno",width=200)
treev2.column("coursenames",width=200)

treev2.heading("studentrollno",text="Student Roll No")
treev2.heading("coursenames",text="Course Name")


allocate={}
if os.path.isfile("all.json"):
    with open("all.json") as f:
        allocate=json.load(f)
    for i in allocate["allocates"]:
        treev2.insert("","end",values=(i["studentrollno"],i["coursenames"]))



# LAST HEADING

last_heading = Label(win,text = "Department of Computer Science and Engineering",width=1200 ,  font = ("normal",15,"bold"),fg="white" ,bg="black",pady=70 )
last_heading.pack(side="bottom")

win.mainloop()



