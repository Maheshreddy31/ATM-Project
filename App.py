bank = {
    201: ["Mahesh Reddy", "2408", 10000, [31, 10, 2002]],
    202: ["vikram", None, 20000, [23, 9, 2005]],
    203: ["vignesh", "9876", 0, [11, 1, 1900]]
}
while True:
    print("Choose the required option: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini statement")
    print("5. Exit")
    
    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if n == 1:
        print("******************************")
        print("Withdraw")
        accno = int(input("Enter your account number: "))
        if accno not in bank:
            print("Invalid Account number")
        else:
            print(f"Welcome {bank[accno][0]}")
            pin = input("Enter your Pin: ")
            if pin != bank[accno][1]:
                print("Invalid Pin")
            else:
                amt = int(input("Enter amount to withdraw: "))
                if amt > bank[accno][2]:
                    print("Insufficient Balance")
                else:
                    bank[accno][2] -= amt
                    print("Withdraw Successful")
        print("******************************")
    elif n == 2:
        print("******************************")
        print("Deposit")
        accno = int(input("Enter your account number: "))
        if accno not in bank:
            print("Invalid Account number")
        else:
            print(f"Welcome {bank[accno][0]}")
            pin = input("Enter your Pin: ")
            if pin != bank[accno][1]:
                print("Invalid Pin")
            else:
                amt = int(input("Enter amount to Deposit: "))
                bank[accno][2] += amt
                print("Deposit Successful")
        print("******************************")
    elif n == 3:
        print("******************************")
        print("Pin Generation")
        accno = int(input("Enter your account number: "))
        if accno not in bank:
            print("Invalid Account number")
        else:
            print(f"Welcome {bank[accno][0]}")
            if bank[accno][1] is not None:
                print("Pin already generated")
            else:
                print("Verify Date of Birth: ")
                date = int(input("Enter Birth Date: "))
                month = int(input("Enter Birth Month: "))
                year = int(input("Enter Birth Year: "))
                if [date, month, year] == bank[accno][3]:
                    pin = input("Enter your new Pin: ")
                    cpin = input("Confirm your Pin: ")
                    if pin != cpin:
                        print("Pins do not match, try again")
                    else:
                        bank[accno][1] = pin
                        print("Pin Generated Successfully!")
                else:
                    print("Incorrect Date of Birth Details. Try again!")
        print("******************************")
    elif n == 4:
        print("******************************")
        print("Mini statement")
        accno = int(input("Enter your account number: "))
        if accno not in bank:
            print("Invalid Account number")
        else:
            print(f"Welcome {bank[accno][0]}")
            pin = input("Enter Your Pin: ")
            if pin != bank[accno][1]:
                print("Invalid Pin")
            else:
                print(f"Balance: {bank[accno][2]}")
        print("******************************")
    elif n == 5:
        print("******************************")
        print("Thank You")
        print("Visit Again")
        print("******************************")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
