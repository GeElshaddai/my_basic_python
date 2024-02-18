# START DAN AKHIR DARI PERULANGAN
start, end = 1, 500

# FOR LOOP
for i in range(start, end + 1):
    
    # HANYA GANJIL
    if i % 2 != 0:
        print(i, end = " ")