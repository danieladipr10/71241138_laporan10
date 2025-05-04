handle = open('mbox-short.txt')
count = 0
for line in handle:
    count = count + 1
    print('Line Count:', count)