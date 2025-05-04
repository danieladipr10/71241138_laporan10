handle = open('mbox-short.txt')
count = 1
for line in handle:
    if line.startswith("Date:") and count <= 10:
        count += 1
        print(line)