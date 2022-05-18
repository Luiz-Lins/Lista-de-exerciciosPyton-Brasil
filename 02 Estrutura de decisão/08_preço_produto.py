
produto1 = float(input('Qnt custa o produto A: '))
produto2 = float(input('Qnt custa o produto B: '))
produto3 = float(input('Qnt custa o produto C: '))

if produto1 < produto2 and  produto1 < produto3:
    print(f' Sugiro comprar o produto A que é o de menor preço R${produto1}')
elif produto2 < produto1 and  produto2 < produto3:
    print(f' Sugiro comprar o produto B que é o de menor preço R${produto2}')
elif produto3 < produto1 and  produto3 < produto2:
    print(f' Sugiro comprar o produto C que é o de menor preço R${produto3}')