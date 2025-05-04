nama_file = "mbox-short.txt"  

try:
    with open(nama_file, 'r') as file:
        print("mbox-short.txt")
        for baris in file:
            print(baris.strip()) 
except FileNotFoundError:
    print(f"Error: File '{nama_file}' tidak ditemukan!")
except Exception as e:
    print(f"Terjadi error: {e}")