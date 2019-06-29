n = 1000000

ans = 0
for i in range(1, n + 1):
    var = 1 / (i ** 2)
    ans = ans + var

ans = (ans * 6) ** (.5)
print(ans)
