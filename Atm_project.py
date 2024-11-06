balance = 15000
print("Welcome to Kabadi Bank ATM")

while True:
    print("\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Your balance is:", balance)
        
    elif choice == "2":
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
            continue
        else:
            balance -= amount
            print(f"{amount} has been withdrawn. Your new balance is: {balance}")
    
    elif choice == "3":
        amount = int(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid deposit amount")
            continue
        else:
            balance += amount
            print(f"{amount} has been deposited. Your new balance is: {balance}")
    
    elif choice == "4":
        print("Thank you for using Kabadi Bank ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
