n = int(input("Enter a number: "))

orig = n
rev = 0

while n > 0:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

if rev == orig:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")
[12:04 am, 29/04/2026] Faaz: n = int(input("Enter a number: "))

orig = n
sum = 0

while n > 0:
    a = n % 10
    sum = sum + (a * a * a)
    n = n // 10

if sum == orig:
    print("The given number is Armstrong number")
else:
    print("The given number is not Armstrong number")
