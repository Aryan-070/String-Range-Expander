def basic_range(str):
    result = []
    parts = str.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    return result

print(basic_range('1-3,5,7-9'))  # Output: [1, 2, 3, 5, 7, 8, 9]
print(basic_range('10-12,14,16-18'))  # Output: [10, 11, 12, 14, 16, 17, 18]
print(basic_range('20,22-24,26'))  # Output: [20, 22, 23, 24, 26]
print(basic_range('30-32,34'))  # Output: [30, 31, 32, 34]