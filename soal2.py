def baca_soal(filename):
    try:
        with open(filename, 'r') as file:
            soal_jawaban = []
            for line in file:
                if '||' in line:
                    soal, jawaban = line.split('||', 1)
                    soal_jawaban.append((soal.strip(), jawaban.strip()))
            return soal_jawaban
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan!")
        return None

def main():
    print("Program Kuis Sederhana")
    filename = input("Nama file soal: ")
    
    soal_jawaban = baca_soal(filename)
    if not soal_jawaban:
        return
    
    print(f"\n=== Mulai Kuis dari file {filename} ===\n")
    
    for soal, jawaban_benar in soal_jawaban:
        print(soal)
        jawaban_user = input("Jawab: ").strip()
        
        # Bandingkan jawaban (case insensitive dan menghapus spasi berlebih)
        if jawaban_user.lower() == jawaban_benar.lower():
            print("Jawaban benar!\n")
        else:
            print(f"Jawaban salah! Jawaban yang benar adalah: {jawaban_benar}\n")

if __name__ == "__main__":
    main()