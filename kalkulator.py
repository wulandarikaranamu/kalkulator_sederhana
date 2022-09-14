print('''operasi aritmatika :
      A. penjumlahan [+]
      B. pengurangan [-]
      C. perkalian   [*]
      D. pembagian   [/]
      E. sisa bagi   [%]
      F. perpangkatan    [**]
      G. pembagian bulat [//] \n ''')

kalkulator = "Kalkulator Sederhana"
print(kalkulator.center(35, "="))

operasi = input("masukkan operator : ")
user = input("user meminta operasi : ")
bilangan_1 = int(input("masukkan bilangan pertama :"))
bilangan_2 = int(input("masukkan bilangan kedua :"))

if operasi == "A" or operasi == "a":
    hasil = bilangan_1 + bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} + {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
elif operasi == "B" or operasi == "b":
    hasil = bilangan_1 - bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} - {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
elif operasi == "C" or operasi == "c":
    hasil = bilangan_1 * bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} * {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
elif operasi == "D" or operasi == "d":
    hasil = bilangan_1 / bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} / {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
elif operasi == "E" or operasi == "e":
    hasil = bilangan_1 % bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} % {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
elif operasi == "F" or operasi == "f":
    hasil = bilangan_1 ** bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} ** {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
elif operasi == "G" or operasi == "g":
    hasil = bilangan_1 // bilangan_2 
    print(f'hasil penjumlahan adalah : {bilangan_1} // {bilangan_2} = {hasil}')
    print("Kalkulator Berhasil, Terima Kasih !")
else :
    print("operasi yang dimasukkan tidak sesuai!") 