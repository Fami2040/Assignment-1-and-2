def rabbit_pairs(n, k):
    # Base case: if n is 1 or 2, we directly return 1
    # This is because at month 1 and 2, we only have one pair of rabbits.
    if n == 1 or n == 2:
        return 1

    # Create an array `F` to store the number of rabbit pairs at each month.
    # We need to store results for months 1 to n, so the array size is n+1.
    F = [0] * (n + 1)

    # Initialize the base cases: 1 pair of rabbits at month 1 and month 2.
    F[1] = 1
    F[2] = 1

    # Starting from month 3, we calculate the number of rabbit pairs using the recurrence relation:
    # F(n) = F(n-1) + k * F(n-2)
    # Where F(n-1) represents surviving pairs from the previous month,
    # and k * F(n-2) represents the new pairs produced by reproduction-age rabbits.
    for i in range(3, n + 1):
        F[i] = F[i - 1] + k * F[i - 2]

    # After filling the array, return the number of rabbit pairs at month n.
    return F[n]

# Example usage:
n, k = 33, 4
# The result will be 19, since after 5 months and each pair producing 3 offspring,
# the number of rabbit pairs will grow as per the modified Fibonacci sequence.
print(rabbit_pairs(n, k))  # Output should be 19
