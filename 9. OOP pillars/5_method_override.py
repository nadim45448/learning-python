class Phone:
    def __init__(self) -> None:
        
        print("Inside phone class")

class Pixel(Phone):
    # init method of phone class is automatically come here. but we again define the init method inside this class in the following line
    # this is called method overridde.

    def __init__(self) -> None:
        super().__init__() #init method of Phone class
        
        print("Inside pixel class") #method override
        
    

pixel=Pixel()