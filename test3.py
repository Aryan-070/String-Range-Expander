def basic_range(str,delimeters=['-', 'to', '..', '~']):
    result = []
    parts = str.split(',')
    
    for part in parts:
        part = part.strip()  # Ensure no leading/trailing spaces
        if not part:
            continue
        for delimiter in delimeters:
            if delimiter in part:
                start, end = map(int, part.split(delimiter))
                result.extend(range(start, end + 1))
                break
        else:
            try:
                result.append(int(part))
            except ValueError:
                continue
    return result

print(basic_range('1..3'))
print(basic_range(', 1-3 , ,5'))
print(basic_range(',22-24,,,,26-45,'))
print(basic_range('10 to 12'))