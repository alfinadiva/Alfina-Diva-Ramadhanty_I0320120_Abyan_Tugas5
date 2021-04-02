# Masukkan nama
Nama = input("Masukkan nama: ")
Nilai = int(input("Masukkan nilai: "))
if Nilai < 60:
    print('Halo' + ',' + str(Nama) + '!' + ' ' +'Nilai anda setelah dikonversi adalah E')
elif Nilai >= 60 and Nilai < 65:
    print('Halo' + ',' + str(Nama) + '!' + ' ' + 'Nilai anda setelah dikonversi adalah C')
elif Nilai >= 65 and Nilai < 70:
    print('Halo' + ',' + str(Nama) + '!' + ' ' +'Nilai anda setelah dikonversi adalah C+')
elif Nilai >= 70 and Nilai < 75:
    print('Halo' + ',' + str(Nama) + '!' + ' ' +'Nilai anda setelah dikonversi adalah B')
elif Nilai >= 75 and Nilai < 80:
    print('Halo' + ',' + str(Nama) + '!' + ' ' +'Nilai anda setelah dikonversi adalah B+')
elif Nilai >= 80 and Nilai < 85:
    print('Halo' + ',' + str(Nama) + '!' + ' ' + 'Nilai anda setelah dikonversi adalah A-')
elif Nilai >= 85 and Nilai <= 100:
    print('Halo' + ',' + str(Nama) + '!' + ' ' + 'Nilai anda setelah dikonversi adalah A')
else:
    pass
print()