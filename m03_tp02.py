# 1 : print prime numbers from 0 to 1000
# 2 : print prime numbers from 0 to X
def is_prime(num):
    """
    if number < 2:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
        i += 1
    return True
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(limit):
    test = 1
    primes = {}
    counter = 0
    while test < limit:
        if is_prime(test):
            counter += 1
            primes[counter] = test
        test += 1
    print(primes)


print_primes(100000)

