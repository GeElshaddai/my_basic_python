"""
number = 10

if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")

print(number)
"""

print(5*"-" +"KALKULATOR PEMBAGIAN"+ 5*"-")
x = int(input("Masukkan nilai x = "))
y = int(input("Masukkan nilai y = "))

try:
    print("Hasil pembagian = ", x/y)
except:
    print("Division by zero")