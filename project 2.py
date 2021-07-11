#import hashlib

#print (hashlib.algorithms_guaranteed)

import hashlib

message = "Deepanshu Jain".encode()

print("MD5:", hashlib.md5(message).hexdigest())

print("BLAKE2c:", hashlib.blake2s(message).hexdigest())

print("BLAKE2b:", hashlib.blake2b(message).hexdigest()) 