

mb = float(input('Qual o tamanho do arquivo para download: '))
mbps = float(input('Qual a velocidade da internet em Mbps: '))
mb_total = mb * 8

segundos = int(mb_total / mbps)

minutos = int(segundos / 60)

print(f'Será necessário aproximadamente {segundos} segundos ou {minutos} minutos para concluir download')

