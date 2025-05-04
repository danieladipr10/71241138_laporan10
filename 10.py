filename = input("Nama file: ")
try:
    with open(filename) as handle:  
        total = 0
        for line in handle:
            total += len(line)
        kb = total / 1000
        print("Ukuran: " + str(kb) + " KB")  
except FileNotFoundError:  
    print("File tidak ditemukan!")