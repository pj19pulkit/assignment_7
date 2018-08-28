#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop. 

dict={}
for i in range (1,6):
    key=i
    value=(input("Enter Value :- "))
    dict[key]=value
x=(input("Enter Value whose Key is to be found :- "))
for key , value in dict.items():
    if value==x:
        print("The Key of the Value %s is %s" %(value , key))    

#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject.

dict_stu ={}
dict_marks={}
for i in range (0,3):
    key=input('Enter The Name of the Student :- ')
    value= dict_marks= { input('Enter Subject 1 :- ') : int(input('Enter Marks ')) , input('Enter Subject 2 :- ') : int(input('Enter Marks ')) , input('Enter Subject 3 :- ') : int(input('Enter Marks ')) }
    dict_stu[key]=value
n=input("Enter the Name the student whose marks is to be displayed :- ")
if n in dict_stu:
    print(dict_stu[n])
    
