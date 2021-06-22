#!/usr/bin/python3
# -*- coding: utf-8 -*-

#CIFRADO CESAR
__author__ = "arielbalo"

import argparse

# Variables globales
alf = ""
es = "abcdefghijklmnñopqrstuvwxyz"
en = "abcdefghijklmnopqrstuvwxyz"
myKey = "cifradodesustitucionpolialfabeticavinegere"

def parse_args():
    parser = argparse.ArgumentParser(description="Cifrador de Vigenere.",
                                     epilog="Más información en https://github.com/arielbalo/CryptoTools/")
    parser.add_argument("-c", "--cipher", action="store_true", help="Cifrar")
    parser.add_argument("-d", "--decipher", action="store_true", help="Descifrar")
    parser.add_argument("-l", "--lang", type=str, help="Lenguage a emplear [en/es]")
    args = parser.parse_args()
    return args

def vinegere(accion):
    mensaje = input("Escriba el mensaje: ")
    
    traducido = []
    indice_clave = 0

    for symbol in mensaje:
        num = alf.find(symbol.lower())
        if num != -1:
            if accion == 'cifrar':
                num += alf.find(myKey[indice_clave])
            elif accion=='decifrar':
                num -= alf.find(myKey[indice_clave])
            num %= len(alf)
            
            if symbol.isupper():
                traducido.append(alf[num].upper())
            elif symbol.islower():
                traducido.append(alf[num])
            
            indice_clave += 1
            
            if indice_clave == len(myKey):
                indice_clave = 0
        else:
            traducido.append(symbol)
    return ('').join(traducido)

    

def main(args):
    global alf
    if args.lang == "es":
        alf = es
    elif args.lang == "en":
        alf = en
    else:
        alf = en
    
    if args.cipher:
        print(vinegere('cifrar'))
    elif args.decipher:
        print(vinegere('decifrar'))
    else:
        print ("\nRevise el panel de ayuda [-h]\n")
    

if __name__ == '__main__':
    args = parse_args()
    main(args)