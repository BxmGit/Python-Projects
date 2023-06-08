#Object Orientated 
#Task - Student Registration
import random

# Libs required for csv functions
import os
import csv

#Students must enter their information including name, last name, age, contact number, email address, and create a password.
class StudentAccount:
    def __init__(self, name, lastname, age, number, email, password, studentID, balance, Module1, Module2): #Initialises and defines the class attributes in student account.
        ################# Assign the class attributes to variables to be used within the program.
        self.name = name 
        self.lastname = lastname
        self.age = age
        self.number = number
        self.email = email
        self.password = password
        self.studentID = studentID 
        self.balance = balance #The program should allocate 400 points to each registered student account automatically (students can use these points for shopping) (1 Point)
        self.Module1 = Module1
        self.Module2 = Module2

    def deposit(self, amount): 
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\n\t\t\t", amount, "has been withdrawn from your points and your current balance is: ", self.balance)
        else:
            print("\n\t\t\tThere is not enough money in your account. Your balance is: ", self.balance)
    
    def checkBalance(self):
        print("\n\t\t\tYour current balance of points is:",self.balance)
    
    def report(self):
        print("\n\t\t\tstudentID:",self.studentID,"\n\t\t\tname:",self.name,"\n\t\t\tlast name:",self.lastname,"\n\t\t\tage:",self.age,"\n\t\t\tnumber:",self.number,"\n\t\t\temail:",self.email,"\n\t\t\tbalance:",self.balance,"\n\t\t\tmodules:",self.Module1, "and", self.Module2)

    



student_dict = dict() #Initialise dictionary called student_dict.
IDlist=[]
name = None
lastname = None
number = None
email = None
password = None
studentID = None
module1 = ""
module2 = ""

print("\n\t\t\t ***Welcome to the Self Service Student Registration System!***")
if os.path.exists('students.csv'):
    with open('students.csv', 'r') as f:
        f.close()
else:
 with open('students.csv', 'x') as f:
     f.close()

    
 
with open('students.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    pastInfo=list(csv_reader)
    print(pastInfo)
    for x in pastInfo:
        fname=x[0]
        lname=x[1]
        age=x[2] 
        phoneNo=x[3]
        emailAdd=x[4]
        Password=x[5]
        studentID=x[6]
        balance=x[7]
        module1=x[8]
        module2=x[9] 
        object=StudentAccount(name=fname, lastname=lname, age=age, number=phoneNo, email=emailAdd, password=Password, studentID=studentID, balance=balance, Module1=module1, Module2=module2)
        student_dict[studentID]=object
        print("Your student ID is",studentID)
        IDlist+=[studentID]
        print(IDlist)


while (True):
 
    print("""\n\t\t\tPlease choose one of the folowing options:
                     1: Student registration
                     2: Module selecion and verification
                     3: Student account top up
                     4: Shopping
                     5: Checking balance
                     6: Edit information
                     7: Reporting 
                     q: Exit""")
           
    option = input("\n\t\t\tYour selected option: ")  

    if option.lower()=="q": #quit
        fieldnames=["Fname","Lname","Age","Number","Email","Password","StudentID","Balance","Module1","Module2"]
        rows=[]
        for x in IDlist:
            if x in student_dict.keys():
                rows+=[{"Fname":student_dict[x].name, 
                "Lname":student_dict[x].lastname, 
                "Age":student_dict[x].age, 
                "Number":student_dict[x].number, 
                "Email":student_dict[x].email, 
                "Password":student_dict[x].password, 
                "StudentID":student_dict[x].studentID, 
                "Balance":student_dict[x].balance, 
                "Module1":student_dict[x].Module1,
                "Module2":student_dict[x].Module2}]

        print(rows)
        with open('students.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

            break

#Option 1 - Student registration

    if option=="1":

        fname=input("Please enter the students first name: ")
        lname=input("Please enter the students last name: ")
        age = int(input('Please enter the students age between 1 and 100: ')) #Program will ask the user to enter the students age.  
        phoneNo = input("Please enter a UK phone number begining in 0: ")#Asks user to input the number.
        emailAdd=input("Please enter the students email address: ") #User inputs email.
        Password = input("Please Enter a password: ")
        balance=400

        while (True):
            
            studentID=random.randint(1,10000) #Produces a random integer between 1 and 10000
            if studentID not in student_dict.keys(): #Validates that the studentID is not already in use in the dictionary. 
                object=StudentAccount(name=fname, lastname=lname, age=age, number=phoneNo, email=emailAdd, password=Password, studentID=studentID, balance=balance, Module1=module1, Module2=module2)
                student_dict[studentID]=object
                print("Your student ID is",studentID)
                IDlist+=[studentID]
                print(IDlist)
                break     


#2) Module selection and verification: (8 Points)
#• The program must authenticate the student access using student ID and password. (2 Points)
#• Students should be able to choose two different modules out of the following modules (more than two modules is not possible and editing modules is not possible):
#           • Programming 1
#           • Programming 2
#           • Networking 1
#           • Networking 2 (4 Points)
#• Students should be able to view their current selected modules. (1 Points)
#• The program should allow the user to return to the main page. (1 Point)

        
    elif option == "2": 
      studentID = int(input("\n\t\t\tPlease enter your student ID: "))     #asks for the end user to input their studentid
      Password = input("\n\t\t\tEnter your password: ")   #ask for the end user to input their password  
      if studentID in student_dict.keys() and Password == student_dict[studentID].password:  #check that both studentid and password match in the dictonary
          
          if student_dict[studentID].Module1 == "" or student_dict[studentID].Module2 == "":   #This is to check whether the user has already chosen 2 modules       
            print("\n\t\t\tYou have two modules to pick out of 4: \n\t\t\t1. Programming 1\n\t\t\t2. Programming 2\n\t\t\t3. Networking 1\n\t\t\t4. Networking 2")     #this will display the module options
            Chosen_module = input("Please enter a choice by number:" )   #The user will have to choose between 1-4 and input the number in order to get their chosen corresponding module
            if Chosen_module == "1":  #if 1 is chosen then it will continue for module programming 1  
               course = 'Programming 1'
               if student_dict[studentID].Module1 == "":  #this statement will check whether the module is filled or not
                  student_dict[studentID].Module1 = course  #the module will be added if the module was empty
               elif student_dict[studentID].Module1 == course: #this statement check if the module has already been chosen
                print("\n\t\t\tYou have picked this module") #this message will display a message saying the module is already chosen       
               elif student_dict[studentID].Module2 == "":   #this statement will check if the second module is filled or not              
                student_dict[studentID].Module2 = course #if the module is not filled it will add the chosen module
               print(student_dict[studentID].Module1)
               print(student_dict[studentID].Module2)


      
            elif Chosen_module == "2":   #if 2 is chosen then it will continue for the module programming 2   
               course = 'Programming 2'  #The module is set in here to be able to check the dictonary and add the module later to the dictonary
               if student_dict[studentID].Module1 == "":  #this statement will check whether the module is filled or not
                student_dict[studentID].Module1 = course   #the module will be added if the module was empty
               elif student_dict[studentID].Module1 == course: #this statement check if the module has already been chosen
                print("\n\t\t\tYou have picked this module")  #this message will display a message saying the module is already chosen         
               elif student_dict[studentID].Module2 == "":  #this statement will check if the second module is filled or not      
                student_dict[studentID].Module2 = course  #if the module is not filled it will add the chosen module
               print(student_dict[studentID].Module1)
               print(student_dict[studentID].Module2)
 
             
      
            elif Chosen_module == "3":    #if number 3 is chosen it will continue for the module Networking 1
               course = 'Networking 1'  #the module is preset in order to check whether module has been chosen next and add it to the dictonary later       
               if student_dict[studentID].Module1 == "":   #this statement will check whether the module is filled or not
                 student_dict[studentID].Module1 = course  #the module will be added if the module was empty      
               elif student_dict[studentID].Module1 == course:  #this statement check if the module has already been chosen
                 print("\n\t\t\tYou have picked this module")    #this message will display a message saying the module is already chosen
               elif student_dict[studentID].Module2 == "":  #this statement will check if the second module is filled or not
                student_dict[studentID].Module2 = course  #if the module is not filled it will add the chosen module 
               print(student_dict[studentID].Module1)
               print(student_dict[studentID].Module2)
                     
            elif Chosen_module == "4":    #if 4 is chosen it will continue to addition of module Networking 4
               course = 'Networking 2'
               if student_dict[studentID].Module1 == "": #this statement will check whetrher the module is filled or not
                 student_dict[studentID].Module1 = course  #the module will be added if the module was empty
               elif student_dict[studentID].Module1 == course:    #this statement check if the module has already been chosen
                print("\n\t\t\tYou have picked this module")  #this message will display a message saying the module is already chosen
               elif student_dict[studentID].Module2 == "":    #this statement will check if the second module is filled or not        
                 student_dict[studentID].Module2 = course #if the module is not filled it will add the chosen module
               print(student_dict[studentID].Module1)
               print(student_dict[studentID].Module2)
          else:
            print("\n\t\t\tYou have already chosen ", student_dict[studentID].Module1 , "And",student_dict[studentID].Module2)
      else:
          print("\n\t\t\tYou have entered incorrect details!")           

#3) Student account top-up: (6 Points)
#• The program must authenticate the student access using student ID and password. (1 Point)
#• Students should be able to deposit points in his/her point account. The program should confirm the requested points with the user before adding them into his/her account. (4 Points)
#• The program must return to the main page. (1 Point)

    elif option =="3":
        studentID = int(input("\n\t\t\tPlease enter your student ID: "))
        Password =(input("\n\t\t\tPlease enter your password: "))

        if studentID in student_dict.keys() and Password==student_dict[studentID].password:
            points = float(input("\n\t\t\tPlease enter amount of points you want to deposit in your account: "))
            print ("\n\t\t\tYour student ID: ", studentID, "Amount to deposite: ", points)
            confirm = input("\n\t\t\tContinue? Y/N: ").lower()
            if confirm == "y":
         
                student_dict[studentID].deposit(points)
                print("\n\t\t\t", points, "is added to your account and your current balance: ", student_dict[studentID].balance)
            else:
                print("\n\t\t\t No money added to your account!!!")
        else:
            print("\n\t\t\tThere is no account with this account number!")

#4) Shopping (printing and food): (12 Points)
#• The program must authenticate the student access using student ID and password. (1 Point)
#• Students should be able to print and buy food from the system:
#• Each page print (single or double) costs 1.25 points (Students can print as many as pages they want as long as they have enough points)
#• Each food portion costs 7.5 points (Students can order as many as portions they like as long as they have enough points)
#• The system should print the cost of total shopping and balance after shopping. It should generate a random number for the student as a coupon. (2 Points)
#• The program should allow the user to return to the main page. 

    elif option =="4":
        studentID = int(input("\n\t\t\tPlease enter your student ID: "))
        Password =(input("\n\t\t\tPlease enter your password: "))
   

        if studentID in student_dict.keys() and Password==student_dict[studentID].password:
            paper=0
            portions=0
            print("""\n\t\t\tPlease choose one of the folowing options:
                             1: Printing
                             2: Ordering food""")
            option = input("\n\t\t\tYour selected option: ")  

            if option == "1": #printing
                print("""\n\t\t\tHow many pages (single or double) do you want to print?""")
                paper = int(input("\n\t\t\tEnter amount: "))

            elif option == "2": #Food
                print("""\n\t\t\tHow many portions of food do you want to buy?""")
                portions = int(input("\n\t\t\tEnter amount: "))

            total=float((paper*1.25)+(portions*7.5)) #total cost = amount of paper * paper price  +  amount of portions * portion price 
            student_dict[studentID].withdraw(total)

        else:
            print("\n\t\t\tThere is no account with this account number!")
    
    elif option =="5":
        studentID = int(input("\n\t\t\tPlease enter your student ID: "))
        Password =(input("\n\t\t\tPlease enter your password: "))
 

        if studentID in student_dict.keys() and Password==student_dict[studentID].password:
            student_dict[studentID].checkBalance()        
        else:
            print("\n\t\t\tThere is no account with this account number!")
    
    elif option =="6":
        studentID = int(input("\n\t\t\tPlease enter your student ID: "))
        Password =(input("\n\t\t\tPlease enter your password: "))
  
        if studentID in student_dict.keys() and Password==student_dict[studentID].password:
            print("""\n\t\t\tPlease choose one of the folowing options to edit:
                             1: Email
                             2: Contact number
                             3: Password""")
            option = input("\n\t\t\tYour selected option: ")
            if option == "1":
                student_dict[studentID].email=input("Please enter your new Email: ") #Asks the end user to input a new email and replaces the previous email with the new email
                print("\n\t\t\tThe new email is ", student_dict[studentID].email) #this will print out the new email 
            elif option == "2":  #if 2 is chosen it will allow the user to change their phone number 
                student_dict[studentID].number=input("Please enter your new Contact number: ")  #Asks the end user to input a new phone number and replaces the previous number with the new number
                print("\n\t\t\tThe new phone number is ", student_dict[studentID].number) #displays the new phone number
            elif option == "3":  #if 3 is chosen it will allow the user to edit their password  
                student_dict[studentID].password=input("Please enter your new Password: ")  #Asks for the end user to input a new password and replaces the old with the new password  
                print("\n\t\t\tYour new password is ", student_dict[studentID].password) #This displays the new password

    elif option =="7":
        studentID = int(input("\n\t\t\tPlease enter your student ID: "))
        Password =(input("\n\t\t\tPlease enter your password: "))

        if studentID in student_dict.keys() and Password==student_dict[studentID].password:
            student_dict[studentID].report()