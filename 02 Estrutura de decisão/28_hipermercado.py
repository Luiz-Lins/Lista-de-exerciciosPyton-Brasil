
carne_comprada = float(input('Qual tipo de carne comprada? Digite 1 File Duplo; Digite 2 Alcatra; Digite 3 Picanha;'))
qnt_comprada = float(input('Qual quantidade comprada: '))
cardtabajara = input('pagamento no cartão tabajara s/n: ')

if carne_comprada == 1 and qnt_comprada < 5:
    price_total = qnt_comprada * 4.9
elif carne_comprada == 1 and qnt_comprada > 5:
    price_total = qnt_comprada * 5.80
elif carne_comprada == 2 and qnt_comprada < 5:
    price_total = qnt_comprada * 5.9
elif carne_comprada == 2 and qnt_comprada > 5:
    price_total = qnt_comprada * 6.80
elif carne_comprada == 3 and qnt_comprada < 5:
    price_total = qnt_comprada * 6.9
elif carne_comprada == 3 and qnt_comprada > 5:
    price_total = qnt_comprada * 7.80

price2 = price_total

if cardtabajara == 1:
    price2 = price_total * 0.95

if carne_comprada == 1:
    carne_comprada2 = 'File Duplo'
elif carne_comprada == 2:
    carne_comprada2 = 'alcatra'
else:
    carne_comprada2 = 'Picanha'

print('cupom fiscal') 
print(f' Sua compra foi do tipo de carne {carne_comprada2}, quantidade {qnt_comprada}Kg, preço total de R${price_total}, valor a pagar com o desconto será de R${price2} ')
    
