#input
bar1 = input("====GEBYAR DISKON==== ")
bar2 = input("====MASUKKAN JUMLAH BARANG YANG YANG DIPESAN==== ")
bar3 = int(input("KIPAS ANGIN DISKON 10%  Rp. 25.000,00   : "))
bar4 = int(input("SEPEDA DISKON 55%       Rp. 6.000,00    : "))
bar5 = int(input("HELM ROSSI DISKON 77%   Rp. 8.000,00    : "))
bar6 = input("====TOTAL====")

#proses
totalkipas = bar3 * 25000 * 10 / 100
totalsepeda  = bar4 * 6000 *  55 / 100
totalhelm = bar5 *  8000 * 77 / 100
totalkeseluruhan = totalkipas + totalsepeda + totalhelm 

#cetak layar
print("TOTAL KIPAS ANGIN   : Rp ", totalkipas )
print("TOTAL SEPEDA SUPER  : Rp ", totalsepeda)
print("TOTAL HELM ROSSI    : Rp ", totalhelm)
print("Jumlah total diskon yang didapat adalah Rp ",totalkeseluruhan)
