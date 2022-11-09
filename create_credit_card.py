class CreditCard:  
    """consumer credit card"""
    def __init__(self, customer, bank, account, limit):
        """ create new credit card"""
        self._customer = customer  #customer name#
        self._bank = bank          #customer's bank name#
        self._account = account    #customer's account number#
        self._limit = limit        #customer's account limit#
        self._balance = 0          #customer's initial account balance = 0#
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance

    def charge(self, price):
        """charge of credit card; return true if card 
        charge processed and return false if charge is denied"""
        if price + self._balance > self._limit:
            #if charge exceed the balance limit#
            #cannot accept te charge#
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """process customer payment that reduces balance"""    
        self._balance -= amount

#### testing method####
if __name__ == '__main__':
    wallet = [ ]
    wallet.append(CreditCard('sumit kumar', 'Bank of Baroda', '929450668331', 5000))
    wallet.append(CreditCard('sumit kumar', 'paytm', '929450668331', 1000))
    wallet.append(CreditCard('sumit kumar', 'Federal Bank', '929450668331', 100))
        
    for val in range(1,17):
          
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
            
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
            
        while wallet[c].get_balance() > 150 :
            wallet[c].make_payment(150)
            print('New Balance = ', wallet[c].get_balance())
        print()