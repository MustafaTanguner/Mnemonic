#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import random
import math
import sys
import os
import os.path
from sozlukler import sifreleme_sozlugu, sifre_cozme_sozlugu

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
print("*" * 31, "Welcome to Mnemonic Encryption Software", "*" * 33, )
print("*" * 105)
print("*" * 31, "*********Author:Mustafa Tangüner*******", "*" * 33, )
print("*" * 105, )
print("*" * 30, "https://www.youtube.com/watch?v=pBSR3DyobIY", "*" * 30, )

print("-" * 105, )
print("")
print("")

while True:
    gelen = input("Access Code image file Path/Lütfen resim yolunu belirtiniz:")
    if os.path.isfile(gelen) and os.access(gelen, os.R_OK):
        print("Dosya var ve okunabilir")
        print("File exists and is readable")
        break
    else:
        print("Either the file is missing or not readable")
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


with open("pixel.txt", "w")as f:
    for item in semboleritemizle(veriler):
        f.write("%s" % item)

with open('pixel.txt', 'r')as f:
    sayilar = []
    Kindi = f.read()
    Kindi = Kindi.lstrip()
    Kindi = Kindi.replace(" ", "")

    q = (len(Kindi) - 100)
    w = (len(Kindi) - 500)
    e = (len(Kindi) - 50)
    r = (len(Kindi) - 86)
    f = (len(Kindi) - 15)
    t = (len(Kindi) - 22)
    y = (len(Kindi) - 55)
    u = (len(Kindi) - 12)
    o = (len(Kindi) - 155)
    p = (len(Kindi) - 123)
    a = (len(Kindi) - 55)
    s = (len(Kindi) - 58)
    d = (len(Kindi) - 99)
    n = (len(Kindi) - 66)
    g = (len(Kindi) - 77)
    h = (len(Kindi) - 11)
    j = (len(Kindi) - 22)
    k = (len(Kindi) - 7)
    l = (len(Kindi) - 42)
    z = (len(Kindi) - 66)
    x = (len(Kindi) - 112)
    c = (len(Kindi) - 33)
    v = (len(Kindi) - 47)
    b = (len(Kindi) - 18)
    i = (len(Kindi) - 29)
    m = (len(Kindi) - 59)

    tan = (q * w * e * r * t * y * u * o * p * a * s * d * n * g * h * j * k * l * z * x * c * v * b * m * i) * (
        math.factorial(1111)) * (math.factorial(999))
    sayilar.append(tan)

for kelime in sayilar:

    x = str(random.randrange(0, 1))
    print("\n\nProcessing:\İŞLEM DEVAM EDİYOR LÜTFEN BEKLEYİNİZI: " + x + ".txt'dir.\n\n")
    print("*" * 15, "İŞLEM TAMAMLANDI", "*" * 15)
    print("*" * 15, "PROCESS COMPLETED", "*" * 15)

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
    for letter in key:
        toplam = toplam + letter

    text = str(input("Text/Lütfen Şifrelenecek Metni Giriniz:"))
    text = text.lower()
    letters = [c for c in text]
    sifre = []
    for letter in letters:
        letter_as_num = sifreleme_sozlugu[letter]
        sifre.append(letter_as_num)

    tamkilit = []
    for letter in sifre:
        letter = letter * toplam
        tamkilit.append(letter)
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
            Tamkilit = Tamkilit[1:len(Tamkilit) - 1]

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
        letter_as_str = sifre_cozme_sozlugu[i]
        COz2.append(letter_as_str)

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
