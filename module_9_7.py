def is_prime(func):
    print(func())
    if 2 % 2 == 0:
        print('простое')
        return func
    return func


@is_prime
def sum_three(*mda):
    return sum(mda)


result = sum_three(2, 3, 6)
print(result)