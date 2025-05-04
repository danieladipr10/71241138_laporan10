try:
    with open('mbox-short.txt', 'r') as handle:  
        hasil = handle.read()
        
        
        print("Ukuran:", len(hasil), "bytes") 
        
        
        if len(hasil) >= 16:
            reversed_last_16 = hasil[-16:][::-1]  
            print("16 huruf terakhir (dibalik):", reversed_last_16)
        else:
            print("File terlalu pendek - kurang dari 16 karakter")
            
except FileNotFoundError:
    print("Error: File 'mbox-short.txt' tidak ditemukan")
except Exception as e:
    print("Terjadi error:", str(e))

# handle = open('mbox-short.txt')
# hasil = handle.read()
# print("Ukuran: " + len(hasil) + "bytes")
# print("Huruf dari belakang sendiri mundur 16 huruf adalah: " + hasil[-16::1])