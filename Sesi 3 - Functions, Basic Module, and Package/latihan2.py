p = int(input("masukkan panjang  objek: "))
l = int(input("masukkan lebar objek: "))
kel = 2*(p+l)
luas = p*l
print("Nilai yang tersedia:")
print("1. Keliling \n2. Luas")
option = int(input("pilih nilai yang ingin dicari (dalam angka): "))

if option == 1:
    print("nilai dari keliling segiempat adalah ", kel)
elif option == 2:
    print("nilai dari luas segiempat adalah ", luas)
else:
    print("opsi yang anda pilih salah")