from umbral import config
from umbral.curve import SECP256K1
from umbral import pre
import random

import sys 

# print("encrypted note from api: " + sys.argv[1]) 

config.set_default_curve(SECP256K1)

from umbral import keys, signing

alices_private_key = keys.UmbralPrivateKey.gen_key()
alices_public_key = alices_private_key.get_pubkey()

alices_signing_key = keys.UmbralPrivateKey.gen_key()
alices_verifying_key = alices_signing_key.get_pubkey()
alices_signer = signing.Signer(private_key=alices_signing_key)

print("Public key: ", alices_public_key)

plaintext = b'0x2694d88b294231e27f16c1610e1250a8f7e200e3ca6d6f370263d4e97cbe2b62'

ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)

cleartext = pre.decrypt(ciphertext=ciphertext,
                        capsule=capsule,
                        decrypting_key=alices_private_key)


bobs_private_key = keys.UmbralPrivateKey.gen_key()
bobs_public_key = bobs_private_key.get_pubkey()

kfrags = pre.generate_kfrags(delegating_privkey=alices_private_key,
                            signer=alices_signer,
                            receiving_pubkey=bobs_public_key,
                            threshold=10,
                            N=20)

kfrags = random.sample(kfrags,  # All kfrags from above
                        10)      # M - Threshold

capsule.set_correctness_keys(delegating=alices_public_key,
                            receiving=bobs_public_key,
                            verifying=alices_verifying_key)
(True, True, True)

cfrags = list()                 # Bob's cfrag collection
for kfrag in kfrags:
    cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule)
    cfrags.append(cfrag)        # Bob collects a cfrag

capsule.set_correctness_keys(delegating=alices_public_key,
                            receiving=bobs_public_key,
                            verifying=alices_verifying_key)
(False, False, False)

for cfrag in cfrags:
    capsule.attach_cfrag(cfrag)

cleartext = pre.decrypt(ciphertext=ciphertext,
                        capsule=capsule,
                        decrypting_key=bobs_private_key)

print("plaintext or decrypted text using Nucypher pyUmbral: ",cleartext)