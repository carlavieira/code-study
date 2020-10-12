def Ex1(array):
    sum = 0
    product: int = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("{}, {}".format(sum, product))


def PrintPairs(array):
    for x in array:
        for y in array:
            print("({}, {})".format(x, y))


def PrintUnorderedPairs(array):
    for x in array:
        for y in array[array.index(x) + 1:]:
            print("({}, {})".format(x, y))


def PrintUnorderedPairs(arrayA, arrayB):
    for x in arrayA:
        for y in arrayB:
            if x < y:
                print("({}, {})".format(x, y))


def Reverse(array):
    for x in range(0, len(array) // 2 + 1):
        other = len(array) - x - 1
        temp = array[x]
        array[x] = array[other]
        array[other] = temp


# Additional Problems

# VI.1 - It will run line 44 (sum += a) b times. So, it is O(b).
def product(a, b):
    sum = 0
    for i in range(0, b):
        sum += a;
    return sum


# VI.2 - It will run line 54 b times. So it is O(b).
def power(a, b):
    if b < 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b - 1)


# VI.3 - It will run one time. So, it is O(1).
def mod(a, b):
    if b <= 0:
        return -1
    div = a // b
    return a - div * b


# VI.4 - It wil repeat line 71 and 72 (a // b) times. So, it is O(a/b).
def div(a, b):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    return count


# VI.5 - It will divide n by 2 until (in the worst case) 1, running log2(n) times. So, it is O(log2(n)).
def sqrt(n):
    return sqrt_helper(n, 1, n)


def sqrt_helper(n, min, max):
    if max < min: return -1
    guess = (min + max) // 2
    if guess * guess == n:
        return guess
    elif guess * guess < n:
        return sqrt_helper(n, guess + 1, max)
    else:
        return sqrt_helper(n, min, guess - 1)


# VI.6 - It wiil run from 1 to sqrt(n). So it is O(sqrt(n)).
def sqrt2(n):
    guess = 1
    while guess * guess <= n:
        if guess * guess == n:
            return guess
        guess += 1
    return -1


# VI.7