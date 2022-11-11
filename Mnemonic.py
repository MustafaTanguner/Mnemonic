#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import random
import math
import sys
import os
import os.path
from termcolor import colored
from sozlukler import sifreleme_sozlugu, sifre_cozme_sozlugu


print(colored("""

ooo        ooooo                                                                o8o            
`88.       .888'                                                                `"'            
 888b     d'888  ooo. .oo.    .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   oooo   .ooooo.  
 8 Y88. .P  888  `888P"Y88b  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b  `888  d88' `"Y8 
 8  `888'   888   888   888  888ooo888  888   888   888  888   888  888   888   888  888       
 8    Y     888   888   888  888    .o  888   888   888  888   888  888   888   888  888   .o8 
o8o        o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' 

""",'blue'))
print("*" * 31, "Welcome to Mnemonic Encryption Software",  "*" * 33,)
print("*" * 105)
print("*" * 41,"Author:@villwocki", "*" * 45, )
print("*" * 105, )
print("*" * 30, "https://www.youtube.com/watch?v=pBSR3DyobIY", "*" * 30, )

print("-" * 105, )
print("")
print("")

while True:
    gelen = input(colored("Access Code image file Path:",'cyan'))
    if os.path.isfile(gelen) and os.access(gelen, os.R_OK):
        print("File exists and is readable")
        break
    else:
        print("Either the file is missing or not readable")



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
    print("\n\nProcessing:" + x + ".txt'dir.\n\n")
    print("*" * 15, "PROCESS COMPLETED", "*" * 15)

    with open("%s.txt" % x, "w")as f:
        for item in sayilar:
            sys.set_int_max_str_digits(6000)
            f.write("%s" % item)

print(colored("Image Analysis Completed Successfully. Your Special Code:",'green'))
print(colored(sayilar,'red'))


def sifrele():
    with open('0.txt', 'r')as f:
        f_conte = f.read()
        x = int(f_conte)

    if x == x:
        key = [(x // (10 ** i)) % 10 for i in range(math.ceil(math.log(x, 10)) - 1, -1, -1)]
    toplam = 0
    for letter in key:
        toplam = toplam + letter

    text = str(input("\n\nText:"))
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
    print(colored("\n\nFile Name: " + x + ".txt'dir.\n\n",'blue'))

    with open("%s.txt" % x, "w")as f:
        for item in tamkilit:
            f.write("%s\n" % item)
    s = open("%s.txt" % x, "r")
    print(colored("ENCRYPTION MESSAGE:",'green'))
    print(colored("Your file has been successfully saved.",'green'))
    print(colored(tamkilit,'red'))


def coz():
    with open('0.txt', 'r')as f:
        f_conte = f.read()
        f_conte = f_conte.lstrip()
        f_conte = f_conte.replace(" ", "")
        x123 = int(f_conte)
    print(colored("ENCRYPT Message to file Path'",'green'))
    Metingiris = 1
    if Metingiris == 1:
        pass

    else:
        print("Feil input")
        coz()

    if Metingiris == 1:
        Tamkilit = []
        try:
            with open(input("\nPlease enter the file Path:"), "r") as f:
                for line in f:
                    Tamkilit.append(line.strip())
        except:
            print(colored("Not Found File:",'red'))
            coz()

        Coz = []
        for i in Tamkilit:
            Coz.append(int(i))
    if Metingiris == 2:
        Tamkilit = input(colored("Please enter the text to be solved:",'green'))

        if Tamkilit.isdigit():
            pass
        else:
            print(colored("Incorrect Text Entered Encrypted text cannot contain letters.Please enter again:",'red'))
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
            print(colored("WRONG KEY OR ERROR PASSWORD:key entered by message does not match:",'red'))

            coz()

    COz2 = []

    for i in Coz1:
        letter_as_str = sifre_cozme_sozlugu[i]
        COz2.append(letter_as_str)

    cozum = "".join(COz2)
    print(" ")
    print(" ")
    print(" ")
    print(colored(cozum,'green'))


Devam = 'E'

while Devam == "E" or Devam == "e":
    print(colored("\n\n(1) ENCRYPT (2) DECRYPT",'green'))

    secim = input("\n>>>>")

    if secim == '1':
        sifrele()
    if secim == '2':
        coz()

    print(" ")
    print(" ")
    Devam = input(colored("PRESS TO QUİT 'ENTER' OR 'E' PRESS TO CONTİNUE.",'blue'))
