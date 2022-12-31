##hospital management software




#importing Libraries
import tkinter as tk
import tkinter.scrolledtext as st


#Creating Functions



def arrtable(k,v):#TO ARRANGE TABLE
    str1=''
    for i in range(len(k)):
        print(v[i],':',k[i],'\n')
    print('____________________________________')
    return str1

    
    
def scrtxt(tittle,content):#To open scrollable text widgit
    win = tk.Tk()
    win.title("Hospital Management System")

    
    #Tittle Label
    tk.Label(win, 
             text = tittle, 
             font = ("Times New Roman", 18), 
             background = 'Blue', 
             foreground = "white").grid(column = 0,
                                        row = 0)
    
    #Text Space

    text_area = st.ScrolledText(win,
                                width = 50, 
                                height = 25, 
                                font = ("Times New Roman",
                                        15))

    text_area.grid(column = 0,
                   pady = 10,
                   padx = 30)
    text_area.insert(tk.INSERT,content)
    
    text_area.configure(state ='disabled')
    #Button
    tk.Button(win,
          command=win.destroy,
          text='C L O S E',
          background='red',
          foreground='white',
          activebackground='blue',
          height=2,
          width=8).grid(column=0,
                        pady=10,padx=30)
    win.mainloop()






#Main
while(True):
    print('WELCOME TO APPOLO-13 HOSPITALS PVT. LTD.')
    import mysql.connector
    password=str(input("ENTER THE DATABASE PASSWORD: "))
    
    mysql=mysql.connector.connect(host="localhost",user="root",passwd=password)
    mycursor=mysql.cursor()
    mycursor.execute("create database if not exists appolo_hospitals")
    mycursor.execute("use appolo_hospitals")

    
