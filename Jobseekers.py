#JOB SEEKERS PROJECT

#I only used  two files txt job.txt and jobseekers.txt

def replace(file_path, linex, lineupdated):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if (line==linex):
                    new_file.write(line.replace(line,lineupdated))
                else:
                    new_file.write(line)    
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)    


def Convertstol(string): 
    li = list(string.split("|")) 
    return li  


def Convertltos(list):
    str=''
    for i in range(7):  
        if (i!=6):
            str += list[i]+'|'  
        else:
            str += list[i]    
    return str    


def unique(code):
    f=open("job.txt",'r')
    line = f.readline()
    if line=='':
        return 1
    while line:
        linelist=Convertstol(line)
        if linelist[0]==code:
            return 0      
        line = f.readline()
    return 1    
    f.close()  


def add():

    print("Add new job offer: \n")
    f=open("job.txt","w")
    list=[]
    code=(input("add new code for this Job : "))
    #unique code function search
    while (unique(code)==0):   
        code=(input("this code already exists,add another code for this job"))
    list.append(code)
    f.write(list[0] + "|")
    print("Company information : \n ")
    list.append(input("Name : "))
    f.write(list[1]+"|")
    list.append(input("Address  : "))
    f.write(list[2] + "|")
    list.append(input("Phone number  : "))
    f.write(list[3] + "|")
    list.append(input("Email  : "))
    f.write(list[4] + "|")
    list.append(input("Requested profile description: Degree , qualification, experience"))
    f.write(list[5] +"|")
    list.append(input("Mission description "))
    f.write(list[6] +"\n")


def deleteLine():
    code = input("CODE for the job to be modified  : ")
    fname = 'job.txt'
    f = open(fname)
    output = []
    for line in f:
        if not code in line:
            output.append(line)
    f.close()
    f = open(fname, 'w')
    f.writelines(output)
    f.close()

def list_jobseekrs():
    choix=int(input("do you want to 1-list all the job seekers 2-list the job seekers that applied to a certain job "))
    g = open("jobseeker.txt", "r")
    if (choix==1):
        print("This the list of job seekers that applied for job offers  \n")
        for s in g:
            print(s)    
    else:    
        code=input("write down the code of the job")
        line = g.readline()
        while line:
            linelist=Convertstol(line)
            if linelist[6]==code+'\n':
                print(line)     
            line = g.readline()
    g.close()

def search ():    #for the search you can type anything for ex : tunis server .. etc doesnt matter and it will display all the jobs that have what ur searching ( space between them)
    s=0
    print(" search a job offer by: job offer ID, domain (computer science, business…) or location :")
    ch=input("saisir les donnes à chercher ")
    ch1=ch.split()  #list
    f=open("job.txt","r")
    for ligne in f :
        s=0
        values=ligne.split("|") #first ligne in list seperated by |

        for i   in  range (len(ch1)):  #see if the element of  the search request are in the first line
            if ligne.count(ch1[i])==1:
                s=s+1
        if len(ch1)==s :
            print(ligne)
    f.close()

from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove,getcwd,sep

def updatea ():
    code1=input("write down the job's code that you want to update:")
    f=open("job.txt",'r')
    line = f.readline()
    while line:
        linelist=Convertstol(line)
        if linelist[0]==code1:
            break      
        line = f.readline()
    f.close()    
    print("line to update: \n")
    print(line)
    modif="yes"     
    while modif=="yes":
        print("what do you wish to update? \n 1-code \n 2-name \n 3-address \n 4-phone number \n 5-email \n 6-Requested profile description \n 7-Mission description ")
        choix=int(input())
        if(choix==1):
            c=input("write down the new code")
            linelist[0]=c             
        elif(choix==2):
            c=input("write down the new name")   
            linelist[1]=c
        elif(choix==3):
            c=input("write down the new address")
            linelist[2]=c 
        elif(choix==4):
            c=input("write down the new phone number")
            linelist[3]=c
        elif(choix==5):
            c=input("write down the new email")
            linelist[4]=c
        elif(choix==6):
            c=input("write down the Requested profile description")
            linelist[5]=c
        elif(choix==7):
            c=input("write down the mission description")
            linelist[6]=c+'\n'    
        modif=input("do you wish to update something else ?")
    updatedline=Convertltos(linelist)
    path = getcwd()
    newPath = path.replace(sep, '/')
    newPath1 = newPath.replace('C:','')+"/job.txt"
    replace(newPath1,line,updatedline)
    f.close()
            
