def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            
            max_lines = max(len(lines1), len(lines2))
            differences = []
            
            for i in range(max_lines):
                line1 = lines1[i].strip() if i < len(lines1) else None
                line2 = lines2[i].strip() if i < len(lines2) else None
                
                if line1 != line2:
                    differences.append((i+1, line1, line2))
            
            return differences
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

def main():
    print("Program Pembanding File Teks")
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")
    
    differences = compare_files(file1, file2)
    
    if differences is None:
        return
    
    if not differences:
        print("Kedua file identik!")
    else:
        print("\nPerbedaan ditemukan:")
        print("Baris | File 1 | File 2")
        print("------|--------|--------")
        for diff in differences:
            line_num, line1, line2 = diff
            print(f"{line_num:5} | {line1 if line1 is not None else '<TIDAK ADA>':6} | {line2 if line2 is not None else '<TIDAK ADA>':6}")

if __name__ == "__main__":
    main()