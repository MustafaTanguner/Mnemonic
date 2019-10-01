import cv2
import random
import math
import sys
import os
import os.path

print("""

ooo        ooooo                                                                o8o            
`88.       .888'                                                                `"'            
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.  
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8 
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888       
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8 
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' 

""")
print("*" * 30, "Mnemonic Şifreleme Yazılımına Hoş Geldiniz.", "*" * 30, )

print("*" * 31,"Welcome to Mnemonic Encryption Software", "*" * 33, )
print("*" * 105)

print("*" * 105, )
print("*" * 30, "https://www.youtube.com/watch?v=pBSR3DyobIY", "*" * 30, )

print("-" * 105, )
print("")
print("")

while True:
    gelen = input("Access Code image file Path/Lütfen resim yolunu belirtiniz:")
    if os.path.isfile(gelen) and os.access(gelen, os.R_OK):
        print("Dosya var ve okunabilir")
        print ("File exists and is readable")
        break
    else:
        print ("Either the file is missing or not readable")
        print("Hatalı yada okunamıyor lütfen tekrar deneyiniz.")
def encode():

    resim = cv2.imread(gelen)
    b = resim[100, 100, 0]
    g = resim[100, 100, 1]
    r = resim[100, 100, 2]
    px = resim[100, 100]
    resim[100, 100] = [255, 255, 255]
    resim[100, 100, 0] = 221
    resim[100, 100, 1] = 223
    resim[100, 100, 2] = 224

    px = resim[100, 100]
    px[0] = 224
    px[1] = 225
    px[2] = 226

    d = resim[9, :, 0], resim[9, :, 1], resim[9, :, 2]


    with open('veriler.txt', 'w') as f:
        f.write(str(d))


encode()

veriler = open("veriler.txt", "r+")


def semboleritemizle(veriler):
    sembolsuzsayilar = []
    g = "dtype=uint8)(,.','a" "rray[]"
    for t in veriler:
        for h in g:
            if h in t:
                t = t.replace(h, "")
        if (len(t) > -1):
            sembolsuzsayilar.append(t)
    return sembolsuzsayilar
with open("pixel.txt" , "w")as f:
        for item in semboleritemizle(veriler):
            f.write("%s" % item)

with open('pixel.txt', 'r')as f:
        sayilar = []
        Kindi = f.read()
        Kindi = Kindi.lstrip()
        Kindi = Kindi.replace(" ", "")

        q = (len(Kindi) -100)
        w = (len(Kindi) -500)
        e = (len(Kindi) -50)
        r = (len(Kindi) -86)
        f = (len(Kindi) -15)
        t = (len(Kindi) -22)
        y = (len(Kindi) -55)
        u = (len(Kindi) -12)
        o = (len(Kindi) -155)
        p = (len(Kindi) -123)
        a = (len(Kindi) -55)
        s = (len(Kindi) -58)
        d = (len(Kindi) -99)
        n = (len(Kindi) -66)
        g = (len(Kindi) -77)
        h = (len(Kindi) -11)
        j = (len(Kindi) -22)
        k = (len(Kindi) -7)
        l = (len(Kindi) -42)
        z = (len(Kindi) -66)
        x = (len(Kindi) -112)
        c = (len(Kindi) -33)
        v = (len(Kindi) -47)
        b = (len(Kindi) -18)
        i = (len(Kindi) -29)
        m = (len(Kindi) -59)

        tan = (q*w*e*r*t*y*u*o*p*a*s*d*n*g*h*j*k*l*z*x*c*v*b*m*i)*(math.factorial(1111))*(math.factorial(999))
        sayilar.append(tan)


for kelime in  sayilar:



    x = str(random.randrange(0, 1))
    print("\n\nProcessing:\İŞLEM DEVAM EDİYOR LÜTFEN BEKLEYİNİZI: " + x + ".txt'dir.\n\n")
    print("*" *15, "İŞLEM TAMAMLANDI", "*" *15)
    print("*" *15, "PROCESS COMPLETED", "*" *15)

    with open("%s.txt" % x, "w")as f:
        for item in sayilar:
            f.write("%s" % item)

