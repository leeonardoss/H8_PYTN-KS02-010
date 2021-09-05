import bentuk3d

ulang = 1

while ulang == 1:
    bentuk3d.main()
    
    opsi = int(input("Masukkan pilihan objek yang anda inginkan: "))
    if opsi == 1:
        print("Kalkulator bola")
        jaribola = int(input("Masukkan nilai jari-jari bola: "))
        bentuk3d.bola(jaribola)


    elif opsi == 2:
        print("Kalkulator kubus")
        rusuk = int(input("Masukkan nilai rusuk: "))
        bentuk3d.kubus(rusuk)

    elif opsi == 3:
        print("Kalkulator balok")
        panjang = int(input("Masukkan nilai panjang: "))
        lebar = int(input("Masukkan nilai lebar: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        bentuk3d.balok(panjang,lebar, tinggi)

    elif opsi == 4:
        print("Kalkulator tabung")
        jari2 = int(input("Masukkan nilai jari-jari: "))
        tinggi = int(input("Masukkan nilai tinggi tabung: "))
        bentuk3d.tabung(jari2, tinggi)

    elif opsi == 5:
        print("Terimakasih sudah menggunakan kalkulator ini. Program akan segera ditutup")
        ulang = 0
        break

    else:
        print("opsi yang anda pilih tidak tersedia, silakan coba lagi")
    
    bentuk3d.next()

    while(bentuk3d.lanjut == 1 or bentuk3d.lanjut == 2):
        if bentuk3d.lanjut == 1 :
            break

        elif bentuk3d.lanjut == 2:
            bentuk3d.tutup()
            ulang = 0
            break