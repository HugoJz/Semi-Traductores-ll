#22 / Enero / 2023 
#Jiménez Estrada Hugo Armando  
#Materia: Seminario de Solucion de Problemas de Traductores de Lenguajes ll
#Maestro: Michel Emanuel Lopez Franco

import re

cadena = re.compile('[a-zA-Z]+[a-zA-Z]+')

identificador = re.compile('[a-zA-Z]+([a-zA-Z]+[\d])*')

real = re.compile('[\d]+\.[\d]+')

entero = re.compile('[\d]')



#Diccionario de operadores
Operadores = {'+' : 'OpSuma tipo: 5', '-' : 'OpRest tipo: 5',
              '*' : 'OpMul tipo: 6', '/' : 'OpDiv tipo: 6',
              '<' : 'OpRelac tipo: 7', '<=' : 'OpRelac tipo: 7', '>' : 'OpRelac tipo: 7', '>=' : 'OpRelac tipo 7',
              '||' : 'OpOr tipo: 8',
              '&&' : 'OpAnd tipo 9',
              '!' : 'OpNot tipo 10',
              '==' : 'OpIgualdad tipo: 11', '!=' : 'OpIgualdad tipo: 11'}
Operadores_key = Operadores.keys()

#Diccionario de palabras reservadas
Reservadas = {'if' : '19',
              'while' : '20',
              'return' : '21',
              'else' : '22',
              'int' : '4',
              'float' : '4',
              'void' : '4',
              '$' : '23'}
Reservadas_key = Reservadas.keys()

#Diccionario de simbolos
Simbolos = {';' : '12',
            ',' : '13',
            '(' : '14',
            ')' : '15',
            '{' : '16',
            '}' : '17',
            '=' : '18'}
Simbolos_key = Simbolos.keys()

linea = []

print ("\tAnalizador Lexico")
print ("\tEscriba '0' para salir del programa")
while (linea != '0'):
        linea = input("Cadena a analizar: ")
        tokens=linea.split(' ')
        print("Los tokens son ", tokens)
        
        for token in tokens:     
            if token in Operadores_key:
                print(token, "<< Es un", Operadores[token])
            elif token in Simbolos_key:
                print(token, "<< Es un simbolo del tipo:", Simbolos[token])
            elif token in Reservadas_key:
                print(token, "<< Es una palabra del tipo:", Reservadas[token])
            elif cadena.match(linea):
                print(token, "<< Es una cadena del tipo: 3")
            elif identificador.match(linea):
                print (token, "<< Es un identificador del tipo: 0")
            elif real.match(linea):
                print(token, "<< Es un real del tipo: 2")
            elif entero.match(linea):
                print(token, "<< Es un identificador del tipo: 1") 
        print("----------------------------------------------------------")

