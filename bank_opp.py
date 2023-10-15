# Bank_Project_with_oop
class ATM():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balanced = 0
    

    def deposit(self, amount):
        self.amount = amount
        self.balanced += self.amount
        print(f"The operation is done \n Acount Balance has been update : $ {self.balanced}")

    
    
    
    def withdraw(self,amount): 
        self.amount = amount
        if self.amount < self.balanced:
            self.balanced -= self.amount
            print(f"The operation is done \n Acount Balance has been update : ${self.balanced}")
        else:
            print("You not have enough money")
            option = input("If you want to borrow money enter : yes \n")
            if option == "yes":
                num_of_money = int(input("Enter the number of money you want: \n"))
                self.balanced -=num_of_money
                print(f"the operation is done you are indebted to the bank with { -1 * self.balanced }")
            else:
                print("you input worng text please repeat the operation")
            
            
                
            

                


    def view_balance(self):
        print(f"Name is : {self.name} \nAge is : {self.age} \n")
        print(f"Acount Balance is : $ {self.balanced}")


