def fibonacci_recursive(n):
    # Check if the input is valid
    if n <= 0:
        return "Provide a positive integer greater than zero."

    # First number in the Fibonacci sequence is 0
    elif n == 1:
        return 0
    # Second number in the Fibonacci sequence is 1
    elif n == 2:
        return 1
    else:
        # Recursive call to calculate the nth Fibonacci number
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(15))
