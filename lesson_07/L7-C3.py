from datetime import datetime


class Person:

    def __init__(self, id_num: int, name: str, address: str):
        self.id_num: int = id_num
        self.name: str = name
        self.address: str = address


class Transaction:

    def __init__(self, transaction_type: str, amount: float, currency: str, rate: float | None):
        self.transaction_type: str = transaction_type
        self.amount: float = amount
        self.currency: currency
        self.rate: float | None = rate


class BankAccount:

    general_account_number: int = 1

    def __init__(self, bank_name: str, branch: str, account_holders: list[Person],
                 usd_allowed: bool, usd_balance: float = 0, nis_balance: float = 0,
                 credit_limit: float = 0):
        self.bank_name: str = bank_name
        self.branch: str = branch
        self.account_holders: list[Person] = account_holders
        self.usd_allowed: bool = usd_allowed
        if self.usd_allowed:
            self.usd_balance: float = usd_balance
        else:
            self.usd_balance: float = 0
        self.nis_balance: float = nis_balance
        self.credit_limit: float = credit_limit
        self.transactions: dict[datetime, list[Transaction]] = {}
        self.account_number: int = self.general_account_number
        BankAccount.general_account_number += 1

    def _add_to_trans_list(self, ttype, amount, currency, rate) -> None:
        if datetime.today() in self.transactions:
            self.transactions[datetime.today()].append(Transaction(ttype, amount, currency, rate))
        else:
            self.transactions[datetime.today()] = [Transaction(ttype, amount, currency, rate)]

    def deposit(self, amount: float, currency: str) -> None:
        if currency == 'usd':
            if self.usd_allowed:
                self.usd_balance += amount
                self._add_to_trans_list('deposit', amount, currency, None)
            else:
                print("Can't add USD to this account.")
        elif currency == 'nis':
            self.nis_balance += amount
            self._add_to_trans_list('deposit', amount, currency, None)
        else:
            print("Unknown currency.")

    def withdraw(self, amount: float, currency: str) -> None:
        if currency == 'usd':
            if self.usd_allowed:
                if self.usd_balance >= amount:
                    self.usd_balance -= amount
                    self._add_to_trans_list('withdraw', amount, currency, None)
                else:
                    print('Balance too low to withdraw the amount.')
            else:
                print("This account does not have a USD balance.")
        elif currency == 'nis':
            if self.nis_balance >= amount:
                self.nis_balance -= amount
                self._add_to_trans_list('withdraw', amount, currency, None)
            else:
                print('Balance too low to withdraw the amount.')
        else:
            print("Unknown currency.")

    def convert_from_usd_to_nis(self, amount: float, rate: float) -> None:
        if self.usd_balance >= amount:
            self.usd_balance -= amount
            self.nis_balance += amount * rate
            self._add_to_trans_list('convert', amount, 'usd', rate)
        else:
            print("Not enough USD in the balance.")

    def convert_from_nis_to_usd(self, amount: float, rate: float) -> None:
        if self.nis_balance >= amount:
            self.nis_balance -= amount
            self.usd_balance += amount * rate
            self._add_to_trans_list('convert', amount, 'nis', rate)
        else:
            print("Not enough NIS in the balance.")

    def get_current_balance(self) -> float:
        return self.nis_balance

    def get_transactions_per_date(self, transaction_date: datetime) -> list[Transaction]:
        if transaction_date in self.transactions:
            return self.transactions[transaction_date]
        else:
            print("No transactions occurred on this day.")

    def get_cashflow_per_month(self, month: int, year: int) -> tuple[float, float]:
        transaction_list: list[Transaction] = []
        for date_ in self.transactions:
            if date_.month == month and date_.year == year:
                transaction_list.extend(self.transactions[date_])
        income: float = 0
        outcome: float = 0
        for trans_ in transaction_list:
            if trans_.transaction_type == 'deposit':
                income += trans_.amount
            elif trans_.transaction_type == 'withdraw':
                outcome += trans_.amount
        return income, outcome
