class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"rs{amount} deposited successfully...")
        else:
            print("Invalid deposit amount!!!!")

    def withdraw(self,amount):
        try:
            if amount<=0:
                raise ValueError("withdrawal amount must be positive!!") 

            if amount % 100!=0:
                raise ValueError("Withdrawal amount must be multiple of Rs 100 and 500")
            if amount > self.balance:
                raise ValueError("Insufficient Balance!!!")
            
            self.balance -=amount
            print(f"rs{amount} withdrawn successfully....")
        except ValueError as e:
            print(f"Withdrawal Error: {e} !!!")

    def check_balance(self):
        print(f"Current Balance : {self.balance}")

def main():
    atm = ATM()

    while True:
        print("\n=====ATM=====")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Exit")

        choice = input("choose an option (1-4):")

        if choice == '1':
            amount = int(input("Enter the amount to deposit: rs"))
            atm.deposit(amount)
        elif choice == '2':
            amount = int(input("Enter the amount you want to withdraw: rs"))
            atm.withdraw(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            print("Thanks for your kind visit...")
        else:
            print("Invalid operation!!!")

if __name__== "__main__":
    main()

