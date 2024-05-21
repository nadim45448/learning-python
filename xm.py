# s="Programming Hero is the best"
# op=""
# res=""
# for word in s:
#     if ' ' not in word:
#         op=word+op #rp
#     else:
#         res+=op+' '
#         print(res)
#         op=''
    
    
    

def abc(func):
    def inner():
        print(" start inner function")
        func()
        print("end of inner function")

    return inner
    
    
    pass
@abc
def deco():
    print("decorator")

deco()








