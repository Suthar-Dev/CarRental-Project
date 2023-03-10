################################### AMITH'S PART ################################
#CAR RENTAL
#CREATE/INSERT BY AMITH
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="car_rental")
if con.is_connected():
 print('Connection Successful..')
cur=con.cursor()
def create_table():#TO CREATE TABLE(CARS,CUSTOMER)
 query="create table if not exists cars(car_ptno varchar(30) primary key,\
type varchar(30),company varchar(20),model varchar(20),\
rent decimal(10,2),insurance decimal(10,2),status varchar(15))"
 cur.execute(query)
 query="create table if not exists customer(passport_no varchar(30) primary key,\
license_no varchar(30),name varchar(30),phone_no int(15),address varchar(30),\
car_ptno varchar(30),drop_date date,drop_time varchar(10),\
drop_place varchar(20),foreign key(car_ptno) references cars(car_ptno))"
 cur.execute(query)
create_table()
def insert_values():#(TO ADD VALUES INTO TABLE)
 while True:
 print()
 clr.write('\t >>Insert<<\n',"KEYWORD")
 clr.write("\t A.Car Details \n\t B.Customer Details \n\t C.Exit \n","SYNC")
 opt=input('\t Enter Option: ')
 if opt.upper()=='A':#TO ADD CAR DETAILS
 print()
 clr.write('\t >>Insert Car Details<<\n',"KEYWORD")
 cp=input("\t Enter Plate Number: ")
 c_ptno = cp.upper()
 typ=input("\t Enter Type: ")
 ty = typ.title()
 com=input("\t Enter Company: ")
 comp = com.title()
 model=input("\t Enter Model: ")
 mod = model.title()
 rent=float(input("\t Enter Rent: "))
 ins=float(input("\t Enter Insurance: "))
 query="insert into cars values('"+c_ptno+"','"+ty+"',\
'"+comp+"','"+mod+"','"+str(rent)+"','"+str(ins)+"',NULL)"
 cur.execute(query)
 con.commit()
 print()
 clr.write('\t Done!\n',"STRING")
 print()
 return c_ptno,0
 elif opt.upper()=='B':#TO ADD CUSTOMER DETAILS
 print()
 clr.write('\t >>Insert Customer Details<<\n',"KEYWORD")
 pno=input('\t Enter Passport Number: ')
 pass_no = pno.upper()
 lno=input('\t Enter License Number: ')
 li_no = lno.upper()
 n=input('\t Enter Name: ')
 name = n.title()
 ph_no=int(input('\t Enter Phone Number: '))
 add=input('\t Enter Address: ')
 ad = add.title()
 cpt=input('\t Enter Car Plate Number: ')
 c_ptno = cpt.upper()
 q = "select status from cars where car_ptno = '"+c_ptno+"'"
 cur.execute(q)
 data = cur.fetchone()
 if data[0] == 'Not Available' or data[0] == 'Crashed':
 return c_ptno,2
 drop_date=input('\t Enter Drop Date In The Format yyyy-mm-dd: ')
 drop_time=input('\t Enter Drop Time In The Format HrHr:MinMin: ')
 d_p=input('\t Enter Drop Place: ')
 drop_place = d_p.title()
 query="insert into customer values('{}','{}','{}',{},\
 '{}','{}','{}','{}','{}')".format(pass_no,li_no,name,ph_no,ad,\
 c_ptno,drop_date,drop_time,drop_place)
 cur.execute(query)
 con.commit()
 print()
 clr.write('\t Done!\n',"STRING")
 print()
 return c_ptno,1
 elif opt.upper()=='C':
 return -1,-1
 else:
 print()
 clr.write('\t //Invalid Option// \n',"COMMENT")
#create_table()
################################# RUDHRA'S PART ################################
#car rental
#search
#Rudhra
 #for customers
def Search_CarType(a):
 query="select type,company,model,rent from cars where type = '"+str(a)+"' and \
status = 'Available'"
 cur.execute(query)
 data = cur.fetchall()
 return data
def Search_Company(a):
 query="select type,company,model,rent from cars where company = '"+str(a)+"' and \
status = 'Available'"
 cur.execute(query)
 data = cur.fetchall()
 return data
def Search_Model(a):
 q="select type,company,model,rent from cars where model = '"+str(a)+"' and \
status = 'Available'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_Rent(a,b):
 q="select type,company,model,rent from cars where rent between '"+a+"' and '"+b+"' and \
status = 'Available'"
 cur.execute(q)
 data = cur.fetchall()
 return data
 #for staff
