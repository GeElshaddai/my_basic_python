#INPUT DATA
angka1 = float(input("Angka1\t\t= "))
operator = input("Op (+, -, *, /)\t= ")
angka2 = float(input("Angka 2\t\t= "))
print(25*"="+ operator)

#ACTION
if operator == "+":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} \t= {hasil}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} \t= {hasil}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"{angka1} * {angka2} \t= {hasil}")

elif operator == "/":
    hasil = angka1 / angka2
    print(f"{angka1} / {angka2} \t= {hasil}")

else:
    print("NILAI YANG DI INPUT SALAH")

print("\nTerimakasih sudah mencoba")