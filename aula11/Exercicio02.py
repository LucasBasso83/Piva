def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_above_100(count=10):
    primes = []
    num = 101
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return tuple(primes)

primes_tuple = find_primes_above_100()
print("Os 10 primeiros números primos acima de 100 são:")
print(primes_tuple)