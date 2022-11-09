class Customer:
    
    def __init__(self, name, identity, account):
        self.custName = name
        self.custID = identity
        self.custAccNo = account
        
    def display(self):
        print('customer name: ', self.custName)
        print('customer ID: ', self.custID)
        print('customer account No. : ', self.custAccNo)
        
#Driver code#
name  =    input('Enter Customer Name: ') 
identity = input('Enter Customer Identification No: ')
account =  input('Enter Customer Account Number: ')
    
customer = Customer(name, identity, account)
customer.display()
    