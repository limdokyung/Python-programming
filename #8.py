#8
ident_num = int(input('주민드록번호 첫 6숫자 형식 : '))
def convert(num):
    year = 1900 + ident_num//(10**5)
    day = ident_num % 100
    