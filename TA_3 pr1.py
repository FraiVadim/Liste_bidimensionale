A=[[1,2,3,4,5],
   [2,3,4,5,6],
   [3,4,5,6,7],
   [4,5,6,71,8],
   [6,6,7,8,9]]
sl=0
print ('Fisierul bidimensional:',A)
print()
for i in range(0,len(A)):
    print ('suma liniei',i+1,':', sum(A[i]))
print()
for j in range (0,len(A)):
    coloana=[]
    for i in A:
        coloana.append(i[j])
    print ('suma coloanei',j+1,':',sum(coloana))
print()
dp=[]
for j in range (0,len(A)):
    for i in A:
        if A.index(i)==j:
            dp.append(i[j])
print('diagonala principala:',dp)
print()
ds=[]
for j in range (0,len(A)):
    for i in A:
        if A.index(i)+j==len(A)-1:
            ds.append(i[j])
print('diagonala secundara:',ds)