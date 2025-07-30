# list comprehension
# step by step input of lg
n=[int(input(f" enter a num {i+1}:"))
   for i in range(5)]
print(n)

n=[int(x) for x in input("enter 5 num with space").split()[:5]]
print(n)

#nested lc.... loop with in loop in a single:lc
n= int(input("enter a table size :"))
table=[[i*j for j in range(1,n+1)]for i in range(1,n+1)]
print("tables of math")
for row in table:
    print(row)

#create a n*n matrix with mannual input numbers 
# input seperated spaces
#print all the rows in lc only
n=input("enter 9 numbers with space:").split()
if len(n) !=9:
    print("exactly 9 numbers:")
else:
    num=[int(x) for x in n]
    matrix=[[num[i*3+j]for j in range(3)]for i in range(3)]
    transpose=[[matrix[i][j] for i in range(3)] for j in range(3)]
for r in matrix:
    print(r)
for r in transpose:
    print(r)

m=int(input("enter a size:"))
n=[int(x) for x in input("enter num:").split()[:m*m]]
matrix=[[n[i*m+j]for j in range(m)]for i in range(m)]
for k in matrix:
    print(k)
f=[k for r in matrix for k in r]
print(f)

# code to consider a lc:to cal square of 16 val as a n*n matrix and print the list of squares in each row
m=int(input("enter a size:"))
n=[int(x) for x in input("enter num:").split()[:m*m]]
matrix=[[n[i*m+j]**2 for j in range(m)]for i in range(m)]
for k in matrix:
    print(k)
f=[k for r in matrix for k in r]
print(f)

m=int(input("enter a size:"))
n=[int(x) for x in input("enter num:").split()[:m*m]]
matrix=[[n[i*m+j] if n[i*m+j]%2==0 else 0 for j in range(m)]for i in range(m)]
for k in matrix:
    print(k)

m=int(input("enter a size:"))
n=[int(x) for x in input("enter num:").split()[:m*m]]
matrix=[[n[i*m+j] if n[i*m+j]%2!=0 else 0 for j in range(m)]for i in range(m)]
for k in matrix:
    print(k)

m=int(input("enter a size:"))
n=[int(x) for x in input("enter num:").split()[:m*m]]
matrix=[[2 if n[i*m+j]%2==0 else 1 for j in range(m)]for i in range(m)]
for k in matrix:
    print(k)