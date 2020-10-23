def isPerfectNumber(n):
    n = int(n)
    num = 0
    for i in range(1, n):
        if(n % i == 0):
            num = num + i
    if (num == n):
        return True
    return False

limit = 10000
result = []

for n in range(1, limit):
    if isPerfectNumber(n):
        result.append(n)

print(result)