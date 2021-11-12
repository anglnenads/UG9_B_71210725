#input
name =input("Nama : ")
born =input("Tempat tanggal lahir : ")

#proses
nama = (name)
a = nama.rpartition(" ")
reverse = a[::-1]

#cetak layar
print("Heloo! ", reverse)
print("Anda lahir di ", born)
