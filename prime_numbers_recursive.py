def prime_numbers_recursive(i, n, prime): # Updates the prime list
    

    # If the square of the current number exceeds the upper limit, stops the recursion as there is no need to check further
    if i * i >= n:
        return

    ## If the current number is marked as prime (prime[i // 2] == 0) mark its multiples as composite in the prime list
    if prime[i // 2] == 0:
        j = i * i
        while j < n:
            prime[j // 2] = 1
            j += i * 2

    prime_numbers_recursive(i + 2, n, prime)

def prime_numbers_recursive_printer(n): # Prints the prime list
    # Check if the input is valid
    if n <= 1:
        return print("Provide a positive integer greater than one.")

    prime = [0] * (n // 2)

    # 2 is the only even prime so we can ignore that. Loop starts from 3
    prime_numbers_recursive(3, n, prime)

    # Writing 2 separately
    print(2, end=" ")

    # Printing other primes
    for i in range(3, n, 2):
        if prime[i // 2] == 0:
            print(i, end=" ")

if __name__ == '__main__':
    limit = 100
    prime_numbers_recursive_printer(limit)
