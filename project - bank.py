class Bank:
     Bank_name = "Indian Bank"
     Branch = "Coimbatore"
     def __init__(self,name,balance,pin):
          self.name = name
          self.balance = balance
          self.__pin = pin
          self.transaction = []
     def check_pin(self,pin):
          return self.__pin == pin
     def deposit(self,amount):
          self.balance+=amount
          self.transaction.append(f"Deposited ₹{amount}")
          print("Deposited:",amount)
     def withdraw(self,amount,pin):
          if not self.check_pin(pin):
               print("Incorrect pin")
               return
          if amount>self.balance:
               print("Insufficient Balance")
               return
          self.balance-=amount
          self.transaction.append(f"withdrawn ₹{amount}")
          print("withdrawn:",amount) 
     def show_balance(self,pin):
          if self.check_pin(pin):
               print("\n--------Account details----------")
               print("Name",self.name)
               print("Balance",self.balance)
     def show_transaction(self,pin):
          if self.check_pin(pin):
               print("\n---------Transaction History---------") 
               for t in self.transaction:
                    print("-",t)
          else:
               print("Incorrect pin")
# ---------------- TEST ----------------
acc1 = Bank("Abhi", 1000, 1234)

acc1.deposit(500)
acc1.withdraw(300, 1234)

acc1.show_balance(1234)
acc1.show_transaction(1234)       