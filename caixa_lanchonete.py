PRECO_XBURGUER = 18.50
PRECO_XSALADA = 20.00
PRECO_BATATA = 10.00
PRECO_REFRI = 6.50
TAXA_ENTREGA = 5.00

qtd_xburguer = int(input("Quantidade de X-Burguer: "))
qtd_xsalada = int(input("Quantidade de X-Salada: "))
qtd_batata = int(input("Quantidade de Batata: "))
qtd_refri = int(input("Quantidade de Refri: "))
pago = float(input("Valor pago: "))

subtotal = (qtd_xburguer * PRECO_XBURGUER) + (qtd_xsalada * PRECO_XSALADA) + (qtd_batata * PRECO_BATATA) + (qtd_refri * PRECO_REFRI)

if subtotal > 100.00:
    desconto = subtotal * 0.10
else:
    desconto = 0.00

com_desconto = subtotal - desconto

if com_desconto >= 50.00:
    taxa = 0.00
else:
    taxa = TAXA_ENTREGA

total = com_desconto + taxa
troco = pago - total

print("\n=== CUPOM ===")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Taxa de entrega: R$ {taxa:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Troco: R$ {troco:.2f}")
