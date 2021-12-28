def naya():
    print("merupakan mahasiswa angkatan 2021 dan lulus sma angkatan 2020")
naya()


print("pengabungan")
def tinggal ():
    naya()
    print("tinggal di kelurahan tande")
    print("kecamatan banggae timmur")
tinggal()

def hargatotalayam (kg):
    harga = 25000
    harga_total= kg*harga
    print("harga",kg,"kg ayam adalah",harga_total)

hargatotalayam(5)

print("contoh kasus yang sama namun bentuk yang beda")
a=int(input("masukkan harga:"))
b=int(input("masukkan kg:"))
def total (kg,harga):
        return kg * harga
x=total(b,a)
print(x)

def siswa (nama,kelas='G',anak='RPL'):
    print("nama saya:",nama)
    print("anak :",anak)
    print("kelas:",kelas)
siswa(naya,kelas='d',anak='orang')
