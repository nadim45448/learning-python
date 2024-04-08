def full_name(f_name, l_name):
    name=f'{f_name} {l_name}'
    return name
name=full_name(l_name="X", f_name="Mr")
# print(name)

def long_name(**kargs):
    print(kargs)

# long_name(first='Dr', last='Chowdhury', middle='Rahaman')

def name_mixed(first, last, **name_parts):
    print(first, last, name_parts)

name_mixed(first='Mr', last='X',midlle='abc')


def all_type(first, *args, **kargs):
    print(first)
    print(args)
    print(kargs)

# all_type('abc','def','ghi',first_name='nadim',middle_name='bin',last_name='hossain')

def all_type1(first, *args, **kargs):
    print(first)
    for word in args:
        print(word)
    
    for key, value in kargs.items():
        print(key, value)
    
    

all_type1('abc','def','ghi',first_name='nadim',middle_name='bin',last_name='hossain')