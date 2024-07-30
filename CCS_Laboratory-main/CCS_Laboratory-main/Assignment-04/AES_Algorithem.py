from Crypto.Cipher import AES 
key = b'vis@gfh#kps12345'
cipher = AES.new(key,AES.MODE_EAX)
data= "vishal@gmail.com".encode()
nonce = cipher.nonce
ciphertext=cipher.encrypt(data)
print("ciphertext",ciphertext)
cipher=AES.new(key,AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print ("plaintext: ", plaintext.decode())