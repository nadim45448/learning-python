class Phone:
    brand='apple'
    color='black'
    price='100000'
    variant=''

    def information(self):
        print(f'Color:{self.brand},color:{self.color}, price:{self.price},variant:{self.variant}')
    
    def set_info(self, variant):
        self.variant=variant
    def send_sms(self, number, text):
        sms=f'sending sms: {text} to: {number}'
        return sms
        

my_phone=Phone()
# print(my_phone.brand)
my_phone.set_info('USA')
my_phone.information()
sms=my_phone.send_sms('018121212', "I missed to miss you")
print(sms)