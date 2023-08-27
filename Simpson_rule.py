def f(x):
    return (x**4) - (2*x) + 1

N = 10
a = 0
b = 2
h = (b - a)/N
sum_one=0
sum_two=0

s = f(a) + f(b)

for k in range(1,N,2):
    sum_one += f(a+k*h)

for k in range(2,N,2):
    sum_two += f(a+k*h)

result = ((4* sum_one) + (2*sum_two) + s) * (h/3) 

error = (result - 4.4) / result
print(error)