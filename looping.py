print("While loop (1 to 5):")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1

print("\nIn For loop (1 to 5):")
for j in range(1, 6):
    print(j, end=" ")

print("\nIn Nested loop (3 x 3 pattern):")
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
