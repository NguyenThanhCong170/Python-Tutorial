w = int(input('What is your weight: '))
change = input('(G)gam or (KG)kilogram: ')
if change.upper() == "G":
    m = w/1000
    print(f'so gam cua ban la {m}')
else:
    m = w * 1000
    print(f'so kilogam cua ban la {m}')