print("Resim Analizi Başaralı Bir Şekilde Tamamlandı. Özel Kodunuz:",
      "\nImage Analysis Completed Successfully. Your Special Code:")
print(sayilar)


def sifrele():
    with open('0.txt', 'r')as f:
        f_conte = f.read()
        x = int(f_conte)

    if x == x:
        key = [(x // (10 ** i)) % 10 for i in range(math.ceil(math.log(x, 10)) - 1, -1, -1)]
    toplam = 0
    for i in key:
        toplam = toplam + i
    


    text = str(input("Text/Lütfen Şifrelenecek Metini Giriniz:"))
    text = text.lower()
    letters = [c for c in text]
    sifre = []
    for i in letters:
        if i == "a":
            i = 16
            sifre.append(i)
        elif i == "b":
            i = 52
            sifre.append(i)
        elif i == "c":
            i = 23
            sifre.append(i)
        elif i == "ç":
            i = 56
            sifre.append(i)
        elif i == "d":
            i = 65
            sifre.append(i)
        elif i == "e":
            i = 34
            sifre.append(i)
        elif i == "f":
            i = 21
            sifre.append(i)
        elif i == "g":
            i = 87
            sifre.append(i)
        elif i == "ğ":
            i = 8774
            sifre.append(i)
        elif i == "h":
            i = 44
            sifre.append(i)
        elif i == "ı":
            i = 64
            sifre.append(i)
        elif i == "i":
            i = 73
            sifre.append(i)
        elif i == "j":
            i = 312
            sifre.append(i)
        elif i == "k":
            i = 98
            sifre.append(i)
        elif i == "l":
            i = 12
            sifre.append(i)
        elif i == "m":
            i = 13
            sifre.append(i)
        elif i == "n":
            i = 45
            sifre.append(i)
        elif i == "o":
            i = 399
            sifre.append(i)
        elif i == "ö":
            i = 541
            sifre.append(i)
        elif i == "p":
            i = 232
            sifre.append(i)
        elif i == "r":
            i = 421
            sifre.append(i)
        elif i == "s":
            i = 38
            sifre.append(i)
        elif i == "ş":
            i = 19
            sifre.append(i)
        elif i == "t":
            i = 17
            sifre.append(i)
        elif i == "u":
            i = 671
            sifre.append(i)
        elif i == "ü":
            i = 231
            sifre.append(i)
        elif i == "v":
            i = 287
            sifre.append(i)
        elif i == "y":
            i = 743
            sifre.append(i)
        elif i == "q":
            i = 7433
            sifre.append(i)
        elif i == "z":
            i = 634
            sifre.append(i)
        elif i == "w":
            i = 785
            sifre.append(i)
        elif i == "x":
            i = 585
            sifre.append(i)
        elif i == "1":
            i = 693
            sifre.append(i)
        elif i == "2":
            i = 478
            sifre.append(i)
        elif i == "3":
            i = 884
            sifre.append(i)
        elif i == "4":
            i = 284
            sifre.append(i)
        elif i == "5":
            i = 25
            sifre.append(i)
        elif i == "6":
            i = 49
            sifre.append(i)
        elif i == "7":
            i = 405
            sifre.append(i)
        elif i == "8":
            i = 161
            sifre.append(i)
        elif i == "9":
            i = 11
            sifre.append(i)
        elif i == "10":
            i = 154
            sifre.append(i)
        elif i == "0":
            i = 224
            sifre.append(i)
        elif i == "(":
            i = 2311
            sifre.append(i)
        elif i == ")":
            i = 22
            sifre.append(i)
        elif i == ".":
            i = 41
            sifre.append(i)
        elif i == "=":
            i = 55
            sifre.append(i)
        elif i == "/":
            i = 440
            sifre.append(i)
        elif i == "\ ":
            i = 4401
            sifre.append(i)
        elif i == "-":
            i = 33
            sifre.append(i)
        elif i == ":":
            i = 22
            sifre.append(i)
        elif i == ";":
            i = 11
            sifre.append(i)
        elif i == ",":
            i = 5
            sifre.append(i)
        elif i == " ":
            i = 51122
            sifre.append(i)
        elif i == "?":
            i = 5224
            sifre.append(i)
        elif i == "!":
            i = 533
            sifre.append(i)
        elif i == "_":
            i = 5331
            sifre.append(i)

    tamkilit = []
    for i in sifre:
        i = i * toplam
        tamkilit.append(i)
    x = str(random.randrange(1, 10000))
    print("\n\nFile Name\Dosyanızın ADI: " + x + ".txt'dir.\n\n")

    with open("%s.txt" % x, "w")as f:
        for item in tamkilit:
            f.write("%s\n" % item)
    s = open("%s.txt" % x, "r")
    print("ENCRYPTION MESSAGE\ŞİFRELENMİŞ MESAJ:")
    print("Your file has been successfully saved.")
    print(tamkilit)

   


def coz():
    with open('0.txt', 'r')as f:
        f_conte = f.read()
        f_conte = f_conte.lstrip()
        f_conte = f_conte.replace(" ", "")
        x123 = int(f_conte)
    print("Lütfen çözülcek metini giriniz dosya olarak girmek İçin '1' 'E Ctrl + V için '2' Basınız:")
    print("Please enter the ENCRYPT message to file Path '1' ' or Ctrl + V '2' Press:")
    Metingiris = int(input(">>>>"))
    if Metingiris == 1 or Metingiris == 2:
        pass

    else:
        print("Feil input/Hatalı Giriş Tekrar Deneyiniz.")
        coz()

    if Metingiris == 1:
        Tamkilit = []
        try:
            with open(input("Please enter the file Path\Dosya Adını Uzantısıyla giriniz:"), "r") as f:
                for line in f:
                    Tamkilit.append(line.strip())
        except:
            print("Not Found File\Dosya Bulunamadı...")
            coz()

        Coz = []
        for i in Tamkilit:
            Coz.append(int(i))
    if Metingiris == 2:
        Tamkilit = input("Please enter the text to be solved \Lütfen çözülecek metni giriniz:")

        if Tamkilit.isdigit():
            pass
        else:
            print("Hatali Metin Girildi.Şifreli Metin Harf İçeremez.\nLütfen Tekrar Giriniz.")
            print("Incorrect Text Entered Encrypted text cannot contain letters.Please enter again:")
            coz()

        if Tamkilit[0] == "[":
            Tamkilit = Tamkilit[1:len(Tamkilit) -1]

        else:
            Coz = Tamkilit.split(",")

    Coz0 = []

    for i in Coz:
        Coz0.append(int(i))



    key = [(x123 // (10 ** i)) % 10 for i in range(math.ceil(math.log(x123, 10)) - 1, -1, -1)]
    toplam = 0

    for i in key:
        toplam = toplam + i

    Coz1 = []

    for i in Coz0:
        if i % toplam == 0:
            i = i / toplam
            Coz1.append(i)
        else:
            print(
                "WRONG KEY OR ERROR PASSWORD:key entered by message does not match\n\YANLIS ANAHATAR VEYA HATALI SIFRALI MESAJ GIRILDI:nMesaj ile Girilen Anahtar Uyusmuyor Lütfen Terkrar Deneyiniz.\n")
            
            coz()

    COz2 = []

    for i in Coz1:
        if i == 16:
            i = "a"
            COz2.append(i)
        if i == 52:
            i = "b"
            COz2.append(i)
        if i == 23:
            i = "c"
            COz2.append(i)
        if i == 56:
            i = "ç"
            COz2.append(i)
        if i == 65:
            i = "d"
            COz2.append(i)
        if i == 34:
            i = "e"
            COz2.append(i)
        if i == 21:
            i = "f"
            COz2.append(i)
        if i == 87:
            i = "g"
            COz2.append(i)
        if i == 8774:
            i = "ğ"
            COz2.append(i)
        if i == 44:
            i = "h"
            COz2.append(i)
        elif i == 64:
            i = "ı"
            COz2.append(i)
        elif i == 73:
            i = "i"
            COz2.append(i)
        elif i == 312:
            i = "j"
            COz2.append(i)
        elif i == 98:
            i = "k"
            COz2.append(i)
        elif i == 12:
            i = "l"
            COz2.append(i)
        elif i == 13:
            i = "m"
            COz2.append(i)
        elif i == 45:
            i = "n"
            COz2.append(i)
        elif i == 399:
            i = "o"
            COz2.append(i)
        elif i == 541:
            i = "ö"
            COz2.append(i)
        elif i == 232:
            i = "p"
            COz2.append(i)
        elif i == 421:
            i = "r"
            COz2.append(i)
        elif i == 38:
            i = "s"
            COz2.append(i)
        elif i == 19:
            i = "ş"
            COz2.append(i)
        elif i == 17:
            i = "t"
            COz2.append(i)
        elif i == 671:
            i = "u"
            COz2.append(i)
        elif i == 231:
            i = "ü"
            COz2.append(i)
        elif i == 287:
            i = "v"
            COz2.append(i)
        elif i == 743:
            i = "y"
            COz2.append(i)
        elif i == 7433:
            i = "q"
            COz2.append(i)
        elif i == 634:
            i = "z"
            COz2.append(i)
        elif i == 785:
            i = "w"
            COz2.append(i)
        elif i == 585:
            i = "x"
            COz2.append(i)
        elif i == 693:
            i = "1"
            COz2.append(i)
        elif i == 478:
            i = "2"
            COz2.append(i)
        elif i == 884:
            i = "3"
            COz2.append(i)
        elif i == 284:
            i = "4"
            COz2.append(i)
        elif i == 25:
            i = "5"
            COz2.append(i)
        elif i == 49:
            i = "6"
            COz2.append(i)
        elif i == 405:
            i = "7"
            COz2.append(i)
        elif i == 161:
            i = "8"
            COz2.append(i)
        elif i == 11:
            i = "9"
            COz2.append(i)
        elif i == 154:
            i = "10"
            COz2.append(i)
        elif i == 224:
            i = "0"
            COz2.append(i)
        elif i == 2311:
            i = "("
            COz2.append(i)
        elif i == 22:
            i = ")"
            COz2.append(i)
        elif i == 41:
            i = "."
            COz2.append(i)
        elif i == 55:
            i = "="
            COz2.append(i)
        elif i == 440:
            i = "/"
            COz2.append(i)
        elif i == 4401:
            i = "\ "
            COz2.append(i)
        elif i == 33:
            i = "-"
            COz2.append(i)
        elif i == 22:
            i = ":"
            COz2.append(i)
        elif i == 11:
            i = ";"
            COz2.append(i)
        elif i == 5:
            i = ","
            COz2.append(i)
        elif i == 51122:
            i = " "
            COz2.append(i)
        elif i == 5224:
            i = "?"
            COz2.append(i)
        elif i == 533:
            i = "!"
            COz2.append(i)
        elif i == 5331:
            i = "_"
            COz2.append(i)

    cozum = "".join(COz2)

    print(">" * 15, cozum, "<" * 15)


Devam = 'E'

while Devam == "E" or Devam == "e":
    print("#" * 60)
    print("LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ \n\n(1) ENCRYPT/SIFRELEME (2) DECRYPT/SIFRE COZME")
   
    
    secim = input(">>>>")

    if secim == '1':
        sifrele()
    if secim == '2':
        coz()

    print(" ")
    print(" ")
    Devam = input("PRESS TO QUİT 'ENTER' OR 'E' PRESS TO CONTİNUE./ÇIKMAK İÇİN 'ENTER' DEVAM ETMEK İÇİN 'E' BASINIZ.")
    





