import hashlib
message=str(input("Enter the string :"))
msg=hashlib.md5(b'message')
msg_digest=msg.hexdigest()
print("The MD5 message is:",msg_digest)
msg1=hashlib.sha1(b'message')
msg1_digest=msg1.hexdigest()
print("The SHA1 message is:",msg1_digest)