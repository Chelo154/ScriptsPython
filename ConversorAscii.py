import sys
i = 0
expresion = sys.argv[1]
valorAscii = ''.join(str(ord(c)) for c in expresion)
print("Valor en Ascii: "+valorAscii)

