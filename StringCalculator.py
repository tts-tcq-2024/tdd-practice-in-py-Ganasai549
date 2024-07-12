def add(input):
    if not input:
        return 0

    delimiter = ','
    if input.startswith('//'):
        delimiter = input[2]
        input = input[4:]
    else:
        input = input.replace('\n', delimiter)

    inp = input.split(delimiter)
    return sum(int(inp) for inp in inp if int(inp) <= 1000)
