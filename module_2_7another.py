def get_multiplied_digits(numbers):
    str_numbers = str(numbers)
    first = int(str_numbers[0])
    if len(str_numbers) > 1:
        return first * get_multiplied_digits(int(str_numbers[1:]))
    else:
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(2077))