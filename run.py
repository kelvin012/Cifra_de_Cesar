import sys
import pyperclip

alfabeto = []
alfabeto_upper = []

for i in range(ord('a'), ord('z') + 1):
    alfabeto.append(chr(i))

alfabeto2x = alfabeto[:] + alfabeto[:]

for i in range(ord('A'), ord('Z') + 1):
    alfabeto_upper.append(chr(i))

alfabeto2x_upper = alfabeto_upper[:] + alfabeto_upper[:]


def main(args):
    c = 0
    lista = []
    text_string = ''
    while c < len(args):
        lista.append(args[c])
        c += 1
    for index in range(3, len(args)):
        text_string += args[index] + ' '

    while True:
        if len(args) <= 3 or (args[3] == '-p' and len(args) > 4):
            print(
                '''   _____                            _       _       _               
  / ____|                          | |     (_)     | |              
 | |     __ _  ___  ___  __ _ _ __/ __) ___ _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__\__ \/ __| | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |  (   / (__| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|   |_| \___|_| .__/|_| |_|\___|_|   
                                             | |                    
                                             |_|                    ''')
            print('Usage: \npython run.py crypt [ chave ] [ texto que sera criptografado ]')
            print('python run.py decrypt [ chave ] [ texto que sera descriptografado ]')
            print('python run.py decrypt [ brute (Para testar usando a chaves de 1 a 25) ] [ texto ]')
            print('python run.py crypt | decrypt [ chave ] [ -p (Para usar o texto da clipboard) ]')
            break
        elif args[1] == 'decrypt' and args[2] == 'brute':
            for k in range(1, 25 + 1):
                out = decrypt(text_string, k)
                print(f'[{k}] {out}')
            break
        elif args[1] == 'crypt' and args[2] == 'brute':
            print('Metodo crypt não possui suporte para bruteforce!')
            break
        else:
            if 1 <= int(args[2]) <= 25:
                if args[3] == '-p' and len(args) <= 4:
                    if args[1] == 'crypt':
                        out = crypt(str(pyperclip.paste()).lower(), int(args[2]))
                        print(out)
                        pyperclip.copy(out)
                        break
                    elif args[1] == 'decrypt':
                        out = decrypt(str(pyperclip.paste()).lower(), int(args[2]))
                        print(out)
                        pyperclip.copy(out)
                        break
                else:
                    if args[1] == 'crypt':
                        out = crypt(text_string, int(args[2]))
                        print(out)
                        break
                    elif args[1] == 'decrypt':
                        out = decrypt(text_string, int(args[2]))
                        print(out)
                        break
            else:
                print('A chave precisa ser um numero entre 1 e 25')
                break


def crypt(texto, chave):
    mensagem_crypt = ''
    for letter in texto:
        if letter.isalpha() and letter.islower():
            pos_letra = alfabeto.index(letter)
            mensagem_crypt += alfabeto2x[pos_letra + chave]
        elif letter.isalpha() and letter.isupper():
            pos_letra = alfabeto_upper.index(letter)
            mensagem_crypt += alfabeto2x_upper[pos_letra + chave]
        else:
            mensagem_crypt += letter
    return mensagem_crypt


def decrypt(texto, chave):
    teste = texto[:]
    mensagem_decrypt = ''
    for letra in teste:
        if letra.isalpha() and letra.islower():
            pos_letra = alfabeto2x.index(letra)
            mensagem_decrypt += alfabeto2x[pos_letra - chave]
        elif letra.isalpha() and letra.isupper():
            pos_letra = alfabeto2x_upper.index(letra)
            mensagem_decrypt += alfabeto2x_upper[pos_letra - chave]
        else:
            mensagem_decrypt += letra
    return mensagem_decrypt


if __name__ == '__main__':
    sys.exit(main(sys.argv))
