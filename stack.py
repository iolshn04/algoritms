def greet(name):
    print('hello, ' + name + '!')
    greet2(name)
    print('getting ready to say bуе...')
    bуе()


def greet2(name):
    print("how are you, " + name + '?')


def bуе():
    print("ok bye!")
    

if __name__ == '__main__':
    greet('Ivan')