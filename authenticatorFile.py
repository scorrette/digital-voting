from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode,b64decode
import mysql.connector

def authenticator(message):
    auth_key = RSA.generate(4096,e=65537)
    auth_private_key = auth_key.exportKey("PEM")
    auth_public_key = auth_key.publickey().exportKey("PEM")
    auth_cipher = PKCS1_OAEP.new(auth_key)
    plainMessage = auth_cipher.decrypt(message)
    [id_byte,cipherVote_2] = message.split(b',,,,,')
    userID = id_byte.decode("utf-8")
    mydb = mysql.connector.connect(
        host = 'ss3010.rutgers-sci.domains',
        user = 'ssrutge4_user1',
        password = "yourpassword",
        database = 'ssrutge4_ECE424'
    )
    dbCursor = mydb.cursor()
    queryString = "select has_registered from Employees where id = " + userID
    dbCursor.execute(queryString)
    result = dbCursor.fetchone()
    if result[0] == "True":
        dbCursor.close()
        mydb.close()
        raise Exception("User Already Voted")
    else:
        #pass cipherVote_2 to Counter
        queryString = "update Employees set has_registered = True where id = " + userID
        dbCursor.execute(queryString)
        dbCursor.close()
        mydb.close()
        signature = b64encode(RSA.sign(cipherVote_2,auth_private_key),"SHA-512")
        auth_cipher = PKCS1_OAEP.new(getKey())
        cipherVote_3 = auth_cipher.encrypt(cipherVote_2)
        return [cipherVote_3,signature]

def getKey():
    new_key = RSA.generate(4096,e=65537)
    private_key = new_key.exportKey("PEM")
    public_key = new_key.publickey().exportKey("PEM")
    return public_key

def mainTest():
    new_key = RSA.generate(1024,e=65537)
    private_key = new_key.exportKey("PEM")
    public_key = new_key.publickey().exportKey("PEM")
    auth_cipher = PKCS1_OAEP.new(new_key)
    cipherVote = auth_cipher.encrypt("vote".encode("utf-8"))
    ID = "123123,,,,,".encode("utf-8")
    message = ID + cipherVote
    [id_byte,cipherVote_2] = message.split(b',,,,,')
    print(id_byte.decode("utf-8"),"\n")
    auth_cipher = PKCS1_OAEP.new(new_key)
    plainVote = auth_cipher.decrypt(cipherVote_2)
    print(plainVote.decode("utf-8"), "\n")

def main():
    print("lol")

if __name__ == "__main__":
    main()