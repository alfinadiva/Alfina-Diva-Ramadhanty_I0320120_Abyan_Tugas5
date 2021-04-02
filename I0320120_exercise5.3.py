# penggunaan if untuk 3 kasus dan selebihnya
# inputkan bilangan
print('Masukkan koordinat!')
x = int(input('Masukkan nilai x: '))
y = int(input('Masukkan nilai y: '))
info = 'Koordinat (' +str(x) + ',' + str(y) + ') berada pada kuadran'
# memriksa nilai x dan y
if x > 0 and y > 0:
    print(info + 'I')
elif x < 0 and y > 0:
    print(info + 'II')
elif x < 0 and y < 0:
    print(info + 'III')
elif x > 0 and y < 0:
    print(info + 'IV')
else:
    pass
print()