s = 'Hacktiv-PTP Python for DS'
a = [100,200,300]

def foo(arg):
    print(f'arg = {arg}')
    
class Foo:
    pass



if (__name__ == '__main__'):
    print('Exceuting as standalone ')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)

