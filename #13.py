#13
#(1)
menu = {
    'Americano' : '가격 : 3,000원',
    'Ice Americano' : '가격 : 3,500원',
    'Cappuccino' : '가격 : 4,000원',
    'Cafe Latte' : '가격 : 4,500원',
    'Espresso' : '가격 : 3,600원'
}
for key in menu:
    print(f'{key}: ${menu[key]}')
#(2)
selection = input('위의 메뉴중 하나를 선택하세요: ')
str(selection)

def selected(key):
    print(selection, '는', menu[selection])    
