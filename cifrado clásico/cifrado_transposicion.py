#!/usr/bin/python3
# -*- coding: utf-8 -*-

#CIFRADO CESAR
__author__ = "arielbalo"

import argparse
import math

def parse_args():
    parser = argparse.ArgumentParser(description="Cifrador de Vigenere.",
                                     epilog="Más información en https://github.com/arielbalo/CryptoTools/")
    parser.add_argument("-c", "--cipher", action="store_true", help="Cifrar")
    parser.add_argument("-d", "--decipher", action="store_true", help="Descifrar")
    parser.add_argument("-f", "--force", action="store_true", help="Aplicar fuerza bruta")
    parser.add_argument("-l", "--lang", type=str, help="Lenguage a emplear [en/es]")
    args = parser.parse_args()
    return args

def encrypt(key, message):
    print('Cifrando el mensaje...')
    cipherText = [''] * key
    for i in range(key):
        index = i
        while index < len(message):
            cipherText[i] += message[index]
            index += key
    return ''.join(cipherText)

def decrypt(key, message):
    print('Decifrando el mensaje...')
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadeBoxes = (numCols * numRows) - len(message)
    plainText = [''] * numCols
    col = row = 0
    
    for i in message:
        plainText[col] += i
        col += 1
        
        if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadeBoxes):
            col = 0
            row += 1
    return ''.join(plainText)

def brute_force(message):
    print('Aplicando fuerza bruta...')
    keys = range(1,len(message))
    for key in keys:
        numCols = math.ceil(len(message) / key)
        numRows = key
        numShadeBoxes = (numCols * numRows) - len(message)
        plainText = [''] * numCols
        col = row = 0
    
        for i in message:
            plainText[col] += i
            col += 1
        
            if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadeBoxes):
                col = 0
                row += 1
        plainText.insert(0, f'[key: {key}] -> ')
        print(''.join(plainText))
    return
    
def main(args):
    message = input('Mensaje: ')
    if not args.force:
        key = int(input(f'Llave [2-{len(message)-1}]: '))
    print()
    
    if args.cipher:
        print(f"El mensaje cifrado es: {encrypt(key, message)}\n")
    elif args.decipher and args.force:
        brute_force(message)
        print()
    elif args.decipher:
        print(f"El mensaje en claro es: {decrypt(key, message)}\n")
    else:
        print ("\nRevise el panel de ayuda [-h]\n")
    

if __name__ == '__main__':
    args = parse_args()
    main(args)