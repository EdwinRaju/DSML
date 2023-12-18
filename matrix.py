import numpy as np
def input1():
    r = int(input("Enter the no of rows"))
    c = int(input("enter the no of columns"))
    imatrix=[]
    for i in range(r):
        r=[]
        for j in range(c):
            elements = int(input("Enter the elemnts"))
            r.append(elements)
        imatrix.append(r)
    return np.array(imatrix)

matrix1 = input1()
matrix2 = input1()
print("Matrix1")
print(matrix1)
print("Matrix2")
print(matrix2)