import sys
import pyperclip

alfabeto = []
alfabeto2x = []

for i in range(ord('a'), ord('z') + 1):
    alfabeto.append(chr(i))

alfabeto2x = alfabeto[:] + alfabeto[:]


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
            print('usage: \npython run.py crypt [ chave ] [ mensagem que sera criptografada ]')
            print('python run.py decrypt [ chave ] [ mensagem que sera descriptografada ]')
            print('python run.py crypt | decrypt [ chave ] [ -p (para pegar texto da clipbord) ]')
            break
        else:
            if int(args[2]) >= 1 and int(args[2]) <= 32:
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
                print('A chave precisa ser um numero entre 1 e 32')
                break


def crypt(texto, chave):
    mensagem_crypt = ''
    for letter in texto:
        if letter.isalpha():
            pos_letra = alfabeto.index(letter)
            mensagem_crypt += alfabeto2x[pos_letra + chave]
        else:
            mensagem_crypt += letter
    return mensagem_crypt


def decrypt(texto, chave):
    teste = texto[:]
    mensagem_decrypt = ''
    for letra in teste:
        if letra.isalpha():
            pos_letra = alfabeto2x.index(letra)
            mensagem_decrypt += alfabeto2x[pos_letra - chave]
        else:
            mensagem_decrypt += letra
    return mensagem_decrypt


if __name__ == '__main__':
    sys.exit(main(sys.argv))
