import sys

if len(sys.argv)==4:
    print(f'Primer parametro:{sys.argv[1]}')
    print(f'Segundo parametro:{sys.argv[2]}')
    print(f'Tercer parametro:{sys.argv[3]}')
else:
    print('Error: solo se admite hasta 3 parametros')
