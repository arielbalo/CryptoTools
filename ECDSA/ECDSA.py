#!/usr/bin/python3

from dataclasses import dataclass
from random import randint
from ECC import *

@dataclass
class Signature:
    r: int
    s: int
    
    def verify(self, z: int, pub_key: Point) -> bool:
        s_inv = pow(self.s, -1, N)  # Python 3.8+
        u = (z * s_inv) % N
        v = (self.r * s_inv) % N
        
        return (u*G + v*pub_key).x.value == self.r

@dataclass
class PrivateKey:
    secret: int
    
    def sign(self, z: int) -> Signature:
        e = self.secret
        k = randint(0, N)
        R = k * G
        r = R.x.value
        k_inv = pow(k, -1, N)  # Python 3.8+
        s = ((z + r*e) * k_inv) % N
        
        return Signature(r, s)


pub = Point(
    x=0x887387E452B8EACC4ACFDE10D9AAF7F6D9A0F975AABB10D006E4DA568744D06C,
    y=0x61DE6D95231CD89026E286DF3B6AE4A894A3378E393E93A0F45B666329A0AE34,
    curve=secp256k1
)

# Caso 1: Verificando autenticidad
z = 0xEC208BAA0FC1C19F708A9CA96FDEFF3AC3F230BB4A7BA4AEDE4942AD003C0F60
r = 0xAC8D1C87E51D0D441BE8B3DD5B05C8795B48875DFFE00B7FFCFAC23010D3A395
s = 0x68342CEFF8935EDEDD102DD876FFD6BA72D6A427A3EDB13D26EB0781CB423C4

try:
    assert Signature(r, s).verify(z, pub)
    print("Correcta verificaión de autenticidad.")
except:
    print("Problemas en la verificación de autenticidad.")

# Caso 2: Verificando autenticidad para diferente firma hacha con el mismo P
z = 0x7C076FF316692A3D7EB3C3BB0F8B1488CF72E1AFCD929E29307032997A838A3D
r = 0xEFF69EF2B1BD93A66ED5219ADD4FB51E11A840F404876325A1E8FFE0529A2C
s = 0xC7207FEE197D27C618AEA621406F6BF5EF6FCA38681D82B2F06FDDBDCE6FEAB6

try:
    assert Signature(r, s).verify(z, pub)
    print("Correcta verificación de autenticidad con diferentes firmas del mismo punto.")
except:
    print("Problemas en la verificación de autenticidad con diferentes firmas del mismo punto.")

# Caso 3: Firma y verificación
e = PrivateKey(randint(0, N))  # genera una clave privada aleatoria
pub = e.secret * G  # clave (punto) pública correspondiente a e
z = randint(0, 2 ** 256)  # generar mensaje aleatorio, en la práctica hash de 256bits del mensaje
signature: Signature = e.sign(z)

try:
    assert signature.verify(z, pub)
    print("Prueba satisfactoria de firma y verificación.")
except:
    print("Problemas en la firma y verificación.")
