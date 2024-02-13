import random
import json

with open("C:\\PythonProjects\\Lab 4\\people_cards.json", "r") as file:
    data = json.load(file)


# cards.py
class Card:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def withdraw(self, amount):  # любое снятие денег с карточки
        self.balance -= amount

    def deposit(self, amount):  # любое пополнение карточки
        self.balance += amount

    def __str__(self):
        return f"Карта {self.number} (Баланс: {self.balance}, Лимит: {self.limit})"


class ChildCard(Card):
    def __init__(self, card_number, balance, limit):
        super().__init__(card_number, balance)
        self.limit = limit

    def __str__(self):
        return (
            f"Карта ребенка {self.number} (Баланс: {self.balance}, Лимит: {self.limit})"
        )


# people.py
class Person:
    def __init__(self, last_name, first_name, cards=[], savings_accounts=[]):
        self.last_name = last_name
        self.first_name = first_name
        self.cards = cards
        self.savings_accounts = savings_accounts

    def purchase(self, item, price):  # функция покупки товара
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
            return
        else:
            if price <= self.cards[0].balance:  # если денег хватает
                self.cards[0].withdraw(price)  # снимаем деньги с карты
                print(
                    f"{self.first_name} {self.last_name} купил(а) {item} за {price} RUB с карты {self.cards[0].card_number}"
                    )
            else:
                print(f"Ошибка. Недостаточно средств.")
                return

    def open_savings_account(
        self, amount, rate
    ):  # функция открытия накопительного счета
        if self.cards[0] is None:
            print(f"У {self.last_name} {self.first_name} нет карт.")
            return
        else:
            if amount <= self.cards[0].balance:  # если денег хватает
                savings_account = SavingsAccount(
                    balance=amount, interest_rate=rate
                )  # создаем накопительный счет
                self.savings_accounts.append(
                    savings_account
                )  # добавляем накопительный счет в список накопительных счетов конкретного человека
                self.cards[0].withdraw(amount)  # снимаем деньги с карты
                print(
                    f"{self.last_name} {self.first_name} открыл(а) накопительный счет с балансом {amount} RUB."
                )
            else:
                print("Недостаточно средств.")
                return
    def savings_account_deposit(self, amount):  # функция пополнения накопительного счета
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
        else:
            self.cards[0].withdraw(amount)  # снимаем деньги с карты
            self.savings_accounts[0].balance += amount * (
                1 + self.savings_accounts[0].interest_rate
            )  # пополняем счет на величину с учетом процентной ставки
            print(
                f"{self.first_name} {self.last_name} пополнил(а) свой накопительный счет на сумму {amount} RUB. Баланс накопительного счета: {self.savings_accounts[0].balance} RUB"
            )
    def savings_account_withdraw(
        self, amount
    ):  # функция снятия денег с накопительного счета
        if self.savings_accounts[0].balance >= amount:  # если денег хватает
            self.cards[0].deposit(amount)  # пополняем карту
            self.savings_accounts[0].balance -= amount  # снимаем деньги со счета
            print(
                f"На карту {self.cards[0].card_number} было переведено {amount} RUB. Баланс накопительного счета: {self.savings_accounts[0].balance} RUB"
            )
        else:
            print(f"Ошибка. Недостаточно средств.")

class Child(Person):
    def __init__(self, last_name, first_name, age, cards=[], savings_accounts=[]):
        super().__init__(last_name, first_name, cards, savings_accounts)
        self.age = age


