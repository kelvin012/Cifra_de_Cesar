### usage:
##### python run.py crypt [ chave ] [ texto que sera criptografado ]
##### python run.py decrypt [ chave ] [ texto que sera descriptografado ]
##### python run.py decrypt [ -brute (Para testar usando a chaves de 1 a 25) ] [ texto ]
##### python run.py crypt | decrypt [ chave ] [ -p (Para usar o texto da clipboard) ]
##### examples:
###### python run.py crypt 3 this is a test message
###### python run.py decrypt 3 wklv lv d whvw phvvdjh
###### python run.py decrypt brute wklv lv d whvw phvvdjh
###### python run.py crypt | decrypt 3 -p