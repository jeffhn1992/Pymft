a = 1
b = 1


while a<1000000:
    print(a,b)
    a = a + b
    b = a + b


n = 5
a=1
b=1
#for i in range(n):
    #print(a , b)
    #a = a + b
    #b = a + b



for i in range(n):
    print(b)
    a , b = b , a+b

