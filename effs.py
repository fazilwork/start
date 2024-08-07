class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} пополнено на счет. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств для снятия.")
        elif amount > 0:
            self.balance -= amount
            print(f"{amount} снято со счета. Текущий баланс: {self.balance}")
        else:
            print("Сумма снятия должна быть положительной.")

    def display_balance(self):
        print(f"Текущий баланс счета {self.account_number}: {self.balance}")

# Пример использования класса
account = BankAccount(account_number="12345678", account_holder="Иван Иванов", balance=1000)

# Пополнение счета
account.deposit(500)

# Снятие средств
account.withdraw(300)

# Попытка снять больше средств, чем есть на счете
account.withdraw(1500)

# Отображение текущего баланса
account.display_balance()
