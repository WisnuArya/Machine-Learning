#Latihan 1
kata = 'Menghitung Panjang Kalimat'
print("Hasil")
print(len(kata))

#Latihan 2
multiline = '''1
2
3
4
'''
print("\nFungsi Multiline")
print(len(multiline))

#Latihan 3
str1 = '1'
str2 = '2'
print("\nMenggabungkan String")
print(str1 + str2)

#Latihan Konversi Char ke ASCII
ch1 = 'a'
ch2 = ' ' #space
ch3 = 'A'
print("\nKonversi Char ke Kode ASCII")
print(ord(ch1))
print(ord(ch2))
print(ord(ch3))

#Latihan Konversi kode ASCII
print("\nKonversi Kode ASCII ke Char")
print(chr(65)+chr(75)+chr(85))

#Latihan Skip Huruf
print("\nLatihan Skip Huruf Tertentu di Python")
cthString="Latihan Python Minggu 3"
vokal = ['a','i','u','e','o']

for i in range(len(cthString)):
    if cthString[i].lower() in vokal:
        continue
    print(cthString[i], end="")
    
    
#Latihan Menentukan Output Indeks Text dengan Jaraknya
print("\n\nLatihan Output String Indeks")
print(cthString[1::4])
print(cthString[1:5])
print(cthString[3:])
print(cthString[:3])
print(cthString[::2])

#Latihan Print String Sesuai Indeks
print("\nLatihan Output String Indeks Part 2")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0]+alphabet[10]+alphabet[20])

#Mencari Kata pada Kalimat berada pada indeks keberapa
txt = """"Cegah mata rantai Covid-19,mari kita dirumah saja hingga hari Minggu.....",1,1
aku mohon yaAllah semoga wabah Covid-19 menghilang sebelum ramadhan datang ,1,-1
Pemprov Papua Naikkan Status Jadi Tanggap Darurat Covid-19. OPM,1,1FF
Covid belum nyampe prigen mbak hmm hoax,0,-2
"Nyuruh orang pintar, lu aja Togog. Itu kerumunan orang bisa nularin Covid 19 lol. Mikir !!!!",-1,-2
Pikir2 balik byk mnde plk nk setelkn lepas Covid.,0,1
"Selamat pagi, hari jum'at. Jum'at keempat di kala pandemi Covid-19. Semoga kita semua dikasih kesehatan. Aamiin.",1,-1
"Hikmah di balik musibah Covid-19, smg para pejabat pemerintahan sadar lbh mengedepankan kekayaan negara utk kesejahteraan rakyat Indonesia, bukan memperkaya diri sendiri, keluarga dan kepentingan golongan. Apalagi membela kepentingan WNA, yg jelas2 melukai kepentingan rakyat.",1,-2
Cegah Covid-19 beserta jajaran Polsek Kuranji melakukan aksi peduli berupa pembagian masker gratis bagi pengguna jalan kegiatan ini dilakukan di depan Polsek Kuranji.Kamis (9/4)Febriputraguci,1,1
Ya Allah kami memohon pada mu perkenankanlah doa doa kami kerana sesungguhnya engkaulah yang maha pengasih lagi maha penyayang...Ya Allah lindungilah kami dari penyakit berjangkit Covid 19... Aamiin.. aamiin ya rabbal a'lamin..stay at home.. jangan keluar rumah,1,-1
"Sah.. Cegah Covid-19 Meluas, Pemerintah Revisi Hari Libur dan Cuti Bersama 2020",1,2"""

print("\nMenemukan Indeks dari Kata (Covid) Pada Kalimat")
fnd = txt.find('Covid')
while fnd != -1:
    print(fnd)
    fnd = txt.find('Covid', fnd + 1)

    