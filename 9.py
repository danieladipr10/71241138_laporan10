filename = input("nama file: ")
handle = open(filename)
c = 0
for line in handle:
    if line.startswith("Subject:"):
        c += 1
        line = line.strip().title()
        print(line)
print("Jumlah: ",c)
