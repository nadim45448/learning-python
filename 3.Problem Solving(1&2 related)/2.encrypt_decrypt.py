""" Encrypt the following data so that no one can know your strateggy
 """
data="firebaby"
shift=3

output=""
new=""
#encryption
for character in data:
    output+=chr(((ord(character)+shift-97)%26+97))
print(output)

#decryption
for character in output:
    new+=chr(((ord(character)-shift-97)%26+97))
print(new)
