#as7-2
class BankAccount:
    def __init__(self, name, account_num, balance = 0):
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance
    def __str__(self):
        return f"{self.__name}님의 계좌 {self.__account_num}의 잔고는 {self.__balance}원 입니다."
    def set_name(self, name):
        self.__name = name
    def set_account_num(self, account_num):
        self.__account_num = account_num
    def set_balance(self, balance):
        self.__balance = balance
    def get_name(self):
        return self.__name
    def get_account_num(self):
        return self.__account_num
    def get_balance(self):
        return self.__balance
    def deposit(self, money):
        if money > 0:
            self.__balance += money
        return print(f"{money}원이 입금되었습니다. 잔고는 {self.__balance}입니다.")
    def withdraw(self, money):
        if self.__balance < money:
            return print(f"계좌 잔고는 {self.__balance}원으로 인출 요구 금액 {money}원보다 작습니다.")
        else:
            self.__balance -= money
            return print(f"{money}원이 인출되었습니다. 잔고는 {self.__balance}입니다.")
   
def main():
    account1 = BankAccount('홍길동', '1234-0001')
    print(account1)

    account1.deposit(2000)
    print(account1)

    account1.withdraw(500)
    print(account1)

    account1.withdraw(5000)
main()