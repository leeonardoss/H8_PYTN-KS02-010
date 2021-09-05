import bentuk2D

ulang = 1

while ulang == 1:
    bentuk2D.main()
    
    opsi = int(input("Masukkan pilihan objek yang anda inginkan: "))
    if opsi == 1:
        print("Kalkulator segitiga siku-siku")
        alas = int(input("Masukkan nilai alas: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        bentuk2D.segitiga(alas,tinggi)


    elif opsi == 2:
        print("Kalkulator kotak")
        sisi = int(input("Masukkan nilai sisi: "))
        bentuk2D.kotak(sisi)

    elif opsi == 3:
        print("Kalkulator persegi panjang")
        panjang = int(input("Masukkan nilai panjang: "))
        lebar = int(input("Masukkan nilai lebar: "))
        bentuk2D.pp(panjang,lebar)

    elif opsi == 4:
        print("Kalkulator lingkaran")
        jari2 = int(input("Masukkan nilai jari-jari: "))
        bentuk2D.lingkaran(jari2)

    elif opsi == 5:
        print("Terimakasih sudah menggunakan kalkulator ini. Program akan segera ditutup")
        ulang = 0
        break

    else:
        print("opsi yang anda pilih tidak tersedia, silakan coba lagi")
    
    bentuk2D.next()

    while(bentuk2D.lanjut == 1 or bentuk2D.lanjut == 2):
        if bentuk2D.lanjut == 1 :
            break

        elif bentuk2D.lanjut == 2:
            bentuk2D.tutup()
            ulang = 0
            break