def Search_CarTypeStaff(a):
 query="select * from cars where type = '"+str(a)+"'"
 cur.execute(query)
 data = cur.fetchall()
 return data
def Search_CompanyStaff(a):
 query="select * from cars where company = '"+str(a)+"'"
 cur.execute(query)
 data = cur.fetchall()
 return data
def Search_ModelStaff(a):
 q="select * from cars where model = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_RentStaff(a,b):
 q="select * from cars where rent between '"+a+"' and '"+b+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_Status(a):
 q = "select * from cars where status = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_Insurance(a,b):
 q="select * from cars where insurance between '"+a+"' and '"+b+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_PassportNo(a):
 q="select * from customer where passport_no = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_LicenseNo(a):
 q="select * from customer where license_no = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_Name(a):
 q="select * from customer where name like '%"+str(a)+"%'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_PhoneNo(a):
 q="select * from customer where phone_no like '%"+a+"%'"
 cur.execute(q)
Page | 15
 data = cur.fetchall()
 return data
def Search_Address(a):
 q="select * from customer where address like '%"+str(a)+"%'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_PtNo(a,b): #b 1 for car b 2 for customer
 if b == 1:
 q="select * from cars where car_ptno = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
 elif b == 2:
 q="select * from customer where car_ptno = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_DropDate(a):
 q="select * from customer where drop_date = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_DropTime(a):
 q="select * from customer where drop_time = '"+str(a)+"'"
 cur.execute(q)
 data = cur.fetchall()
 return data
def Search_DropPlace(a):
 q="select * from customer where drop_place like '%"+str(a)+"%'"
 cur.execute(q)
 data = cur.fetchall()
 return data
################################## KARAN'S PART #################################
Page | 16
#Karan's Code
#updating car details
def Update_Rent(car_no,newrent):
 query="update cars set rent='"+str(newrent)+"' where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
def Update_Insurance(car_no,newins):
 query="update cars set insurance='"+str(newins)+"' where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
def Update_Status(car_no,newStatus):
 query = "update cars set status = '"+str(newStatus)+"' where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
#updating customer details
def Update_Address(p_no,newAdd):
 query="update customer set address='"+newAdd+"' where passport_no='"+str(p_no)+"'"
 cur.execute(query)
 con.commit()
def Update_Phone(p_no,newPhone):
 query="update customer set phone_no='"+str(newPhone)+"' where passport_no='"+str(p_no)+"'"
 cur.execute(query)
 con.commit()
def Update_Date(car_no,newDate):
 query="update customer set drop_date='"+newDate+"' where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
Page | 17
def Update_Time(car_no,newTime):
 query="update customer set drop_time='"+newTime+"' where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
def Update_Place(car_no,newPlace):
 query="update customer set drop_place='"+newPlace+"' where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
def Update_Carpt(p_no,car_no):
 query="update customer set car_ptno='"+car_no+"' where passport_no='"+p_no+"'"
 cur.execute(query)
 con.commit()
#delete customer when the car is returned
def Delete_Customer(p_no):
 query="delete from customer where passport_no='"+str(p_no)+"'"
 cur.execute(query)
 con.commit()
#delete car when the car is crashed and insurance is paid
def Delete_Car(car_no):
 query="delete from cars where car_ptno='"+str(car_no)+"'"
 cur.execute(query)
 con.commit()
################################## Extra functions ##################################
def customer_check(p_no):
 query="select * from customer where passport_no = '"+str(p_no)+"'"
 cur.execute(query)
 p = 0
 try:
 while True:
Page | 18
 dat=cur.fetchone()
 if dat[0]==p_no:
 p=1
 except :
 pass
 return p
def car_check(car_ptno):
 query="select * from cars where car_ptno = '"+str(car_ptno)+"'"
 cur.execute(query)
 p=0
 try:
 while True:
 dat=cur.fetchone()
 if dat[0]==car_ptno:
 p=1
 except :
 pass
 return p
def car_check_customer(car_ptno):
 query="select * from customer where car_ptno = '"+str(car_ptno)+"'"
 cur.execute(query)
 p=0
 try:
 while True:
 dat=cur.fetchone()
 if dat[5]==car_ptno:
 p=1
 except :
 pass
 return p

Page | 19
def display_all_cars():
 query="select * from cars"
 cur.execute(query)
 data = cur.fetchall()
 return data
def display_all_customers():
 query="select * from customer"
 cur.execute(query)
 data = cur.fetchall()
 return data
#################################### DEV'S PART #################################
# Display by Dev Suthar
import random
from tabulate import tabulate
import sys
try:
 clr=sys.stdout.shell
except AttributeError:
 raise RuntimeError("USE IDLE")
