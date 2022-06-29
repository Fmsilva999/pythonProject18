while True:
    nun = int(input('Informe um número para exibir sua tabuada [0 p/ sair]: ')) #achei mais interessante usar o zero para sair.
    if nun == 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        print(f'{nun} x {cont:2} = {nun * cont:3}')
print('Programa encerrado. Volte sempre!')