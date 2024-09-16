class Atm:
    def __init__(self):

        self.pin=""
        self.balance= 10000
        self.menu()
        
        
    def menu(self):
        user_value= input("""\n Welcome to ATM simulator! \n
            How can I help you today?\n
            Press 1 o create pin
            press 2 to change pin
            press 3 to check balance
            press 4 to withdraw Amount
            press anything else to exit
            """)
        if user_value == "1":
            #Create Pin
            self.create_pin()
        elif user_value == "2":
            #change pin
            self.change_pin()
        elif user_value == "3":
            #check balance
            self.check_balance()
        elif user_value == "4":
            #Withdraw money
            self.withdraw_money()
        else:
            exit()
            
        #Creating methods for the above 
    def create_pin(self):
        
        input_pin = int(input("Enter 4 digit number to set up your ATM pin: "))
        if len(str(input_pin)) == 4:
            self.pin =input_pin 
            print("Pin Created sucessfully")
        else:
            print("Invalid Pin, enter 4 digits pin")
        self.menu()  
        
        
        
    def change_pin(self):
        
        old_pin = int(input("Enter your 4 digit ATM pin: "))
        
        if self.pin == old_pin:
            new_pin = int(input("Enter 4 digit number to set up your new ATM pin: "))
            print(new_pin)
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Invalid Pin")
        self.menu()
        
        
    def check_balance(self):
        enter_pin = int(input("Enter your 4 digit ATM pin: "))
        if enter_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Invalid Pin")
            
        self.menu()
        
    def withdraw_money(self):
        enter_pin = int(input("Enter your 4 digit ATM pin: "))
        if enter_pin == self.pin:
            enter_amount= int(input("Enter your amount you want to withdraw: "))
            if enter_amount <= self.balance:
                self.balance -= enter_amount
                print(f"Your current balance is: {self.balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")
            
        self.menu()    
            
        
        

obj = Atm()