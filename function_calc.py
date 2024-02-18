#BASIC CALCULATOR USING FUNCTION IN PYTHON
def calc(input1, input2):
    tambah = input1 + input2
    kurang = input1 - input2
    kali = input1 * input2
    bagi = input1 / input2
    return tambah,kurang,kali,bagi

x = int(input("Masukkan nilai x = "))
y = int(input("Masukkan nilai y = "))
a,b,c,d = calc(x,y)

print("\nHASIL :")
print(f"HASIL TAMBAH = {a}")
print(f"HASIL KURANG = {b}")
print(f"HASIL KALI = {c}")
print(f"HASIL BAGI = {d}")