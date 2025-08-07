def basic_range(str):
    result = []
    parts = str.split(',')
    for part in parts:
        part = part.strip()  # Ensure no leading/trailing spaces
        if not part:
            continue
        part = part.replace(' ', '')  # Remove any spaces within the part
        if '-' in part:
            start, end = map(int, part.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    return result

print(basic_range('1-3,5,7-9'))
print(basic_range(', 1-3 , ,5'))
print(basic_range(',22-24,,,,26-45,'))
print(basic_range('30-32,34'))