l = ['Heya!' , 'Howdy!' , 'Hola!' , 'Hello!' , 'Bonjour!' , 'Ola!' , 'Namaste!' , 'Guten tag!',\
 'Nin hao!' , 'Konnichiwa!' , 'Merhaba!','Hallo!']
i = random.randrange(len(l)) # Gives random greeting everytime
clr.write(" \n","DEFINITION")
clr.write(" \n","ERROR")
print(' '*45,l[i].upper() ,'WELCOME TO METALLICA CAR RENTAL')
clr.write(" \n","ERROR")
clr.write(" \n","DEFINITION")
print()
while True:
 print()
 clr.write("Please Select Your Role: \n1.Customer \n2.Staff Member \n3.Exit \n","KEYWORD")
 print()
 a = int(input('Enter Option : '))
Page | 20
 print()
 if a == 1:
 print('-'*121)
 print()
 while True:
 clr.write(" >>>CUSTOMER<<< \n","STRING")
 print()
 clr.write("\t1.Search A Car \n\t2.Update Your Details \n\t3.Exit \n","SYNC")
 b = int(input('\tEnter Option: ')) #Menu
 if b == 1:
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t>>Search Car Via<<\n","KEYWORD")
 clr.write("\t 1.Car Type \n\t 2.Company \n\t \
3.Model \n\t 4.Rent \n\t 5.Exit \n","SYNC")
 c = int(input('\t Enter Option: '))
 if c == 1:
 print()
 print('-'*121)
 print()
 while True:
 pno=1
 clr.write("\t >>CAR TYPES<< \n","KEYWORD")
 clr.write("\t \
(1)Small: 2 Seater \n\t (2)Medium: 4 Seater \n\t (3)Large: 5 Seater \n\t (4)Xlarge: 7 Seater\
\n\t (5)Cruiser: 7 Seater for OffRoad \n\t (6)Exit \n","SYNC") # Shows different types of car types
we have
 Q = input('\t Enter Preferred Car Type: ')
 if Q.isdigit() and Q!='6':
 print()
 clr.write('\t **Please Enter Car Type**\n',"BUILTIN")
 print()
 continue
Page | 21
 q = Q.title() # To capitalize first letter of each word
 d = Search_CarType(q)
 if Q=='6' or Q.capitalize()=='Exit':
 pno=0
 print()
 print('-'*121)
 print()
 break
 if len(d)==0:
 pno=0
 print()
 clr.write("\t **The Type Of Car Is Currently Unavailable** \n","BUILTIN")
 print()
 else:
 print()
 print(tabulate(d,headers = ['Car Type','Car Company','Car Model',\
 'Car Rent'],tablefmt = 'fancy_grid')) #To print in tabular form
 break
 elif c == 2:
 print()
 print('-'*121)
 print()
 while True:
 pno=1
 clr.write("\t >>Car Companies<<\n","KEYWORD")
 clr.write("\
\t (1)Toyota \n\t (2)Nissan \n\t (3)Hyundai \n\t (4)Honda \n\t (5)Chevrolet \
\n\t (6)Skoda \n\t (7)Kia \n\t (8)Exit \n","SYNC") # Shows the car companies we have
 Q = input('\t Enter Preferred Car Company: ')
 if Q.isdigit() and Q!='8':
 print()
 clr.write('\t **Please Enter Car Company**\n',"BUILTIN")
 print()
 continue
Page | 22
 q = Q.title()
 d =Search_Company(q)
 if Q=='8' or Q.capitalize()=='Exit':
 pno=0
 print()
 print('-'*121)
 print()
 break
 if len(d)==0:
 pno=0
 print()
 clr.write("\t **The Type Of Car Is Currently Unavailable** \n","BUILTIN")
 print()
 else:
 print()
 print(tabulate(d,headers = ['Car Type','Car Company','Car Model',\
 'Car Rent'],tablefmt = 'fancy_grid'))
 break
 elif c == 3:
 print()
 print('-'*121)
 print()
 while True:
 pno=1
 clr.write("\t >>Car Models<< \n","KEYWORD")
 clr.write("\
\t (1)Micro \n\t (2)Sedan \n\t (3)Cuv \n\t (4)Suv \n\t (5)Minivan \n\t (6)Exit \n","SYNC")
#Shows car models we have
 Q = input('\t Enter Preferred Car Model: ')
 if Q.isdigit() and Q!='6':
 print()
 clr.write('\t **Please Enter Car Model** \n',"BUILTIN")
 print()
 continue
 q = Q.title()
