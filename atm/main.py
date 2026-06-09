from service import atm_service

while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        atm_service.show_balance()

    elif choice == "2":
        atm_service.deposit()

    elif choice == "3":
        atm_service.withdraw()

    elif choice == "4":
        atm_service.show_statement()

    elif choice == "5":
        break

    else:
        print("Invalid Choice")