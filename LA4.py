groupA=['Kevin', 'Nimish', 'Kunal', 'Aaakash']
groupB=['Kevin', 'Sakshi', 'Sanket', 'Gaitonde', 'Kunal']
groupC=['Nimish','Aaakash', 'Vedant','Kunal']

lena=len(groupA)
lenb=len(groupB)
print(" list of Students who play both cricket and badminton : ")
resultlistCB=[]
for i in range(lenb):   
    for var in range(lena):
        if(groupB[i]==groupA[var]):
            resultlistCB.append(groupB[i]);
            break;
print(resultlistCB)

print(" list of Students who play both cricket and badminton : ")
resultlistCB=[];
if lena<lenb:
    for i in range(lena):
        for var in range(lenb):
            if(groupA[i]==groupB[var]):
                resultlistCB.append(groupA[i]);
                break;
else:
    for i in range(lenb):
        for var in range(lena):
            if(groupB[i]==groupA[var]):
                resultlistCB.append(groupB[i]);
                break;
    
print(resultlistCB)

print(" list of Students who play either cricket or badminton but not both : ")
resultlistCBN=[];
flag=0;
if lena<lenb:
    for i in range(lenb):
        for var in range(lena):
            if(groupB[i]==groupA[var]):
                flag=1;
        if(flag==0):
            resultlistCBN.append(groupB[i]);
        flag=0;
                
            
else:
    for i in range(lena):
        for var in range(lenb):
            if(groupA[i]==groupB[var]):
                flag=1;
        if(flag==0):
            resultlistCBN.append(groupA[i]);
        flag=0;
    
print(resultlistCBN)

print(" list of Students who play either cricket or badminton but not both : ")
resultlistCBN=[];
flag=0;

for i in range(lenb):
    for var in range(lena):
        if(groupB[i]==groupA[var]):
            flag=1;
    if(flag==0):
        resultlistCBN.append(groupB[i]);
    flag=0;
                
            
for i in range(lena):
    for var in range(lenb):
        if(groupA[i]==groupB[var]):
            flag=1;
    if(flag==0):
        resultlistCBN.append(groupA[i]);
    flag=0;

    
print(resultlistCBN)

print("Number of students who play neither cricket nor badminton : ")
resultlistCBNF=[];
lenc=len(groupC)
for i in range(lenc):
    for var in range(lena):
        if(groupC[i]==groupA[var]):
            flag=1;
            break;
    for var1 in range(lenb):
        if(groupC[i]==groupB[var]):
            flag=1;
            break;
    if(flag==0):
        resultlistCBNF.append(groupC[i]);
    flag=0;
lenCBNF=len(resultlistCBNF)
print(lenCBNF)
print(resultlistCBNF)
                

print(" List of students who play cricket and football : ")
resultlistCF=[];
flag=0;

for i in range(lenc):
    for var in range(lena):
        if(groupC[i]==groupA[var]):
            resultlistCF.append(groupC[i]);
            break;

print(resultlistCF)   
lenCF=len(resultlistCF)
print (lenCF)

print(" List of students who play cricket and football but not badminton : ")
resultlistCFNB=[];
for i in range(lenCF):
    for var in range(lenb):
        if(resultlistCF[i]==groupB[var]):
            flag=1;
    if(flag==0):
        resultlistCFNB.append(resultlistCF[i]);
    flag=0;
 
print(resultlistCFNB)

