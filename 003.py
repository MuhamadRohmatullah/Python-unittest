angka = int(input("Masukan angka : "))

def cekAngka(angka):
    
    if angka % 2 == 0:
        print("Genap")
    elif angka % 2 == 1:
        print("Ganjil")

cekAngka(angka)

