from PKG import mod2d

ulang = 1

while ulang == 1:
    mod2d.main()
    
    opsi = int(input("Masukkan pilihan objek yang anda inginkan: "))
    if opsi == 1:
        print("Kalkulator segitiga siku-siku")
        alas = int(input("Masukkan nilai alas: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        mod2d.segitiga(alas,tinggi)


    elif opsi == 2:
        print("Kalkulator kotak")
        sisi = int(input("Masukkan nilai sisi: "))
        mod2d.kotak(sisi)

    elif opsi == 3:
        print("Kalkulator persegi panjang")
        panjang = int(input("Masukkan nilai panjang: "))
        lebar = int(input("Masukkan nilai lebar: "))
        mod2d.pp(panjang,lebar)

    elif opsi == 4:
        print("Kalkulator lingkaran")
        jari2 = int(input("Masukkan nilai jari-jari: "))
        mod2d.lingkaran(jari2)

    elif opsi == 5:
        print("Terimakasih sudah menggunakan kalkulator ini. Program akan segera ditutup")
        ulang = 0
        break

    else:
        print("opsi yang anda pilih tidak tersedia, silakan coba lagi")
    
    mod2d.next()

    while(mod2d.lanjut == 1 or mod2d.lanjut == 2):
        if mod2d.lanjut == 1 :
            break

        elif mod2d.lanjut == 2:
            mod2d.tutup()
            ulang = 0
            break