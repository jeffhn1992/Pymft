def multiply(n , m):
    out = n * m
    return out

print(multiply(3,4))

def sumn(n):
    out = (n*(n+1))/2
    return out

def isprime(n):
    type = "Prime"
    for i in range(2, n-1):
        if  n% i ==0:
            type = "Not prime"
    return type







print(isprime(13))
print(isprime(10))
print(isprime(9))
print(isprime(5))