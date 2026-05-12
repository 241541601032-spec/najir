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