class Adult(Person):
    def __init__(
        self,
        last_name,
        first_name,
        cards=[],
        savings_accounts=[],
        children=[],
        investment_accounts=[],
    ):
        super().__init__(last_name, first_name, cards, savings_accounts)
        self.children = children
        self.investment_accounts = investment_accounts

    def give(self, amount):  # функция передачи денег ребенку
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
            return
        else:
            if amount <= self.cards[0].balance:  # если денег хватает
                self.cards[0].withdraw(amount)  # снимаем деньги с карты
                self.cards[0].withdraw(amount)  # снимаем деньги с карты
                child = random.choice(
                    self.children
                )  # выбираем случайного ребенка из списка детей данного взрослого
                childcard = child.cards[0]  # выбираем карту этого ребенка из класса этого ребенка
                childcard.deposit(amount)
                print(
                    f"{self.first_name} {self.last_name} дал(а) своему ребенку {self.children[0].first_name} {self.children[0].last_name} {amount} RUB с карты {self.cards[0].card_number}"
                    )
                return

    def send(self, receiver_number, amount):  # функция перевода денег другому взрослому
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
            return
        else:
            if amount <= self.cards[0].balance:  # если денег хватает
                for person in People:  # пробегаемся по всем взрослым из файла
                    for i in range(len(person.cards)):  # пробегаемся по всем картам всех взрослых
                        if person.cards[i].card_number == receiver_number:  # если нашли нужную карту получателя
                            self.cards[0].withdraw(amount)  # снимаем деньги с карты
                            person.cards[i].deposit(amount)  # пополняем карту получателя
                            print(
                                f"{self.first_name} {self.last_name} отправил(а) {amount} RUB {person.first_name} {person.last_name} с карты {self.cards[0].card_number}"
                            )
                            return
                print(f"Карта {receiver_number} не найдена.")
                return
            else:
                print(f"Ошибка. Недостаточно средств.")

    def salary(self, amount):  # функция получения зарплаты
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
            return
        else:
            self.cards[0].deposit(amount)  # пополняем первую карту
            # Тут конечно можно реализовать перевод зарплаты на конкретную карту аналогичным образом через for card in self.cards, но я решил в этот раз так не делать
            print(
                f"{self.first_name} {self.last_name} получил(а) зарплату {amount} RUB на карту {self.cards[0].card_number}"
            )
            return

    def template(self, item, price):
        super().purchase(item, price)
        print(
            f"Выполнен обьязательный платеж и куплен {item} за {price} RUB с карты {self.cards[0].card_number}"
        )
        return

    def open_investment_account(
        self, amount
    ):  # функция открытия инвестиционного счета
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
        else:
            if amount <= self.cards[0].balance:  # если денег хватает
                investment_account = InvestmentAccount(
                    balance=amount
                )  # создаем инвестиционный счет
                self.investment_accounts.append(
                    investment_account
                )  # добавляем инвестиционный счет в список инвестиционных счетов конкретного человека
                self.cards[0].withdraw(amount)  # снимаем деньги с карты
                print(
                    f"{self.last_name} {self.first_name} открыл(а) инвестиционный счет с балансом {amount} RUB."
                )
                return
            return
    def investment_account_deposit(self, amount):  # функция пополнения накопительного счета
        if self.cards[0] is None:
            print(f"У {self.first_name} {self.last_name} нет карт.")
        else:
            self.cards[0].withdraw(amount)  # снимаем деньги с карты
            self.investment_accounts[0].balance += (
                amount  # пополняем счет на величину с учетом процентной ставки
            )
            if self.investment_accounts[0].balance >= 0:  # если баланс положительный
                self.investment_accounts[0].banned = False  # счет не заблокирован
            print(
                f"{self.first_name} {self.last_name} пополнил(а) свой инвестиционный счет на сумму {amount} RUB. Баланс инвестиционного счета: {self.investment_accounts[0].balance} RUB"
            )
    def investment_account_withdraw(
        self, amount
    ):  # функция снятия денег с накопительного счета
        if self.investment_accounts[0].banned == False:  # если счет не заблокирован
            if self.investment_accounts[0].balance >= amount:  # если денег хватает
                self.cards[0].deposit(amount)  # пополняем карту
                self.investment_accounts[0].balance -= amount  # снимаем деньги со счета
                print(
                    f"На карту {self.cards[0].card_number} было переведено {amount} RUB. Баланс инвестиционного счета: {self.investment_accounts[0].balance} RUB"
                )
            else:
                print(f"Ошибка. Недостаточно средств.")
                print(f"Баланс инвестиционного счета: {self.investment_accounts[0].balance} RUB")
        else:
            print("Счет заблокирован")

    def __str__(self):
        print(
            f"{self.first_name} {self.last_name} (Cards: {len(self.cards)}, Children: {len(self.children)})"
        )


# accounts.py


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.banned = False


class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0):
        super().__init__(balance)
        self.interest_rate = interest_rate
        self.banned = False

    def __str__(self):
        return f"Баланс накопительного счета: {self.balance} RUB"


class InvestmentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.banned = False

    def update(self):  # функция обновления баланса
        self.balance += random.randint(-500, 500)  # случайное изменение баланса
        print(f"Инвестиционный счет обновился. Баланс инвестиционного счета: {self.balance} RUB")
        if self.balance < 0:  # если баланс отрицательный
            self.banned = True  # счет заблокирован
            print(
                f"Ваш счет заблокирован из-за отрицательного баланса. Баланс: {self.balance} RUB"
            )

# main.py
def main():
    People = []
    for person in data:
        adult = Adult(
            last_name=person["last_name"],
            first_name=person["first_name"],
            cards=[],
            children=[],
        )
        for card in person["cards"]:
            cards = Card(card_number=card["number"], balance=card["balance"])
            adult.cards.append(cards)
        for child in person["children"]:
            children = Child(
                last_name=child["last_name"],
                first_name=child["first_name"],
                cards=[],
                age=child["age"],
            )
            for card in child["cards"]:
                cards = ChildCard(
                    card_number=card["number"],
                    balance=card["balance"],
                    limit=card["limit"],
                )
                children.cards.append(cards)
            adult.children.append(children)
        People.append(adult)
    return People

People = main()

Man1 = People[1]
Man2 = People[2]
Man2.give(300)
Man1.send("3554164416385571", 250)
Man1.template("Хлеб", 50)
Man2.salary(10000)
Man2.open_savings_account(5000, 10)
Man2.savings_account_deposit(300)
Man2.savings_account_withdraw(1500)
Man1.purchase("Молоко", 100)
Man2.open_investment_account(5000)
Man2.investment_account_deposit(800)
Man2.investment_account_withdraw(500)
Man2.investment_accounts[0].update()