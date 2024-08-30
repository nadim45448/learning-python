import hashlib

# hashing
# database information
email='nadim@gmail.com'
pwd='chairOnThetable'
pwd_encode=pwd.encode()
pwd_hash=hashlib.md5(pwd_encode).hexdigest()
# print(pwd_hash)

# your information
your_email='nadim@gmail.com'
your_password='chairOnThetable'
hashed_your_password=hashlib.md5(your_password.encode()).hexdigest()
if email==your_email and pwd_hash==hashed_your_password:
    print("right user")
else:
    print("wrong user")

    


#  database store: what anyone see?
hacker_email='nadim@gmail.com'
hacker_password='140bcf8c8734d207bc9b96c30aa527ae'


