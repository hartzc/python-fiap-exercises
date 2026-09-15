entrega = float(input("Digite a distância da entrega em km: "))
chuva = input("Está chovendo? (s/n): ").lower()
while chuva not in ['s', 'n']:
    print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")
    chuva = input("Está chovendo? (s/n): ").lower()

if entrega <= 5:
    if chuva == 's':
        print("O valor da entrega é R$ 7,00")
    else:
        print("O valor da entrega é R$ 5,00")

if entrega > 5 and entrega <= 10:
    if chuva == 's':
        print("O valor da entrega é R$ 10,00")
    else:
        print("O valor da entrega é R$ 8,00")

if entrega > 10:
    if chuva == 's':
        print("O valor da entrega é R$ 12,00")
    else:
        print("O valor da entrega é R$ 10,00")    




