n=int(input("Enter the number of terms:"))
a, b = 0, 1

# Check if number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    print(a, b, end=" ")

    # Generate Fibonacci series
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
