def penjumlah(x,y):
    hasil = x+y
    return hasil
def pengurangan(x,y):
    hasil = x-y
    return hasil
def perkalian(x,y):
    hasil = x*y
    return hasil
def pembagian(x,y):
    hasil = x/y
    return hasil

print("pilihan:")
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")

a = int(input("masukkan pilihanmu : "))


bil1 = int(input("bilangan 1 ="))
bil2 = int(input("bilangan 2 ="))

if a == 1:
    print(penjumlah(bil1,bil2))
elif a == 2:
    print(pengurangan(bil1,bil2))
elif a == 3:
    print(perkalian(bil1,bil2))
elif a == 4:
    print(pembagian(bil1,bil2))