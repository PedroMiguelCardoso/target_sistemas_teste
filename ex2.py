def fibonacci(num):            #Definindo a função fibonacci
    x, y = 0, 1    #inicializando as variáveis com seus valores correspondentes 
    while y < num: #criando a estrutura de repetição que será utilizada enquanto y for menor que num
        x, y = y, x + y             #escrevendo a sequência de fibonacci
        if y == num:                
            return True             #se y for igual a num o valor retornado sera True
    return False

numeroTeste = int(input("Digite o número desejado para que eu possa testar se ele pertence a sequência de Fibonacci: ")) #Solicitando que o usuário escolha um número para realizar o teste

if fibonacci(numeroTeste):
    print("O número", numeroTeste, "pertence à sequência de Fibonacci.")           
else: 
    print("O número", numeroTeste, "não pertence à sequência de Fibonacci.")             #possíveis resultados que serão mostrados variando de acordo com o número escolhido
