# diziler- listeler -start

sayilar= [100, 200, 300, 400, 500, "merhaba", 15.5, True] #listedeki tüm elemanların veri tipi aynı olmak zorunda değil
#programci saymaya sıfırdan başlar
# index indis => 0 başlangıç değeri -1 son index
print(sayilar)
print(sayilar[0])
print(sayilar[5])

print(sayilar)
sayilar.append(100)
sayilar.append(600)   # =>listenin sonuna eleman ekler
print(sayilar)
sayilar.pop()  # parantez içindeki indexi siler eğer parantez içi boşsa sonunu siler
print(sayilar)
sayilar.remove(100)  #indexe göre değil değere göre siler ve aynı olan birden fazla değer varsa aynı olan ilk değeri siler
print(sayilar)
sayilaraEkleme= [700,800,900]
sayilar.extend(sayilaraEkleme)  #içerisindeki değerleri listeye ekler appendin aksine sonuncuyu değil hepsini ekler.
print(sayilar)
sayilar.clear()  #listenin hepsinin temizlenmesini sağlar "Dizinin içini boşaltan fonksiyon"
print(sayilar)

# diziler- listeler -end

# string interpolation -start

hello= "Merhaba"
username= "Özge"

print(hello + " " + username)

totalText= hello + " " + username
print(totalText)

totalText= "{message} Sayın {name}".format(message=hello, name=username)
print(totalText)

#f-string

totalText= f"Hoşgeldiniz {username}"
print(totalText)

# string interpolation -end

# karar yapıları -start

ortalamaNot= input("Lütfen Ortalamanızı Giriniz:")

# if else blokları
# 4 satır =>1 Tab/indent
# numerik => int, double
# type conversion -start

ortalamaNotAsInteger= int(ortalamaNot)

# type conversion -end
if ortalamaNotAsInteger > 80:
    print("Başarıyla Geçtiniz")

# else if =>elif
elif ortalamaNotAsInteger > 60:
    print("Ortalama")
elif ortalamaNotAsInteger > 50:
    print("Normal")
else:
    print("Kaldınız")

studentCount = 44
if studentCount > 20:
    print("Öğrenciler ders için hazır")

print("if bloğundan bağımsız kısım")


vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

ortalama= int(ortalamaAsInteger)

if final < 40:
    print("Kaldı")

if ortalamaAsInteger < 50:
    print("Kaldı")

if (vize*2) == final:
    print("Kaldı")

else:
    print("Geçti")


# karar yapıları -end