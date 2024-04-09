# with open('message.txt','a')as fileWrite:
#     # with open('message.txt','w')as fileWrite:
#     fileWrite.write(' again hello from me\n')

with open('message.txt','r') as fileRead:
    text=fileRead.read()
    print(text)