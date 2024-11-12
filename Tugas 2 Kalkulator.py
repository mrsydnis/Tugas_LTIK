print("Hello World")
print("Selamat datang di mini calculator")
pilihan = int(input("pilih akan menjumlah atau mengkalikan :"))
if pilihan == "menjumlah":
    a = int(input("Masukan bilangan pertama: "))
    b = int(input("Masukan bilangan kedua: "))
    c = int(input("Masukan bilangan ketiga: "))
    calculate = a + b + c
    print(f"Hasil dari penjumlah {a}+{b}+{c}={calculate}")
elif pilihan == "mengkalikan":
    A = int(input("Masukan bilangan pertama: "))
    B = int(input("Masukan bilangan kedua: "))
    C = int(input("Masukan bilangan ketiga: "))
    Calculate = A*B*C
    print(f"Hasil dari perkalian dari {A}x{B}x{C}={Calculate}")