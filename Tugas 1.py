#Nama: Mursyid Daniswara
#NIM: 2401311
#Kelas: RPL 1C

Panjang = int(input("Masukan Panjang Lapangan: "))
Lebar = int(input("Masukan Lebar Lapangan: "))

SatuPutaran = (Panjang + Lebar) * 2

Jarak = int(input("Masukan jarak berlari(km): "))

total = SatuPutaran * Jarak

convertToKm = total / 1000

print(f"Jarak yang ditempuh yaitu {convertToKm} Km")