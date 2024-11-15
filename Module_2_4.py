numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False #Не понял зачем его использовать...
for i in range(len(numbers)+1):
    for k in range(len(numbers)+1):
        if i == k and i != 0 and k != 0 and i > 1 and i % 2 > 0:
            primes.append(i)
            break
        if i > 1 and i == k and i != 0 and k != 0 and i % 2 == 0:
            not_primes.append(i)
            break
print("Простые числа: ", primes)
print("Не простые числа: ", not_primes)
