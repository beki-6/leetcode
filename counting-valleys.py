def countValleys(steps, path):
    valleys, count = 0, 0
    for i in range(len(path)):
        if path[i] == 'U':
            count += 1
        elif path[i] == 'D':
            count -= 1
        if count == 0 and path[i] == 'U':
            valleys += 1
    return valleys

print(countValleys(8, 'UDDDUDUU'))
    