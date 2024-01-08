def fibonacci_linear(n):
    # Check if the input is valid
    if n <= 0:
        return "Provide a positive integer greater than zero."

    # Initialize the first two Fibonacci numbers
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f1, f2 = 0, 1

        # Iterate from the 3rd Fibonacci number up to the nth Fibonacci number
        for x in range(2, n):
            # Calculate the current Fibonacci number
            fn = f1 + f2

            # Update f1 and f2 for the next iteration
            f1, f2 = f2, fn

        return fn

print(fibonacci_linear(15))
