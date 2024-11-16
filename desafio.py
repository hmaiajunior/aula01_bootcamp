input("Digite o seu nome: ")
salario = float(input("Entre com o seu salario: "))
bonus = float(input("Entre com o seu bônus: "))
constante_bonus = 1000

valor_bonus =  constante_bonus + salario * bonus

print(f"O usuario possui um bonus de {valor_bonus}")