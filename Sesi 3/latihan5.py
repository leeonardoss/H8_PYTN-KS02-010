import math

ulang = "y"

while ulang == "y" or ulang == "Y":
    print("Selamat datang pada program kalkulator geometri sederhana untuk objek 2 dimensi")
    print("---------------------------------------------------------------------------------")
    print("Berikut objek yang tersedia:")
    print("1. Segitiga siku-siku")
    print("2. Kotak")
    print("3. Persegi panjang")
    print("4. Lingkaran")

    opsi = int(input("Masukkan pilihan objek yang anda inginkan: "))

    if opsi == 1:
        print("Kalkulator segitiga siku-siku")
        sisi = int(input("Masukkan nilai sisi: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        keliling = 3*sisi
        luas = sisi*tinggi/2
        print("Keliling segitiga senilai ", keliling)
        print("Luas segitiga senilai ", luas)

    elif opsi == 2:
        print("Kalkulator kotak")
        sisi = int(input("Masukkan nilai sisi: "))
        keliling_kotak = 4*sisi
        luas_kotak = sisi*sisi
        print("Keliling kotak senilai ", keliling_kotak)
        print("Luas kotak senilai ", luas_kotak)

    elif opsi == 3:
        print("Kalkulator persegi panjang")
        panjang = int(input("Masukkan nilai panjang: "))
        lebar = int(input("Masukkan nilai lebar: "))
        keliling_pp = 2*panjang+2*lebar
        luas_pp = panjang*lebar
        print("Keliling persegi panjang senilai ", keliling_pp)
        print("Luas persegi panjang senilai ", luas_pp)

    elif opsi == 4:
        print("Kalkulator lingkaran")
        jari2 = int(input("Masukkan nilai jari-jari: "))
        diameter = 2*jari2
        keliling_o = diameter*math.pi
        luas_o = math.pi*(jari2**2)
        print("Keliling lingkaran senilai ", keliling_o)
        print("Luas lingkaran senilai ", luas_o)


    else:
        print("opsi yang anda pilih tidak tersedia, silakan coba lagi")
    ulang = input("Apakah anda ingin mengulang [y/n]? ")

else:
    print("program selesai")
