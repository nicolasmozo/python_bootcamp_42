class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return '1'#False
        if len(dir(new_account)) - 1 % 2 == 0:
            return '2'#False
        if not new_account.name or not new_account.id or not new_account.value:
            return '3'#False
        if not isinstance(new_account.id,int) or not isinstance(new_account.value,int) and not isinstance(new_account.value,float):
            return '4'#False
        z = False
        a = False
        for i in dir(new_account):
            if i.startswith('b'):
                return '5'#False
            if i.startswith('zip'):
                z = True
            if i.startswith('addr'):
                a = True
        if z == False or a == False:
            return '6'#False
        for i in self.accounts:
            if i.name == new_account.name:
                return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        if not isinstance(origin,str) or not isinstance(dest,str):
            return False
        if not isinstance(amount,int) or not isinstance(amount,float):
            return False
        if amount < 0:
            return False
        for i in self.accounts:
            if i.name == origin:
                if i.value < amount:
                    return False
        if origin == dest:
            print('valid but not fund movement')
            return True
        for i in self.accounts:
            for j in self.accounts:
                if i.name == origin and j.name == dest:
                    #credit
                    Account(origin).transfer(amount)
                    #debit
                    Account(dest).value -= amount
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
    


# a1 = Account('uno')
# Bank.add(self=Bank(), new_account=Account('uno',value=0))
# print(Bank.transfer(self=Bank(),origin='c',dest='d',amount=0))
bank = Bank()
print(bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )))