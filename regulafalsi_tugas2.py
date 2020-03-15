import math
def f(x):
    return 1/((x-0.3)**2+0.01) - 1/((x-0.8)**2+0.04) 

a = 1
b = 3
e = 0.000001
N = 100
iterasi = 0


print('________________________________')
print('c                       f(c)')
print('________________________________')
while True:
    iterasi += 1
    c = (b - f(b)*(b-a)/(f(b)-f(a)))
    if f(a)*f(c)<0:
        b = c
    else:
        a = c
    print('{:7.5f} \t {:+15.10f}'.format(c, f(c)))
    if abs(f(c)) <= e or iterasi >= N:
        break
print('________________________________')