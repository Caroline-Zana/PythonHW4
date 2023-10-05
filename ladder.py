def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError(" number needs to be no less than one and no more than 25.")

    ways = [0] * (n + 1)
    
    ways[0] = 1

    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

