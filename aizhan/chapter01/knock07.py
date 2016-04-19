x = input('Enter x: ')
y = input('Enter y: ')
z = input('Enter z: ')

def xtoki(a,b,c):
    print(str(a) + '時の' +str(b) + 'は' + str(c))
    
xtoki(x,y,z)

inp = ''

while inp != 'exit':
    inp = input('Type x or y or z for checking: ')
    if inp.lower() == 'x':
        print('x =', x)
    elif inp.lower() == 'y'.lower():
        print('y =', y)
    elif inp.lower() == 'z'.lower():
        print('z =', z)
    elif inp.lower() == 'exit':
        exit()
    else:
        print('Sorry! Wrong enter. Try x or y or z or exit')

