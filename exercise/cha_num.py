culomns = 8
rows = int(256/culomns)


for i in range(rows):
    for j in range(culomns):
        num = i * culomns + j
        print(num, chr(num), end='\t|\t')
    print('')