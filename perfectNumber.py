n = int(input("Enter any number: "))
num = 0
for i in range(1, n):
    if(n % i == 0):
        num = num + i
if (num == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")