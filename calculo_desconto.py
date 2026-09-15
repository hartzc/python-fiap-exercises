idade = int(input("Digite a sua idade: "))

while True:
    estudante = input("Você é estudante? (s/n): ").lower()
    if estudante in ['s', 'n']:
        break
    else:
        print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

if idade < 18 or estudante == 's' or idade >= 60 and estudante == 'n':
    print("Você tem direito a desconto.")
else:
    print("Você não tem direito a desconto.")
