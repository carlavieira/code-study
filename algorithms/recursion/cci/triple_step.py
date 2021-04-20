def tripe_step(n):
    memo = dict()
    def possibilities(x):
        if x < 0 : return 0
        elif x == 0: return 1
        if x not in memo:
            memo[x] = possibilities(x-1) + possibilities(x-2) + possibilities(x-3)
        return memo[x]
    return possibilities(n)

print(tripe_step(4))