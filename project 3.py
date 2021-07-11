import hashlib, uuid
salt = uuid.uuid4().hex
password = ('Sample_Password')
hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
print(hashed_password)