#Table Creation
    mycursor.execute("create table if not exists patient_details(puid int(10) primary key,name varchar(30) ,age int(3),sex char(1),address varchar(50),contact int(15))")
    mycursor.execute("create table if not exists doctor_details(duid int(10) primary key,name varchar(30) ,specialisation varchar(40),age int(2),address varchar(30),contact varchar(15),fees decimal(10,2),monthly_salary decimal(10,2))")
    mycursor.execute("create table if not exists nurse_details(nuid int(10) primary key,name varchar(30),age int(2),address varchar(30),contact varchar(15),monthly_salary decimal(10,2))")
    mycursor.execute("create table if not exists other_workers_details(ouid int(10)primary key,name varchar(30),age int(2),address varchar(30),contact varchar(15),monthly_salary decimal(10,2))")
    mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) )")


    while(True):
        print("1. SIGN IN (LOGIN) \n 2. SIGN UP (REGISTER))")
    
        r=int(input("Enter your choice:"))



        if r==2:
            print("###PLEASE REGISTER YOURSELF###")
            u=input("Enter your username :")
            p=input(" Set your password :")
            
            mycursor.execute("insert into user_data values('{}','{}')".format(u,p))
            mysql.commit()
    
    
            print("\n\nREGISTERED SUCCESSFULLY!!!\n\n")
            x=input("Enter any key to continue:")


        elif r==1:
                print("  {{SIGN IN }}  ")
                un=input("ENTER THE USERNAME:")
                ps=input("ENTER THE PASSWORD:")
                
                mycursor.execute("select password from user_data where username='{}'".format(un))
                row=mycursor.fetchall()


                for i in row:
                    a=list(i)


                    if a[0]==ps:
                        while(True):
                            ##Task dashboard
                            print("""
                                     1.STAFF DETAILS
                                     2.PATIENT DETAILS
                                     3.LOG OUT
                                     4.ABOUT US
                                     """)
                            #Choice from dashboard
                            a=int(input("ENTER YOUR CHOICE:"))


                            if a==1:
                                #DASH_1(STAFF DETAILS)
                                print("""
                                                                          1. SHOW DETAILS
                                                                          2. ADD NEW MEMBER
                                                                          3. DELETE EXISTING MEMBER
                                                                          4. EXIT
                                                                          """)
                                b=int(input("ENTER YOUR CHOICE:"))
                                #DASH_1.1(SHOW DETAILS)
                                if b==1:
                                    print("""
                                                                                1. DOCTOR DETAILS
                                                                                2. NURSE DETAILS
                                                                                3. OTHER WORKERS
                                                                                """)
                                
                                    c=int(input("ENTER YOUR CHOICE:"))
                                    #DASH_1.1.1(DOCTOR DETAILS)
                                    if c==1:
                                        mycursor.execute("select * from doctor_details")
                                        row=mycursor.fetchall()
                                        for i in row:
                                            b=0
                                            v=list(i)#TO CONVERT row(tuple) to row(list)
                                            k=["DUID","NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","FEES","MONTHLY_SALARY"]
                                            str1=arrtable(v,k)
            
                                            
                                    #DASH_1.1.2(Nurse details)
                                    elif c==2:
                                        mycursor.execute("select * from nurse_details")
                                        row=mycursor.fetchall()
                                        for i in row:
                                            v=list(i)
                                            k=["NUID","NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                            arrtable(v,k)

                                            
                                    #DASH_1.1.3(Other Workers)
                                    elif c==3:
                                        mycursor.execute("select * from other_workers_details")
                                        row=mycursor.fetchall()
                                        for i in row:
                                            v=list(i)
                                            k=["OUID","NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                            arrtable(v,k)

                                            
                                #DASH_1.2
                                elif b==2:
                                    print("""
                                                                             1. ADD NEW DOCTOR
                                                                             2. ADD NEW NURSE
                                                                             3. ADD NEW WORKER
                                                                                    """)
                                    c=int(input("ENTER YOUR CHOICE:"))
                                    
                                    if c==1:
                                      #DASH_1.2.1(ADD NEW DOCTOR)
                                      duid=int(input('ENTER DUID :'))
                                      name=input("Enter Dr. Name:")
                                      spe=input("Enter Specialisation:")
                                      age=input("ENTER AGE:")
                                      add=input("ENTER ADDRESS:")
                                      cont=input("ENTER CONTACT NO.:")
                                      fees=input("ENTER FEES:")
                                      ms=input("ENTER MONTHLY_SALARY:")
                                      #INSERTING VALUES ENTERED INTO THE DOCTORS_TABLE
                                      mycursor.execute("insert into doctor_details values({},'{}','{}',{},'{}','{}',{},{})".format(duid,name,spe,age,add,cont,fees,ms))
                                      mysql.commit()
                                      print("SUCCESSFULLY ADDED DATA OF Dr.",name)

                                    
                                    elif c==2:
                                      #DASH_1.2.2
                                      nuid=int(input('ENTER NUID :'))
                                      name=input("ENTER NURSE NAME:")
                                      age=input("ENTER AGE:")
                                      add=input("ENTER ADDRESS:")
                                      cont=input("ENTER CONTACT NO.:")
                                      ms=int(input("ENTER MONTHLY_SALARY:"))
                                      #INSERTING VALUES ENTERED TO THE TABLE
                                      mycursor.execute("insert into nurse_details values({},'{}',{},'{}','{}',{})".format(nuid,name,age,add,cont,ms))
                                      mysql.commit()
                                      print("SUCCESSFULLY ADDED DATA OF nurse",name)

                                   
                                    elif c==3:
                                      #DASH_1.2.3(Enter Worker Details)
                                      duid=int(input('ENTER  OUID :'))
                                      name=input("ENTER WORKER NAME:")
                                      age=input("ENTER AGE:")
                                      add=input("ENTER ADDRESS:")
                                      cont=input("ENTER CONTACT NO.:")
                                      ms=input("ENTER MONTHLY_SALARY:")
                                      #INSERTING VALUES ENTERED TO THE TABLE
                                      mycursor.execute("insert into other_workers_details values({},'{}',{},'{}','{}',{})".format(ouid,name,age,add,cont,ms))
                                      mysql.commit()
                                      print("SUCCESSFULLY ADDED")

                                
                                elif b==3:
                                    #DASH_1.3
                                   print("1. DELETE DOCTOR DETAILS\n2. DELETE NURSE DETAILS\n3. DELETE OTHER WORKERS")
                                   c=int(input("ENTER YOUR CHOICE:"))

                                   
                                   if c==1:
                                       #DASH_1.3.1_deleting nurse details
                                       duid=input("ENTER DOCTOR'S DUID:")
                                       mycursor.execute("select * from doctor_details where duid={}".format(duid))
                                       row=mycursor.fetchall()
                                       print(row)
                                       p=input("Are you sure to delete this data? (y/n):")
                                       if p=="y":
                                           mycursor.execute("delete from doctor_details where duid={}".format(duid))
                                           mysql.commit()
                                           print("SUCCESSFULLY DELETED!!")
                                       else:
                                           print("RECORD NOT DELETED")
                                       

                                      
                                   #DASH_1.3.2(deleting nurse details)
                                   elif c==2:
                                       nuid=input("ENTER NURSE'S NUID:")
                                       mycursor.execute("select * nurse_details where nuid={}".format(nuid))
                                       row=mycursor.fetchall()
                                       print(row)
                                       p=input("Are you sure to delete this data? (y/n):")
                                       if p=="y":
                                           mycursor.execute("delete from nurse_details where nuid={}".format(nuid))
                                           mysql.commit()
                                           print("SUCCESSFULLY DELETED!!")
                                       else:
                                           print("RECORD NOT DELETED")

                                           
                                   #DASH_1.3.2(deleting other_workers details)
                                   elif c==3:
                                       ouid=input("ENTER THE WORKER'S OUID :")
                                       mycursor.execute("select * from workers_details where ouid=={}".format(ouid))                                       
                                       row=mycursor.fetchall()
                                       print(row)
                                       p=input("Are you sure to delete this data? (y/n):")
                                       if p=="y":
                                           mycursor.execute("delete from other_workers_details where ouid={}".format(ouid))
                                           mysql.commit()
                                           print("SUCCESSFULLY DELETED!!")
                                       else:
                                           print("RECORD NOT DELETED")

                                           
                                elif b==4:
                                    break
                               
                            #DASH_2(PATIENT DETAILS)
                            elif a==2:
                                
                                print("""
                                                                          1. SHOW  PATIENT DETAILS
                                                                          2. ADD  NEW PATIENT
                                                                          3. DISCHARGE PATIENT
                                                                          4. EXIT
                                                                          """)
                                
                                b=int(input("ENTER YOUR CHOICE:"))
                                #showing existing details

                            
                                if b==1:
                                    #DASH_2.1(SHOW PATIENT DETAILS)
                                    mycursor.execute("select * from patient_details")
                                    row=mycursor.fetchall()
                                    for i in row:
                                        b=0
                                        v=list(i)
                                        k=["PUID","NAME","AGE","SEX","ADDRESS","CONTACT"]
                                        arrtable(k,v)
                                    
                                
                                elif b==2:
                                    #DASH_2.2(ADD PATIENT DETAILS)
                                    puid=int(input('Assign PUID to PATIENT :'))
                                    name=input("ENTER NAME: ")
                                    sex=input("ENTER SEX(M/F) : ")
                                    age=int(input("ENTER AGE: "))
                                    add=input("ADDRESS: ")
                                    cont=input("CONTACT NUMBER: ")
                                    mycursor.execute("insert into patient_details values({},'{}',{},'{}','{}',{})".format(puid,name,age,sex,add,cont))
                                    mysql.commit()
                                    mycursor.execute("select * from patient_details")
                                    for i in mycursor:
                                        v=list(i)
                                        k=['PUID','NAME','SEX','AGE','ADDRESS','CONTACT']
                                        arrtable(k,v)
                                        print("REGISTERED SUCCESSFULLY")

                                
                                elif b==3:
                                    #DASH_2.3(DISCHARGE PATIENT)
                                    puid=input("ENTER THE PUID:")
                                    mycursor.execute("select * from patient_details where puid={}".format(puid))
                                    row=mycursor.fetchall()
                                    print(row)
                                    bill=input("HAS HE PAID ALL THE BILLS ? (y/n):")
                                    if bill=="y":
                                        mycursor.execute("delete from patient_details where puid={}".format(puid))
                                        mysql.commit()

                                        
                                #if user wants to exit
                                elif b==4:
                                    break

                                
                            ###$$@@SIGN OUT@@$$###
                            elif a==3:
                                print('SIGNED OUT')
                                print('____________________________________________\n\n')
                                
                                break

                            
                            elif a==4:
                                #About us
                                file1=open('AboutUs.txt','r')
                                content=file1.read()
                                cntnt=content
                                scrtxt('ABOUT US',cntnt)

                                
    else:
        print('Username and password not valid')
        break
                        
        
    
    






     








































            
  
        


    
    
 



