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

    def __init__(self, customer, bank, account, limit) -> None:
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

    def charge(self, price):
        """Charge the given price to the card.

        Args:
            price (float): The amount to charge in dollars

        Returns:
            bool: True if charge was processed, False if charge would exceed limit
        """
        if price + self.balance > self.limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Make a payment to reduce the balance.

        Args:
            amount (float): The amount to pay in dollars
        """
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """ An extension to CreditCard that compounds interst and fees"""

    def __init__(self, customer, bank, account, limit, apr) -> None:
        """Create a new predatory credit card instance.

        Args:
            customer (str): The name of the customer
            bank (str): The name of the issuing bank 
            account (str): The account identifier
            limit (float): Credit limit in dollars
            apr (float): Annual percentage rate (e.g. 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, account, limit)  # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge the given price to the card, plus fees if applicable.

        Args:
            price (float): The amount to charge in dollars

        Returns:
            bool: True if charge was processed, False if charge would exceed limit
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self.balance += 5  # assess penalty
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == '__main__':
    # Test the CreditCard class with sample usage
    # Create a wallet of credit cards
    # Process charges and payments
    # Print account summaries
    wallet = []
    wallet.append(CreditCard('John Doe', 'bank', '1234 5678 9012 3456', 2500))
    wallet.append(CreditCard('Jane Smith', 'bank',
                  '9876 5432 1098 7654', 3500))
    wallet.append(CreditCard('Bob Wilson', 'bank',
                  '1111 2222 3333 4444', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print(f'Customer = {wallet[c].customer}')
        print(f'Bank = {wallet[c].bank}')
        print(f'Account = {wallet[c].account}')
        print(f'Limit = {wallet[c].limit}')
        print(f'Balance = {wallet[c].balance}')
        while wallet[c].balance > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].balance)
        print()
