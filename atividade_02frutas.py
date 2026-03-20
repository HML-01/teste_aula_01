# Exercício 1:
'''
with open ('frutas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Morango\n")
    arquivo.write("Melancia\n")
    arquivo.write("Abacaxi\n")
    arquivo.write("Manga\n")
    arquivo.write("Mamão\n")

with open ('frutas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip_())
'''
# Exercício 2:
'''
usuario = input("Digite os itens para adicionarmos na sua lista de compras ou 'sair', quando quiser sair:")

while usuario!="sair":
    with open ('compras.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(usuario)
        arquivo.write("\n")
    
    usuario = input("Digite os itens para adicionarmos na sua lista de compras ou 'sair', quando quiser sair:")
    
with open ('compras.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
'''
# Exercício 3:
'''
usuario= input("Digite uma anotação:")

from datetime import datetime
agora = datetime.now().strftime('%d/%m/%Y %H:%M')

with open ('diario.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(agora + "  ---  " + usuario + "\n")

with open('diario.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
'''
# Outro modo de fazer:
'''
usuario= input("Digite uma anotação:")

while usuario!="sair":
    from datetime import datetime
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    with open ('diario.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(agora + "  ---  " + usuario + "\n")
    usuario= input("Digite uma anotação:")

with open('diario.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
'''
# Exercício 4:

