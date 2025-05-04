filename = input("nama file: ")
handle = open(filename)
c = 0
for line in handle:
    if line.find("ac.uk") != -1:
        c += 1
        print("Web domain 'ac.uk' ditemukan di \"" + line.strip() + "\"")
print("Jumlah: ",c)
