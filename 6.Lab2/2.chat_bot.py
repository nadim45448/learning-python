""" chatbot
steps:
1. input/listen
2. process/decide
3. ooutput/talkback """


greet_words=['hi','hello','yo']
bye_words=['bye','tata', 'see you letter']
bad_word=['dog','pocha','dustu']

def listen():
    return input('Say something: ')

def decide(command):
    # print(command)
    command=command.lower()
    broken_words=command.split(" ")
    # print(broken_words)
    for word in broken_words:
        if word in greet_words:
            talkback("Holaaa!")
            break
        elif word in bye_words:
            talkback("bye tata....")
            break
        elif word in bad_word:
            talkback('You are a bad guy. Behave yourself')
    

   

def talkback(response):
    print(response)
   

while True:

    command=listen()
    decide(command)