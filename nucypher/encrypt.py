from umbral import config
from umbral.curve import SECP256K1
from umbral import pre
import random

import sys 

# print("note: " + sys.argv[1]) 

config.set_default_curve(SECP256K1)

from umbral import keys, signing

alices_private_key = keys.UmbralPrivateKey.gen_key()
alices_public_key = alices_private_key.get_pubkey()

alices_signing_key = keys.UmbralPrivateKey.gen_key()
alices_verifying_key = alices_signing_key.get_pubkey()
alices_signer = signing.Signer(private_key=alices_signing_key)


print("Public key: ", alices_public_key)
plaintext = b'0x2694d88b294231e27f16c1610e1250a8f7e200e3ca6d6f370263d4e97cbe2b62'
print("Plaintext: ",plaintext)
# plaintext = sys.argv[1]

ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)

print("CipherText using Nucypher pyUmbral: ", ciphertext)
