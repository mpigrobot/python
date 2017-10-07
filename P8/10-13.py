def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],reversed_cmp)