import numpy as np
A = np.array([[3,-0.1,-0.2,7.85],[0.1,7,-0.3,-19.3],[0.3,-0.2,10,71.4]])

n = len(A)

for k in range(0,n-1):
    for i in range(k+1,n):
        m=A[i,k]/A[k,k]
        for j in range(0,n+1):
            A[i,j]=A[i,j]-m*A[k,j]

print(A)

X = np.zeros((n,1))
X[n-1,0]=A[n-1,n]/A[n-1,n-1]

for i in range(n-2,-1,-1):
    S=0
    for j in range(i+1,n):
        S=S+A[i,j]*X[j,0]
    X[i,0]=(A[i,n]-S)/A[i,i]

print(X)