def inverteString(string):
    return string[::-1] #operação para inverter a leitura da string digitada


textoDigitado = input("Digite seu texto para que eu possa inverter a ordem:  \n")
textoInvertido = inverteString(textoDigitado)

print("O texto que você digitou foi:",textoDigitado,"e após a minha execução ele ficou:",textoInvertido)