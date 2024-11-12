def get_multiplied_digits(number=0):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) >1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first != 0:
        return first
    return 1

result = get_multiplied_digits(402030)
print(result)