def Binsearch(arr,KEY):
    low = 0
    high = len(arr)-1
    m = 0
    while(low<=high):
        m =(low+high)//2	
        if(KEY<arr[m]):
            high = m-1
        elif(KEY>arr[m]):
            low = m+1
        else:
             return m
	 
    return -1


def FibSearch(arr, key,n):    
    
    b = 0 
    a = 1 
    f = b + a 
  
    while (f < n): 
        b = a 
        a = f 
        f = b + a 
      
    offset = -1; 
  
    while (f > 1): 
          
        i = min(offset+b, n-1) 
  
        if (arr[i] < key): 
            f = a 
            a = b
            b = f - a
            offset = i 
  
        elif (arr[i] > key): 
            f = b 
            a = a - b 
            b = f - a
  
        else : 
            return i 
  

    if(a and arr[offset+1] == key): 
        return offset+1; 
  
    return -1

print("\nHow many Students are there?")
n = int(input())
array = []
i=0
for i in range(n):
    print("\n Enter roll number: ")
    item = int(input())
    array.append(item)

print("The Roll Numbers of Students are ...\n")
print(array)


while(True):
    print("Main Menu")
    print("\n 1. Binary Search")
    print("\n 2. Fibonacci Search")
    print("\n 3. Exit")
    print("\n Enter your choice: ")
    choice = int(input())
    if(choice == 1):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Binsearch(array,key)
        if(location !=-1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    elif(choice == 2):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = FibSearch(array,key,n)
        if(location !=-1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    else:
        print("Exitting");
        break

