import math

def bola(jaribola):
    print("Kalkulator bola")
    volume = 4/3*jaribola**3*math.pi
    luas = 4*math.pi*jaribola**2
    print("Volume bola senilai ", volume)
    print("Luas bola senilai ", luas)
    return

def kubus(rusuk):
    print("Kalkulator kubus")
    volume_kubus = rusuk**3
    luas_kubus = 6*rusuk*rusuk
    print("Volume kubus senilai ", volume_kubus)
    print("Luas kubus senilai ", luas_kubus)
    return

def balok(panjang,lebar,tinggi):
    print("Kalkulator balok")
    volume_balok = panjang*lebar*tinggi
    luas_balok = 2*(panjang*lebar)+2*(panjang*tinggi)+2*(lebar*tinggi)
    print("Volume balok senilai ", volume_balok)
    print("Luas balok senilai ", luas_balok)
    return

def tabung(jari2, tinggi):
    print("Kalkulator tabung")
    diameter = 2*jari2
    luas_tabung = (diameter*math.pi*tinggi)+(2*math.pi*jari2**2)
    volume_tabung = math.pi*(jari2**2)*tinggi
    print("Volume tabung senilai ", volume_tabung)
    print("Luas tabung senilai ", luas_tabung)

def main():
    print("Selamat datang pada program kalkulator geometri sederhana untuk objek 3 dimensi")
    print("---------------------------------------------------------------------------------")
    print("Berikut objek yang tersedia:")
    print("1. Bola")
    print("2. Kubus")
    print("3. Balok")
    print("4. Tabung")
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