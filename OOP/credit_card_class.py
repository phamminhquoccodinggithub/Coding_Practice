"""A consumer credit card.

This class represents a credit card with basic functionality like checking balance,
making charges and payments. It stores customer information, bank details, and
tracks spending limits and current balance.

Attributes:
    customer (str): The name of the customer (e.g., 'John Smith')
    bank (str): The name of the banking institution (e.g., 'Chase')
    account (str): The account identifier (e.g., '1234 5678 9012 3456') 
    limit (float): Credit limit in dollars (e.g., 2500)
    balance (float): Current balance in dollars (e.g., 325.65)
"""


class CreditCard:
    """ A conumer credit card."""

    def __init__(self, customer, bank, account, limit, balance) -> None:
        """Create a new credit card instance.

        The initial balance is zero.

        Args:
            customer (str): The name of the customer (e.g., 'John Smith')
            bank (str): The name of the bank (e.g., 'Chase') 
            account (str): The account identifier (e.g., '1234 5678 9012 3456')
            limit (float): Credit limit in dollars (e.g., 2500)
            balance (float): balance in dollars, initiation is zero
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0


    @property
    def customer(self):
        """Get the name of the customer.

        Returns:
            str: The name of the customer
        """
        return self._customer

    @property
    def bank(self):
        """Get the name of the bank.

        Returns:
            str: The name of the bank
        """
        return self._bank

    @property
    def account(self):
        """Get the account identifier.

        Returns:
            str: The account identifier
        """
        return self._account

    @property
    def limit(self):
        """Get the credit limit.

        Returns:
            float: The credit limit in dollars
        """
        return self._limit

    @property
    def balance(self):
        """Get the current balance.

        Returns:
            float: The current balance in dollars
        """
        return self._balance
