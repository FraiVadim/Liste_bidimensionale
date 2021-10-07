n=int(input('dati numarul de linii si coloane '))
A=[]
if n>=2 and n<=10:
    for i in range(0,n):
        v=[]
        print ('dati numerele din linia ',i+1)
        for j in range (0,n):
            x=int(input())
            v.append(x)
        A.append(v)
print (A)
print()
dp=[]
for i in range(len(A[0])):
    for j in range (0,len(A)):
        if i==j:
            dp.append(A[i][j])
print('a. Suma componentelor care se afla pe diagonala principala: ',sum(dp))
print()
ds=[]
for i in range(len(A[0])):
    for j in range (0,len(A)):
        if i+j==len(A)-1:
            ds.append(A[i][j])
print('b. Suma componentelor care se afla pe diagonala secundara: ',sum(ds))
print()
susdp=[]
for i in range(len(A[0])):
    for j in range (0,len(A)):
        if i<j:
            susdp.append(A[i][j])
print('c. Suma componentelor care se afla mai sus de diagonala principala: ',sum(susdp))
print()
josdp=[]
for i in range(len(A[0])):
    for j in range (0,len(A)):
        if i>j:
            josdp.append(A[i][j])
print('d. Suma componentelor care se afla mai jos de diagonala principala: ',sum(josdp))
print()
susds=[]
for i in range(len(A[0])):
    for j in range (0,len(A)):
        if (i+j)<n-1:
            susds.append(A[i][j])
print('e. Suma componentelor care se afla mai sus de diagonala secundara: ',sum(susds))
print()
josds=[]
for i in range(len(A[0])):
    for j in range (0,len(A)):
        if (i+j)>n-1:
            josds.append(A[i][j])
print('f. Suma componentelor care se afla mai jos de diagonala secundara: ',sum(josds))