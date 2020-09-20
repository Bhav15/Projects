import string, random
import pymysql
import datetime
from datetime import datetime
import requests, json

class Hospital:
    
    def Register(self):
        file = open("C://Users//ADMIN//Bhav.txt", mode ="w")
        Username = input ("Enter your username: ")
        Password = "".join(random.choice(string.ascii_uppercase + string.digits)for i in range(6))
        print ("Your One time password is: ", Password)

        file.write(str(Username))
        file.write(':')
        file.write(str(Password))
        file.close()

    def Login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        file = open("C://Users//ADMIN//Bhav.txt")
        login = file.readline()
        Username, Password = login.split(':')
        if (Username == username) and (Password == password):
            print("Login Successfull")
            Hospital.Appointment(dict)
        else:
            print("Username and password is incorrect")

    def Appointment(self):
        idx=int(input("Enter the index no of the hospital you want to choose: "))
        if idx<= len(lst):
            print(lst[idx])
        con = pymysql.connect(host="localhost", user="root",password="", database="appointmentdb")
        
        print("Fill the form below:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        add = input("Address: ")
        Contact = int(input("Contact No: "))
        print("Select a category from list below")
        Hospital.Category(dict)
        catr = input("Category: ")
        Doctor = input("Doctor name: ")
        Date = input("Date: ")
        print("Select Time")
        Hospital.Time(time)
        Time=input("Time: ")
        if Date and Time not in dict:
            Status = "Appointment Confirmed"
            print(Status)
        else:
            print("Select another time:")
        
        cur = con.cursor()
        insert_query ="""insert into patient_details
            (Name,Age,Gender,Address,Contact,Category,Doctor,Date,Time,Status)
            values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(name,age,gender,add,Contact,catr,Doctor,Date,Time,Status)
        cur.execute(insert_query)
        con.commit()

    def Hospital_find(self):
        api_key = 'AIzaSyDGeiDKK4tR5MK39KFf3YDLgEzKt60ce08'
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        query = input('Search query: ')
        r = requests.get(url + 'query=' + query +'&key=' + api_key)
        x = r.json()
        y = x['results']
        for i in range(len(y)):
            c=y[i]['name']
            print(i, y[i]['name'])
            lst.append(c)

    def Category(self):
        category.extend(['General Physician', 'Pediatrician', 'Gynecologist', 'Surgeon','Psychiatrist',
             'Cardiologist','Dermatologist','Opthalmologist','Neurologist','Radiologist','Oncologist'])
        for i in range(len(category)):
                print("{}. {}".format(i+1, category[i]))
    
        return

    def Time(self):
        time.extend(['9:00-9:30','9:30-10:00','10:00-10:30','10:30-11:00','11:00-11:30','11:30-12:00','1:30-2:00','2:00-2:30','2:30-3:00','3:00-3:30','3:30-4:00'])
        for i in range(len(time)):
            print(time[i])
        
        return
        

        

if __name__ == '__main__':
    dict ={}
    lst=[]
    category=[]
    time=[]
    
while True:
    print("""Make a choice:
1. Register
2. Find hospitals near you
3. Book Appointment
4. Logout""")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        Hospital.Register(dict)
        
    elif ch==2:
        Hospital.Hospital_find(dict)
        
    elif ch==3:
        print("Login to continue")
        Hospital.Login(dict)
        
    elif ch==4:
        break
    else:
        print("Something went wrong! Please try again")
        
        
        