def add_jobseeker():
    list=[]
    print("Personal information and Professional information.:")
    g=open( "jobseeker.txt","a")
    list.append(input(" ID card : "))
    g.write(list[0] +"|")
    list.append(input("Name : "))
    g.write(list[1]+ "|")
    list.append(input("Adress  : "))
    g.write(list[2] + "|")
    list.append(input("phonenumber  : "))
    g.write(list[3]+ "|")
    list.append(input("Education : "))
    g.write(list[4]+ "|")
    list.append(input("experience and skills "))
    g.write(list[5] + "|")
    f=open("job.txt",'r')
    line=f.readline()
    while line:
        print(line)
        line=f.readline()
    f.close()
    list.append(input("write down the job's code that you want to apply to"))
    g.write(list[6]+"\n")
    g.close()

def updatej ():
    ID1=input("write down your ID Card")
    f=open("jobseeker.txt",'r')
    line = f.readline()
    while line:
        linelist=Convertstol(line)
        if linelist[0]==ID1:
            break      
        line = f.readline()
    f.close()    
    print("line to update: \n")
    print(line)
    modif="yes"     
    while modif=="yes":
        print("what do you wish to update? \n 1-ID card \n 2-name \n 3-address \n 4-phone number \n 5-education \n 6-experience and skills ")
        choix=int(input())
        if(choix==1):
            c=input("write down the new ID card")
            linelist[0]=c             
        elif(choix==2):
            c=input("write down the new name")   
            linelist[1]=c
        elif(choix==3):
            c=input("write down the new address")
            linelist[2]=c 
        elif(choix==4):
            c=input("write down the new phone number")
            linelist[3]=c
        elif(choix==5):
            c=input("write down the new education Degree")
            linelist[4]=c
        elif(choix==6):
            c=input("write down the new experience or skills")
            linelist[5]=c  
        modif=input("do you wish to update something else ?")
    updatedline=Convertltos(linelist)
    path = getcwd()
    newPath = path.replace(sep, '/')
    newPath1 = newPath.replace('C:','')+"/jobseeker.txt"    #this can find its own path
    replace(newPath1,line,updatedline)
    f.close()



#now this is the interface area


from tkinter import *
import tkinter.messagebox as box
window = Tk()  
def dialog1():      
        if (user.get() == 'admin' and  passw.get() == 'admin'):
            box.showinfo('info','Correct Login')    
        elif(user.get() =='user'and passw.get() == 'user'):
            box.showinfo('info','Correct login')
        else:
            box.showinfo('info','Invalid  login')
            window.destroy()  
            exit() 
        window.destroy()
       
window.title('hire now')

frame = Frame(window)
user=StringVar()
Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)
entry1 = Entry(window,textvariable=user)
entry1.pack(padx=15, pady=5)

Label2 = Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)

passw= StringVar()
entry2 = Entry(window,textvariable=passw,show="*")
entry2.pack(padx = 15,pady=7)


btn = Button(frame, text = 'Check Login',command = dialog1)
btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()
ch="yes"
while ch=="yes":
    if user.get()=='admin':
        options=input(" choose : \n 1- add a job offer \n 2- update a job  \n 3 - delete a job \n 4- display lists of jobseekers  \n")
        if options=='1':
            add()
        elif options=="2":
            updatea()
        elif options=="3":

             deleteLine()
        else:
             list_jobseekrs()
    if user.get()=='user':
         options1 = input(" choose : \n 1- Search a job offer \n 2- Brows and Apply for a job offer \n 3 - Update job seeker information\n  ")
         if options1=='1' :
            search()
         elif options1=='2':
            add_jobseeker()
         else:
            updatej()       
    ch=input("would you like to repeat the process or  a new one : yes or no ")
