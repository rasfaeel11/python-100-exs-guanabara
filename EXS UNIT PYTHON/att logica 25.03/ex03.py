# Pedro Florencio, Rafael Melo, William Santos
#25/03/25
#variaveis e mudanças de variaveis
nome = str(input("digite seu nome"))
sobrenome = str(input("digite seu sobrenome"))
sobrenome2 = str(input("digite seu terceiro nome"))
idade = int(input("digite sua idade"))
altura = float(input("digite sua altura"))
print("Seu nome é ", nome.capitalize(), sobrenome.capitalize(), sobrenome2.capitalize(), "voce tem ", idade, " anos e sua altura e ", altura, "M e seu e-mail é ", nome.lower() + "." + sobrenome.lower() + ("@souunit.com.br") )
sobrenome = sobrenome.replace(sobrenome, sobrenome2)
print ("sua segunda opcao de e-mail é: ", nome.lower() + "." + sobrenome.lower() + "@souunit.com.br")
# primeiro o sistema voltou as variaveis postas pelo usuario e depois fez uma concatenacao juntando as variaveis "nome" e "sobrenome" junto com uma string  predifinida, fazendo o e-mail do usuario
