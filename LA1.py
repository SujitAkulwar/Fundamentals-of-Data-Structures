print("Enter total no of students : ")
n = int(input())


arr = []
for i in range(0,n):
    ele = int(input("Marks Of Students  :  "))
    arr.append(ele)
print(arr)


print("select : \n 1. Average marks of students : \n 2. Highest score and lowest score : \n 3. Marks scored by most of the students : \n 4. list of students who were absent for the test : \n ")
a = 0 
a = int(input())
average = 0
sum = 0
highest_mark = 0
lowest_mark = 10000
highest_frequancy =0
big =0
absent_student=0



while a != -1:
    
    if a==1:
        for i in range(0,n):
            if arr[i]>0:
                sum = sum + arr[i]      
        average = sum / n
        print("average score of class is ",average)
        sum = 0 
        average = 0
        print("Enter -1 to stop code !!")
        a = int(input())


 
    if a==2:

        for i in range(0, n):
            if arr[i] > highest_mark :
                highest_mark = arr[i]

        for i in range(0, n):
            if arr[i] < lowest_mark and arr[i]!= -1:
                lowest_mark=arr[i]    
        print("highest score of class is: ",highest_mark,"\n lowest score of class is:",lowest_mark)     
        highest_mark = 0
        lowest_mark = 10000
        print("Enter -1 to stop code !!")  
        a = int(input())


    if a==3:
        c=0
        for i in range(0,n):
            for j in range(0,n):
                
                if (arr[i]==arr[j] ) and (arr[i]!=(-1)):
                    c=c+1
                    
            if c>big:
                big =c
            highest_frequancy = arr[i]
            c=0    
        print("highest frequancy marks of class is ",highest_frequancy)
        print("Enter -1 to stop code !!")  
        c=0
        highest_frequancy =0
        big = 0
        a = int(input())


    
    if a==4:
        for i in range(0, n):
            if arr[i] == -1 :
                absent_student=absent_student+1
        print("No of students absent to class test  : ",absent_student)     
        absent_student=0
        print("Enter -1 to stop code !!")  
        a = int(input())    
