def basic_range(str,delimeters):
    result = []
    parts = str.split(',')
    
    for part in parts:
        part = part.strip()  # Ensure no leading/trailing spaces
        if not part:
            continue
        for delimiter in delimeters:
            if delimiter in part:
                start, end = map(int, part.split(delimiter))
                if start > end:
                    start, end = end, start
                if start < 0 or end < 0:
                    continue
                if start == end:
                    result.append(start)
                else:
                    if start < 0 or end < 0:
                        continue
                result.extend(range(start, end + 1))
                break
        else:
            try:
                result.append(int(part))
            except ValueError:
                continue
    return result
delimeters=['-', 'to', '..', '~']
print(basic_range('1..3',delimeters))
print(basic_range(', 1-3 , ,5',delimeters))
print(basic_range(',5-3,,,,26-45,',delimeters))
print(basic_range('10 to 12',delimeters))