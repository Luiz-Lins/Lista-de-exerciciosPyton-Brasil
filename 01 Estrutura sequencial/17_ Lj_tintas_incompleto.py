import math

area_a_ser_pintada = float(input('area a ser pintada: '))
area_folga= area_a_ser_pintada * 1.1
cobertura_de_tinta = 6 * 18
lata_tinta = 18
valor_lata = 80

qnt_necessaria = math.ceil(area_folga / cobertura_de_tinta)
print(qnt_necessaria)
print(qnt_necessaria * valor_lata)

cobertura_do_galao = 6 * 3.6
galao_tinta = 3.6
valor_galao = 25

qnt_necessaria = math.ceil(area_folga / cobertura_do_galao)
print(qnt_necessaria)
print(qnt_necessaria * valor_galao)

qnt_necessaria1 = math.floor(area_folga / cobertura_de_tinta)
print(qnt_necessaria1)

qnt_falta = qnt_necessaria1 % area_folga
print(qnt_falta)