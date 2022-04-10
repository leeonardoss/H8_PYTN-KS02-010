import math

def segitiga(alas, tinggi):
    print("Kalkulator segitiga siku-siku")
    keliling = 3*alas
    luas = alas*tinggi/2
    print("Keliling segitiga senilai ", keliling)
    print("Luas segitiga senilai ", luas)
    return

def kotak(sisi):
    print("Kalkulator kotak")
    keliling_kotak = 4*sisi
    luas_kotak = sisi*sisi
    print("Keliling kotak senilai ", keliling_kotak)
    print("Luas kotak senilai ", luas_kotak)
    return

def pp(panjang,lebar):
    print("Kalkulator persegi panjang")
    keliling_pp = 2*panjang+2*lebar
    luas_pp = panjang*lebar
    print("Keliling persegi panjang senilai ", keliling_pp)
    print("Luas persegi panjang senilai ", luas_pp)
    return

def lingkaran(jari2):
    print("Kalkulator lingkaran")
    diameter = 2*jari2
    keliling_o = diameter*math.pi
    luas_o = math.pi*(jari2**2)
    print("Keliling lingkaran senilai ", keliling_o)
    print("Luas lingkaran senilai ", luas_o)

def main():
    print("Selamat datang pada program kalkulator geometri sederhana untuk objek 2 dimensi")
    print("---------------------------------------------------------------------------------")
    print("Berikut objek yang tersedia:")
    print("1. Segitiga siku-siku")
    print("2. Kotak")
    print("3. Persegi panjang")
    print("4. Lingkaran")
    print("5. Tutup")

def tutup():
    print("Terimakasih sudah menggunakan kalkulator ini. Program akan segera ditutup")

def next():
    global lanjut
    lanjut = int(input("Apakah ingin lanjut? \n1. Lanjut \n2. Stop \n"))
    if lanjut < 1 or lanjut > 2:
        while lanjut < 1 or lanjut > 2:
            lanjut = int(input("Apakah ingin lanjut? \n1. Lanjut \n2. Stop \n"))
        else:
            return lanjut