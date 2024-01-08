def prime_numbers_iterative(n):
    # Check if the input is valid
    if n <= 1:
        return print("Provide a positive integer greater than one.")

    # prime[i] is going to store true if i*2 + 1 is composite
    prime = [0] * (n // 2)

    # 2 is the only prime that is even, so we can skip it and start the loop from 3
    i = 3
    while i * i < n:
        # If i is prime, the all of its multiples are composite, so they get marked as well
        if prime[i // 2] == 0:
            j = i * i
            while j < n:
                prime[j // 2] = 1
                j += i * 2
        i += 2

    # Writing 2 separately
    print(2, end=" ")

    # Printing other primes
    i = 3
    while i < n:
        if prime[i // 2] == 0:
            print(i, end=" ")
        i += 2

if __name__ == '__main__':
    limit = 1
    prime_numbers_iterative(limit)
