num_map = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def roman_encrypt(num):
    if num < 0 or num > 3999:
        return f"{num} is not a valid number"
    else:
        roman = ''
        while num > 0:
            for value, roman_w in num_map:
                while num >= value:
                    num -= value
                    roman += roman_w
        return roman


for i in range(100):
    print(roman_encrypt(i))
