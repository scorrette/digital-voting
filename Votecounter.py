# -*- coding: utf-8 -*-


import os
import binascii
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode,b64decode



def vote_Counter():
    
    ver_signature = ver_Signature()
    
    if (ver_signature):
        dec_ballot = dec_Ballot()
        
        

def ver_Signature():
    
         ######## Receive Public key from Authenticator ##########
    auth_public_key = RSA.importKey(open('auth_public_key.pem').read())
          
                ###### Receive Signature from Authenticator #######
    #open signature file
    with open("signature.txt", "rb") as f:
        signature = f.read()
        
    #Decrypt the ballot and then find hash of it
    dec_ballot = dec_Ballot()
    
    #create hash of the decrypted ballot
    hash = SHA256.new(dec_ballot)
       
    ##################### VERIFYING SIGNATURE ################################ 
    verifier = PKCS115_SigScheme(auth_public_key) 
    try: 
       verifier.verify(hash, signature)
       print("Signature is valid.")
       return True
    except: 
       print("Signature is invalid.")
       return False
    

def dec_Ballot():
    #Using vote counter's private key, decrypt the ballot
    with open("enc_ballot.ballot", "rb") as f:
        ballot = f.read()
    counter_private_key = RSA.importKey(open('counter_private_key.pem').read())
    counter_cipher = PKCS1_OAEP.new(counter_private_key)
    plain_ballot  = counter_cipher.decrypt(ballot)
    
    return(plain_ballot)
  
       
#main test
vote_Counter()