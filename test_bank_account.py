import unittest

from bank_account import BankAccount, MinimumBalanceAccount

class AccountBalanaceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_yangu = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_yangu.balance, 3000, msg='Account Balance Invalid.')

    def test_deposit(self):
        self.account_yangu.deposit(4000)
        self.assertEqual(self.account_yangu.balance, 7000, msg='Deposit Method Inaccurate.')

    def test_withdraw(self):
        self.account_yangu.withdraw(500)
        self.assertEqual(self.account_yangu.balance, 2500, msg='Withdraw method Inaccurate.')

    def test_invalid_transaction(self):
        self.assertEqual(self.account_yangu.withdraw(6000), "Invalid Transaction", msg='Invalid Transaction.')

    def test_sub_class(self):
        self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='Not True subclass of Balance Account.')