Page | 23
 d = Search_Model(q)
 if Q=='6' or Q.capitalize()=='Exit':
 pno=0
 print()
 print('-'*121)
 print()
 break
 if len(d)==0:
 pno=0
 print()
 clr.write("\t **The Type Of Car Is Currently Unavailable** \n","BUILTIN")
 print()
 else:
 print()
 print(tabulate(d,headers = ['Car Type','Car Company','Car Model',\
 'Car Rent'],tablefmt = 'fancy_grid'))
 break
 elif c == 4:
 print()
 print('-'*121)
 print()
 while True:
 pno=1
 clr.write("\t >>Rent Range<< \n","KEYWORD")
 print()
 p = input('\t Minimum Rent: ')
 q = input('\t Maximum Rent: ')
 d = Search_Rent(p,q)
 if len(d)==0:
 pno=0
 print()
 clr.write("\t **The Type Of Car Is Currently Unavailable** \n","BUILTIN")
 print()
 else:
Page | 24
 print()
 print(tabulate(d,headers = ['Car Type','Car Company','Car Model',\
 'Car Rent'],tablefmt = 'fancy_grid'))
 print()
 while True:
 s=1
 Q=int(input('\t 1.Enter Again \n\t 2.Exit \n\t Enter Option: '))
 if Q==1:
 print()
 break
 elif Q==2:
 print()
 s=0
 break
 else:
 print()
 clr.write("\t //Invalid Option// \n","COMMENT")
 print()
 if s==0:
 break


 elif c == 5:
 print()
 print('-'*121)
 print()
 break
 else:
 print()
 clr.write("\t //Invalid Option// \n","COMMENT")
 print()
 continue
 if pno!=0:
 print()
Page | 25
 clr.write("**Once You Have Finalized The Car You Want To Rent, Please Reach Out
To Our \
Staff For Further Process** \n","STRING")
 print()
 print("-"*121)
 print()


 elif b == 2:
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t>>Update<< \n","KEYWORD")
 clr.write("\t 1.Phone Number \n\t 2.Address \
\n\t 3.Car Drop Details \n\t 4.Exit \n","SYNC")
 c = int(input('\t Enter Option: '))
 if c == 1:
 print()
 clr.write("\t >>Update Phone Number<< \n","KEYWORD")
 pn = input('\t Enter Your Passport Number: ')
 p_no = pn.upper() # To change every letter of the input to upper case
 p = customer_check(p_no)
 if p == 1:
 nP = input('\t Enter New Phone Number: ')
 Update_Phone(p_no,nP)
 print()
 clr.write("\t Done! Phone Number Updated Successfully.. \n","STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write("\t **Customer With This Passport Number Does Not Exist**
\n","BUILTIN")
Page | 26
 print()
 print('-'*121)
 print()
 elif c == 2:
 print()
 clr.write("\t >>Update Address<< \n","KEYWORD")
 pn = input('\t Enter Passport Number: ')
 p_no = pn.upper()
 p = customer_check(p_no)
 if p == 1:
 nA = input('\t Enter New Address: ')
 newAdd = nA.title()
 Update_Address(p_no,newAdd)
 print()
 clr.write("\t Done! Address Updated Successfully.. \n","STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write("\t **Customer With This Passport Number Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif c == 3:
 while True:
 print()
 clr.write("\t >>Update Car Drop Details<<\n","KEYWORD")
 clr.write("\t 1.Drop Time \n\
\t 2.Drop Place \n\t 3.Drop Date \n\t 4.Exit \n","SYNC")
 d = int(input('\t Enter Option: '))
 if d == 1:
 print()
 clr.write("\t >>Update Drop Time<< \n","KEYWORD")
Page | 27
 cn = input('\t Enter Car License Plate: ')
 car_no = cn.upper() #To capitalize every letter of input
 p = car_check_customer(car_no)
 if p == 1:
 newTime = input('\t Enter New Time In The Format HrHr:MinMin: ')
 Update_Time(car_no,newTime)
 print()
 clr.write("\t Done! Car Drop Time Updated Successfully... \n","SRING")
 print()
 print('-'*121)
 print()
 break

 else:
 print()
 clr.write("\t **Car With This License Plate Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif d == 2:
 print()
 clr.write("\t >>Update Drop Place<< \n","KEYWORD")
 cn = input('\t Enter Car License Plate: ')
 car_no = cn.upper()
 p = car_check_customer(car_no)
 if p == 1:
 nP = input('\t Enter New Drop Place: ')
 newPlace = nP.title()
 Update_Place(car_no,newPlace)
 print()
 clr.write("\t Done! Car Drop Place Updated Successfully... \n","STRING")
 print()
 print('-'*121)
 print()
Page | 28
 break

 else:
 print()
 clr.write("\t **Car With This License Plate Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif d == 3:
 print()
 clr.write("\t >>Update Drop Date<< \n","KEYWORD")
 cn = input('\t Enter Car License Plate: ')
 car_no = cn.upper()
 p = car_check_customer(car_no)
 if p == 1:
 newDate = input('\t Enter New Drop Date In The Format yyyy-mm-dd: ')
 Update_Date(car_no,newDate)
 print()
 clr.write("\t Done! Car Drop Date Updated Successfully... \n","STRING")
 print()
 print('-'*121)
 print()
 break
 else:
 print()
 clr.write("\t **Car With This License Plate Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif d == 4:
 print()
 print('-'*121)
 print()
 break
Page | 29
 else:
 print()
 clr.write('\t //Invalid Option// \n',"COMMENT")
 elif c == 4:
 print()
 print('-'*121)
 print()
 break
 else:
 print()
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif b == 3:
 print()
 clr.write("\t--Thank You!-- \n","DEFINITION")
 print()
 print('-'*121)
 print()
 break
 else:
 print()
 clr.write('\t//Invalid Option// \n',"COMMENT")
 print()
 elif a == 2:
 print('-'*121)
 clr.write('Enter Password:','COMMENT')
 b = input(' ') #Password is - BestCarRental
 if b == 'BestCarRental':
 print('-'*121)
 print()
 while True:
 print()
 clr.write(' >>>Staff<<<\n',"STRING")
 print()
Page | 30
 clr.write("\t1.Insert New Car/Customer Details \n\t2.Search \
Details \n\t3.Update/Delete \n\t4.Display All \n\t5.Exit \n","SYNC") #Menu for staff
 c = int(input('\tEnter Option: '))
 if c == 1:
 print()
 print('-'*121)
 print()
 while True:
 clr.write(" \t>>Insert<< \n","KEYWORD")
 clr.write("\t 1.Add New Car/Customer \n\t 2.Exit \n","SYNC")
 op = int(input('\t Enter Option: '))
 if op == 1:
 car_no,R=insert_values()
 if R==0:
 status='Available'
 Update_Status(car_no,status)
 elif R==1:
 status='Not Available'
 Update_Status(car_no,status)
 elif R==2:
 print()
 clr.write('\t **The Car Is Not Available For Rent**\n',"BUILTIN")
 print()
 else:
 print()
 elif op == 2:
 print()
 print('-'*121)
 print()
 break
 else:
 print()
 clr.write('\t //Invalid Option// \n'," COMMENT")
 print()
Page | 31

 elif c == 2:
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t>>Search<< \n","KEYWORD")
 clr.write("\t 1.Customer Details \n\t 2.Car Details \n\t 3.Exit \n","SYNC")
 d = int(input('\t Enter Option: '))
 print()
 if d == 1: #Customer details
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t >>Search Customer Via<<\n","KEYWORD")
 clr.write("\t 1.Passport Number \n\t 2.License Number\
\n\t 3.Name \n\t 4.Phone Number \n\t 5.Address \n\t 6.Car Plate Number \
\n\t 7.Car Drop Details \n\t 8.Exit \n","SYNC")
 e = int(input('\t Enter Option: '))
 print()
 if e == 1:
 clr.write('\t >>Search Via Passport Number<<\n',"KEYWORD")
 pn = input('\t Enter Passport Number: ')
 p_no = pn.upper()
 f = Search_PassportNo(p_no)
 if len(f) == 0:
 print()
 clr.write("\t **Customer With This Passport Number Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
Page | 32
 print(tabulate(f,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
'Address','CarPtNo' ,\
'DropDate','DropTime',\
'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 2:
 clr.write('\t >>Search Via License Number<<\n',"KEYWORD")
 ln = input('\t Enter License Number: ')
 l_no = ln.upper()
 f = Search_LicenseNo(l_no)
 if len(f) == 0:
 print()
 clr.write("\t **Customer With This License Number Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
 'Address','CarPtNo' ,\
'DropDate','DropTime',\
'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 3:
 clr.write('\t >>Search Via Name<<\n',"KEYWORD")
 N = input('\t Enter Name: ')
 n = N.title()
 f = Search_Name(n)
Page | 33
 if len(f) == 0:
 print()
 clr.write("\t **Customer With This Name Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
'Address','CarPtNo' ,\
'DropDate','DropTime',\
'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 4:
 clr.write('\t >>Search Via Phone Number<<\n',"KEYWORD")
 p = input('\t Enter Phone Number: ')
 f = Search_PhoneNo(p)
 if len(f) == 0:
 print()
 clr.write("\t **Customer With This Phone Number Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
 'Address','CarPtNo' ,\
'DropDate','DropTime',\
 'DropPlace'],tablefmt = 'fancy_grid'))
 print()
Page | 34
 print('-'*121)
 print()
 elif e == 5:
 clr.write('\t >>Search Via Address<<\n',"KEYWORD")
 ad = input('\t Enter Address: ')
 add = ad.title()
 f = Search_Address(add)
 if len(f) == 0:
 print()
 clr.write("\t **Customer With This Address Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
'Address','CarPtNo' ,\
'DropDate','DropTime',\
'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 6:
 clr.write('\t >>Search Via Car Plate Number<<\n',"KEYWORD")
 cn = input('\t Enter Car Plate Number: ')
 c_no = cn.upper()
 cus = 2
 f = Search_PtNo(c_no,cus)
 if len(f) == 0:
 print()
 clr.write("\t **Customer With This Car Plate Number Does Not Exist**
\n","BUILTIN")
 print()
Page | 35
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
'Address','CarPtNo' ,\
 'DropDate','DropTime',\
 'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 7:
 while True:
 clr.write("\t >>Search Car Drop Details Via<< \n","KEYWORD")
 clr.write("\t 1.Drop Place \n\t 2.Drop Date \
\n\t 3.Drop Time \n\t 4.Exit \n","SYNC")
 f = int(input('\t Enter Option: '))
 print()
 if f == 1:
 clr.write('\t >>Search Via Drop Place<<\n',"KEYWORD")
 pl = input('\t Enter Drop Place: ')
 pla = pl.title()
 g = Search_DropPlace(pla)
 if len(g) == 0:
 print()
 clr.write("\t **Customer With This Drop Place Does Not Exist**
\n","BUILTIN")
 print()
 else:
 print()
 print(tabulate(g,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
 'Address','CarPtNo' ,\
 'DropDate','DropTime',
 'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 break
 elif f == 2:
 clr.write('\t >>Search Via Drop Date<<\n',"KEYWORD")
 da = input('\t Enter Drop Date In Format yyyy-mm-dd: ')
 g =Search_DropDate(da)
 if len(g) == 0:
 print()
 clr.write("\t **Customer With This Drop Date Does Not Exist**
\n","BUILTIN")
 print()
 else:
 print()
 print(tabulate(g,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
'Address','CarPtNo' ,\
 'DropDate','DropTime',\
 'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 break
 elif f == 3:
 clr.write('\t >>Search Via Drop Time<<\n',"KEYWORD")
 a = input('\t Enter Drop Time In Format HrHr:MinMin: ')
 g = Search_DropTime(a)
 if len(g) == 0:
 print()
 clr.write("\t **Customer With This Drop Time Does Not Exist**
\n","BUILTIN")
 print()
 else:
Page | 37
 print()
 print(tabulate(g,headers = ['Pass_No','License',\
 'Name','PhoneNo',\
'Address','CarPtNo' ,\
 'DropDate','DropTime',\
 'DropPlace'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 break
 elif f == 4:
 print()
 print('-'*121)
 print()
 break
 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif e == 8:
 print()
 print('-'*121)
 print()
 break
 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif d == 2: #Car details
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t >>Search Car Via<< \n","KEYWORD")
 clr.write("\t 1.Plate Number \n\t 2.Type \n\t 3.Company \
\n\t 4.Model \n\t 5.Rent \n\t 6.Insurance \n\t 7.Status \n\t 8.Exit \n","SYNC")
Page | 38
 e = int(input('\t Enter Option: '))
 print()
 if e == 1:
 clr.write('\t >>Search Via Plate Number<<\n',"KEYWORD")
 cn = input('\t Enter Car Plate Number: ')
 c_no = cn.upper()
 staff = 1
 f = Search_PtNo(c_no,staff)
 if len(f) == 0:
 print()
 clr.write("\t **Car With This Plate Number Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 2:
 clr.write('\t >>Search Via Type<<\n',"KEYWORD")
 Q = input('\t Enter Car Type: ')
 q = Q.title()
 f = Search_CarTypeStaff(q)
 if len(f)==0:
 print()
 clr.write("\t **Car Of This Type Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
Page | 39
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 3:
 clr.write('\t >>Search Via Company<<\n',"KEYWORD")
 Q = input('\t Enter Car Company: ')
 q = Q.title()
 f = Search_CompanyStaff(q)
 if len(f)==0:
 print()
 clr.write("\t **Car Of This Company Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 4:
 clr.write('\t >>Search Via Model<<\n',"KEYWORD")
 m = input('\t Enter Car Model: ')
 M = m.title()
 f = Search_ModelStaff(M)
 if len(f)==0:
 print()
 clr.write("\t **Car Of This Model Does Not Exist** \n","BUILTIN")
Page | 40
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 5:
 clr.write('\t >>Search Via Rent<<\n',"KEYWORD")
 p = input('\t Enter Minimum Rent: ')
 q = input('\t Enter Maximum Rent: ')
 f = Search_RentStaff(p,q)
 if len(f)==0:
 print()
 clr.write("\t **Car Within This Rent Range Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 6:
 clr.write('\t >>Search Via Insurance<<\n',"KEYWORD")
 mi = input('\t Enter Minimum Insurance: ')
 Mi = input('\t Enter Maximum Insurance: ')
Page | 41
 f = Search_Insurance(mi,Mi)
 if len(f)==0:
 print()
 clr.write("\t **Car Within This Insurance Range Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
 elif e == 7:
 clr.write('\t >>Search Via Status<<\n',"KEYWORD")
 s = input('\t Enter Status: ')
 S = s.title()
 f = Search_Status(S)
 if len(f)==0:
 print()
 clr.write("\t **Car With This Status Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 print(tabulate(f,headers = ['Car PtNo','Type','Company','Model',\
 'Rent','Insurance','Status'],\
 tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
Page | 42
 elif e == 8:
 print()
 print('-'*121)
 print()
 break
 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif d == 3:
 print()
 print('-'*121)
 print()
 break
 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif c == 3:
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t>>Update/Delete<<\n","KEYWORD")
 clr.write("\t 1.Car Details \n\t 2.Customer Details \n\t 3.Exit \n","SYNC")
#Update/Delete menu
 d = int(input('\t Enter Option: '))
 print()
 if d == 1:
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t >>Update/Delete Car Details<< \n","KEYWORD")
 clr.write("\t 1.Update Rent \n\t 2.Update Insurance \n\t 3.Update Status \
\n\t 4.Delete Car \n\t 5.Exit \n","SYNC")
 e = int(input('\t Enter Option: '))
Page | 43
 print()
 if e == 1:
 clr.write('\t >>Update Rent<<\n',"KEYWORD")
 cn = input('\t Enter Car Plate Number: ')
 car_ptno = cn.upper()
 p = car_check(car_ptno)
 if p == 1:
 newrent = input('\t Enter New Rent: ')
 Update_Rent(car_ptno,newrent)
 print()
 clr.write("\t Done! Car Rent Updated Successfully.. \n","STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write("\t **Car With This Plate Number Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif e == 2:
 clr.write('\t >>Update Insurance<<\n',"KEYWORD")
 cn = input('\t Enter Car Plate Number: ')
 car_ptno = cn.upper()
 p = car_check(car_ptno)
 if p == 1:
 newins = input('\t Enter New Insurance: ')
 Update_Insurance(car_ptno,newins)
 print()
 clr.write("\t Done! Car Insurance Updated Successfully.. \n","STRING")
 print()
 print('-'*121)
 print()
 else:
Page | 44
 print()
 clr.write("\t **Car With This Plate Number Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif e == 3:
 clr.write('\t >>Update Status<<\n',"KEYWORD")
 cn = input('\t Enter Car Plate Number: ')
 car_ptno = cn.upper()
 p = car_check(car_ptno)
 if p == 1:
 ns = input('\t Enter New Status: ')
 newStatus = ns.title()
 Update_Status(car_ptno,newStatus)
 print()
 clr.write("\t Done! Car Status Updated Successfully \n","STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write("\t **Car With This Plate Number Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif e == 4:
 clr.write('\t >>Delete Car<<\n',"KEYWORD")
 cn = input('\t Enter Car Plate Number: ')
 car_ptno = cn.upper()
 p = car_check(car_ptno)
 if p == 1:
 try:
 clr.write("\n\t Please Make Sure Insurance Is Paid If The Car Is
Crashed \n","SYNC")
 print('\n\t 1.Proceed \n\t 2.Exit')
Page | 45
 f = int(input('\t Enter option: '))
 if f == 1:
 Delete_Car(car_ptno)
 print()
 clr.write("\t Car Details Deleted Successfully.. \n","STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write('\t --Thank You!--\n',"DEFINITION")
 print()
 except:
 clr.write('\n\t **Please Make Sure The Customer Using This \
Car Is Deleted First\n\n',"BUILTIN")
 else:
 print()
 clr.write("\t **Car With This Plate Number Does Not Exist** \n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif e == 5:
 print()
 print('-'*121)
 print()
 break
 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif d == 2:
 print()
 print('-'*121)
 print()
 while True:
Page | 46
 clr.write('\t >>Update/Delete Customer Details<<\n',"KEYWORD")
 clr.write('\t 1.Update Car For Customer \n\t 2.Delete Customer \n\t 3.Exit
\n',"SYNC")
 op = int(input('\t Enter Option: '))
 print()
 if op == 1:
 clr.write('\t >>Update Car For Customer<<\n',"KEYWORD")
 pn = input('\t Enter Passport ID: ')
 p_no = pn.upper()
 p = customer_check(p_no)
 if p == 1:
 car_no = input('\t Enter New Car Plate Number: ')
 query="select status from cars where car_ptno = '"+car_no+"'"
 cur.execute(query)
 check_s=1
 try:
 while True:
 dat=cur.fetchone()
 if dat[0]=='Not Available':
 check_s=0
 except:
 pass
 if check_s==1:
 query="select car_ptno from customer where passport_no =
'"+str(p_no)+"'"
 cur.execute(query)
 try:
 while True:
 dat=cur.fetchone()
 Update_Status(dat[0],'Available')
 except :
 pass
 Update_Carpt(p_no,car_no)
 Update_Status(car_no,'Not Available')
 print()
 clr.write('\t Customer Details Updated Successfully..\n',"STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write('\t The Car Is Not Available For Rent\n',"BUILTIN")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write("\t **Customer With This Passport Number Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif op == 2:
 clr.write('\t >>Delete Car<<\n',"KEYWORD")
 pn = input('\t Enter Passport ID: ')
 p_no = pn.upper()
 p = customer_check(p_no)
 if p == 1:
 clr.write('\n\t Please Make Sure The Billings Have Been Done\n',"SYNC")
 print('\n\t 1.Proceed \n\t 2.Exit')
 e = int(input('\t Enter Option: '))
 if e == 1:
 query="select car_ptno from customer where passport_no =
'"+str(p_no)+"'"
 cur.execute(query)
 try:
 while True:
 dat=cur.fetchone()
 Update_Status(dat[0],'Available')
Page | 48
 except :
 pass
 Delete_Customer(p_no)
 print()
 clr.write('\t Customer Details Deleted Successfully..\n',"STRING")
 print()
 print('-'*121)
 print()
 else:
 print()
 clr.write("\t --Thank You!-- \n","DEFINITION")
 print()
 else:
 print()
 clr.write("\t **Customer With This Passport Number Does Not Exist**
\n","BUILTIN")
 print()
 print('-'*121)
 print()
 elif op == 3:
 print()
 print('-'*121)
 print()
 break
 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
 print()
 elif d == 3:
 print()
 print('-'*121)
 print()
 break

 else:
 clr.write('\t //Invalid Option// \n',"COMMENT")
Page | 49
 print()
 elif c == 4:
 print()
 print('-'*121)
 print()
 while True:
 clr.write("\t>>Display All<< \n","KEYWORD")
 clr.write("\t 1.Customer Details \n\t 2.Car Details \n\t 3.Exit \n","SYNC")
 op = int(input('\t Enter Option: '))
 print()
 if op == 1:
 print('-'*121)
 print()
 clr.write('>>Customer Details<<\n',"KEYWORD")
 print()
 d = display_all_customers()
 print(tabulate(d,headers = ['Passport No.','License No.','Name','Phone No.',\
 'Address','Car Plate No.','Drop Date','Drop Time',\
 'Drop Place'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()

 elif op == 2:
 print('-'*121)
 print()
 clr.write('>>Cars Details<<\n',"KEYWORD")
 print()
 d = display_all_cars()
 print(tabulate(d,headers = ['Car Plate No.','Car Type','Car Company','Car Model',\
 'Car Rent','Car Insurance','Car Status'],tablefmt = 'fancy_grid'))
 print()
 print('-'*121)
 print()
Page | 50
 elif op == 3:
 print()
 print('-'*121)
 print()
 break

 else:
 clr.write("\t //Invalid Option// \n","COMMENT")
 print()
 elif c == 5:
 print()
 clr.write('\t--Thank You!--\n',"DEFINITION")
 print('-'*121)
 print()
 break
 else:
 print()
 clr.write("\t//Invalid Option// \n","COMMENT")
 else:
 print('-'*121)
 clr.write("Incorrect Password \n","COMMENT")
 print('-'*121)
 print()
 elif a==3:
 print()
 clr.write("******************************************THANK YOU FOR CHOOSIING METALLICA
CAR RENTAL********\
**************************** \n","DEFINITION")
 print()
 break
 else :
 print()
 clr.write("//Invalid Option// \n","COMMENT")
 print()
