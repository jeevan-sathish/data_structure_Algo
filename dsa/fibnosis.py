def fibnosos(n):
    fib = [0,1]
    for i in range(2,n):
        result = fib[i -1] + fib[i-2]
        fib.append(result)

    return fib

print(fibnosos(10))