# Program penghitung nilai terkecil dan terbesar
# by Kevin Alvaro Adianto

kecil=int(input("Masukkan Bilangan 1 :"))
besar=kecil
ke = 2
tambah = str.lower(input("Tambah Lagi? (Y/T)"))

while (tambah == "y"):
    bilangan=int(input("Masukkan Bilangan"+ str(ke)+ ":"))
    ke=ke+1

    if bilangan < kecil:
        kecil=bilangan
    
    if bilangan > besar:
        besar=bilangan

    tambah = str.lower(input("Tambah Lagi? (Y/T)"))

print("Bilangan Terkecil adalah:", kecil)
print("Bilangan Terbesar adalah:", besar)
