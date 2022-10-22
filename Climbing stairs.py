def climbing_stairs(n):
    sum = 0
    memo = {1: 1, 2: 2, 3: 3, 4: 5}
    for i in range(1, n + 1):
        if i not in memo:
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

print(climbing_stairs(5))