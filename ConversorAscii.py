import sys
maximo = len(sys.argv)
i = 0
print("\n")
print("**************************************")
print("*  CONVERSOR DE EXPRESIONES A ASCII  *")
print("**************************************")
print("by @chelo154")
print("--------------------------------------")
print("\n")
if(maximo <= 1):
    print("ERROR -Debes Ingresar expresiones para poder convertirlas a Ascii")
    print('\nEjemplo de Uso: python ConversorAscii.py "Hola" "Mundo"')
    print("\nSaliendo.... ")
    exit()
while(i < maximo):
    if(i != 0):
        print("Expresion "+str(i)+": ")      
        expresion = sys.argv[i]
        valorAscii = ''.join(str(ord(c)) for c in expresion)
        print("Valor Original: "+expresion)
        print("Valor en Ascii: "+valorAscii)
        print("")
    i=i+1
print("Expresiones Convertidas Exitosamente :D ")