def main():    
    while True : 
       print("\t\t\t1: Accept Matrix"); 
       print("\t\t\t2: Display Matrix"); 
       print("\t\t\t3: Addition of Matrices"); 
       print("\t\t\t4: Substraction of Matrices"); 
       print("\t\t\t5: Multiplication of Matrices"); 
       print("\t\t\t6: Transpose Matrix"); 
       print("\t\t\t7: Exit"); 
       ch = int(input("Enter your choice : ")) 

       M3 = []        
       if (ch == 7):
           print ("End of Program") 
           break 
 
 
       elif (ch==1): 
           M1 = [] 
           M2 = [] 
           print("Input First Matrix ") 
           accept_matrix(M1) 
           r1 = len(M1) 
           c1 = len(M1[0]) 
           print("Input Second Matrix ") 
           accept_matrix(M2) 
           r2 = len(M2) 
           c2 = len(M2[0])  
       elif (ch==2): 
           print("\tFirst ",end=' ') 
           display_matrix(M1,r1,c1) 
           print("\tSecond ",end =' ') 
           display_matrix(M2,r2,c2)     
 
 
       elif (ch==3): 
           print("\tFirst ",end=' ') 
           display_matrix(M1,r1,c1) 
           print("\tSecond ",end =' ') 
           display_matrix(M2,r2,c2) 
           if(r1 == r2 and c1 == c2) : 
               addition_matrix(M1,M2,M3,r1,c1) 
               print("\tAddition  ") 
               display_matrix(M3,r1,c1) 
           else : 
               print("Addition not possible (order not same)") 
       elif (ch==4): 
           print("\tFirst ",end=' ') 
           display_matrix(M1,r1,c1) 
           print("\tSecond ",end =' ') 
           display_matrix(M2,r2,c2) 
           if(r1 == r2 and c1 == c2) : 
               substraction_matrix(M1,M2,M3,r1,c1) 
               print("\tSubstraction  ") 
               display_matrix(M3,r1,c1) 
           else : 
               print("substraction not possible (order not same)") 
       elif (ch==5): 
           print("\tFirst ",end=' ') 
           display_matrix(M1,r1,c1) 
           print("\tSecond ",end =' ') 
           display_matrix(M2,r2,c2) 
           if(c1 == r2) : 
               multiplication_matrix(M1,M2,M3,r1,c1,c2) 
               print("\tMultiplication  ") 
               display_matrix(M3,r1,c2) 
           else : 
               print("Multiplication not possible ") 
       elif (ch==6): 
           print("\tFirst ",end=' ') 
           display_matrix(M1,r1,c1) 
           find_transpose_matrix(M1,r1,c1,M3); 
           print("\tTranspose  ",end=' '); 
           display_matrix(M3,c1,r1) 
           print("\tSecond ",end =' ') 
           display_matrix(M2,r2,c2) 
           M3 = [] 
           find_transpose_matrix(M2,r2,c2,M3); 
           print("\tTranspose  ",end=' '); 
           display_matrix(M3,c2,r2) 
       else : 
           print ("Wrong choice entered! try again")
main()