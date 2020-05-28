print("Nama: Fira Angraini Syamsul")
print("NIM: H061181018")

import numpy as np 
n = int(input('Input jumlah pasangan nilai = '))
SM = np.zeros((n, n))
x = np.zeros((n))
y = np.zeros((n))
for k in range(0, n):
    print('Input x [{}] = '.format(k), end=" ")
    x[k] = float(input())
    print('Input y [{}] = '.format(k), end=" ")
    y[k] = float(input())
    SM[k, 0] = y[k]

#untuk mencari nilai f(0.23)
X = float(input('Input nilai X yang ingin dicari pasangannya = '))

def faktorial(i):
    fak = 1 
    for k in range(2, i+1, 1):
        fak *= k
    return fak

for k in range(1, n):
    for i in range(0, n-k):
        SM[i, k] = SM[i+1, k-1] - SM[i, k-1]
h = x[1] - x[0]
p1 = (X - x[0])/h 
jumlah1 = SM[0, 0]
for i in range(1, n):
    suku1 = SM[0, i]
    for k in range(0, i):
        suku1 = suku1*(p1-k)
    suku1 = suku1/faktorial(i)
    jumlah1 = jumlah1+suku1

print('Hasilnya =',jumlah1)

#untuk mencari f(0.29)
Y = float(input('Input nilai X yang ingin dicari pasangannya = '))

for k in range(1, n):
    for i in range(0, n-k):
        SM[i, k] = SM[i+1, k-1] - SM[i, k-1]
h = x[1] - x[0]
p2 = (Y - x[0])/h 
jumlah2 = SM[0, 0]
for i in range(1, n):
    suku2 = SM[0, i]
    for k in range(0, i):
        suku2 = suku2*(p2-k)
    suku2 = suku2/faktorial(i)
    jumlah2 = jumlah2+suku2

print('Hasilnya =',jumlah2)