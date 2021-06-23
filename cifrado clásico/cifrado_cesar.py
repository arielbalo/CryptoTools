#!/usr/bin/python3
# -*- coding: utf-8 -*-

#CIFRADO CESAR
__author__ = "arielbalo"

import argparse

#alf = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz0123456789"
alf = ""
es = "abcdefghijklmnñopqrstuvwxyz"
en = "abcdefghijklmnopqrstuvwxyz"

def parse_args():
    parser = argparse.ArgumentParser(description="Cifrador de César.",
                                     epilog="Más información en https://github.com/arielbalo/CryptoTools/")
    parser.add_argument("-c", "--cipher", action="store_true", help="Cifrar")
    parser.add_argument("-d", "--decipher", action="store_true", help="Descifrar")
    parser.add_argument("-l", "--lang", type=str, help="Lenguage a emplear [en/es]")
    args = parser.parse_args()
    return args

def cifrar():
    print ("Cifrar un mensaje")
    texto = input("Tu texto: ").lower()
    
    k = int(input("Valor de desplazamiento: "))
    cifrad = ""
    
    for c in texto:
        if c in alf:
            cifrad += alf[(alf.index(c)+k)%(len(alf))]
        else:
            cifrad += c
            
    print("Texto cifrado: ",cifrad)

def decifrar():
    print("Aplicando fuerza bruta")
    texto = input("Mensaje: ").lower()

    for key in range(len(alf)):
        traducido = ''

        for elem in texto:
            if elem in alf:
                elemIndex = alf.find(elem)
                tradIndex = elemIndex - key

                if tradIndex < 0:
                    tradIndex = tradIndex + len(alf)
                traducido = traducido + alf[tradIndex]
            else:
                traducido = traducido + elem

            if len(traducido) == len(texto):
                print('key #{}: {}'.format(key, traducido))

def main(args):
    global alf
    if args.lang == "es":
        alf = es
    elif args.lang == "en":
        alf = en
    else:
        alf = en

    if args.cipher:
        cifrar()
    elif args.decipher:
        decifrar()
    else:
        print("\nRevise el panel de ayuda [-h]\n")

if __name__ == '__main__':
    args = parse_args()
    main(args)