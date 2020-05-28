print("Nama: Fira Angraini Syamsul")
print("NIM: H061181018")

import numpy as np
import math

def f(x):
    return x*e**-x+np.cos(2*x) #akar persamaan
e = 2.7182818284 #nilai bilangan euler

err =float(input("masukkan nilai error:"))
x=np.zeros(20)
x[0]=int(input("masukkan nilai batas atas:"))
x[1]=int(input("masukkan nilai batas bawah:"))
iterasi = int(input("Tentukan iterasi:"))
n=iterasi+1

for n in range(1,n):
    x[n+1]=x[n]-f(x[n])*(x[n]-x[n-1])/(f(x[n])-f(x[n-1]))
    print(n+1,x[n+1],f(x[n+1]))

while True:
    iterasi+=1
    if x[n+1]-x[n]/x[n+1]<=err:
        x[n]=x[n-1]

    else:
        x[n]=x[n+1]
    
    if abs(f(x[n]))<err:
        break