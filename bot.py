nome = input("Oi! Eu sou a SereiA. Qual o seu nome? ")
print(f"Que nome bonito... É um prazer te conhecer, {nome}! ")

idade = int(input(f"Quantos anos você tem, {nome}?"))
bot_idade = 3
diferenca_idade = 0

if idade > bot_idade:
    diferenca_idade = idade - bot_idade
    print(f"Uau! Você tem {diferenca_idade} anos a mais do que eu! Eu tenho apenas {bot_idade} anos, sabia? ")
else:
    diferenca_idade = bot_idade - idade
    print(f"Nossa, sou mais velha que você, haha! Estou crescendo, já tenho {bot_idade} anos, sabia? ")

cor = input("Qual sua cor favorita? ")
print(f"Ah, {cor} é uma cor linda! Deve combinar bastante com você. ")

hobby = input("Eu adoro estudar no meu tempo livre. O que você gosta de fazer? ")
estudar = "estudar"

if estudar not in hobby:
    print("Tenho certeza de que isso é super divertido também! ")
else:
    print("Sério? Outra pessoa que adora estudar?")
    print("Sabia que tem uma página que me ensinou muito sobre direitos trans no Brasil? Adorei estudar por ela, vou te mandar aqui, olha. ")
    print("senacscs.github.io/t2/domi/segundo/sereia/")