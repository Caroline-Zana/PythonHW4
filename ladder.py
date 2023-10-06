def my_steps(n):
    if not 1 <= n <= 25:
        raise ValueError("Input is out of bounds")

    if n <= 2:
        return n

    prev_1, prev_2 = 1, 2
    for i in range(3, n + 1):
        current = prev_1 + prev_2
        prev_1, prev_2 = prev_2, current

    return prev_2

