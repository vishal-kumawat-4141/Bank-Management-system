from random import randint


class Bank:
    def __init__(self):
        self.name = input("Enter Account holder name : ")
        self.account_number = randint(1000000, 99999999)
        self.phone_number = int(input("Enter Account holder phone number :  "))
        self.current_balence = 0

    def deposit(self):
        deposit_amount = int(input("Enter deposit amount : "))
        self.current_balence += deposit_amount

    def withdrawl(self):
        withdrawl_amount = int(input("Enter withdrawl ammount : "))
        if self.current_balence < withdrawl_amount:
            print("Insuficiant bank balance!")
        else:
            self.current_balence -= withdrawl_amount

    def show_info(self):
        print(f"\nAccount Holder name : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account phone number  : {self.phone_number}")
        print(f"Account current balance : {self.current_balence}")


# n1 = Bank()
# n1.deposit()
# n1.withdrawl()
# n1.show_info()
Banks = []


def check_account_exist(acc_no: int):
    global Banks
    for obj in Banks:
        if obj.account_number == acc_no:
            return obj
    return None


while True:
    print("1. Create new Account.")
    print("2. show bank information.")
    print("3. Deposit.")
    print("4. withdrawal.")
    print("5. Transitions.")
    print("6. Exit.")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        obj = Bank()
        Banks.append(obj)
        print(Banks)

    elif choice == 2:
        if len(Banks) == 0:
            print(f"Bank Account not created yet.")
        else:
            for obj in Banks:
                obj.show_info()

    elif choice == 3:
        if len(Banks) == 0:
            print(f"Bank Account not created yet.")
        else:
            a_c = int(input("Enter your account number : "))
            factor = 0
            for obj in Banks:
                if obj.account_number == a_c:
                    factor += 1
                    obj.deposit()
            if factor == 0:
                print("Account number does not match .")

    elif choice == 4:
        if len(Banks) == 0:
            print(f"Bank Account not created yet.")
        else:
            account_number = int(input(f"Enter your account number : "))
            factor = 0
            for obj in Banks:
                if obj.account_number == account_number:
                    factor += 1
                    obj.withdrawl()
            if factor == 0:
                print(f"account number does not match in Banks detials!")
    elif choice == 5:
        if len(Banks) == 0:
            print(f"Bank Account not created yet.")
        else:
            from_account = int(input("Enter the your account number : "))
            to_account = int(input("Enter the reciver account number : "))
            from_account_obj = check_account_exist(from_account)
            to_account_obj = check_account_exist(to_account)
            if from_account_obj != None and to_account_obj != None:
                transfer_amount = int(input("Enter transfer ammount : "))
                if from_account_obj.current_balence < transfer_amount:
                    print(f"Insuficiant   in your account !")
                else:
                    from_account_obj.current_balence -= transfer_amount
                    to_account_obj.current_balence += transfer_amount
                    print(f"Your payment has successfully transfered .")
            else:
                print("Bank account does not match!")
    elif choice == 6:
        break


# Anoter method for bank transtion

# if choice == 5:
#         if len(Banks) == 0:
#             print("There is no account found.\nFirst, create a account.")
#         else:
#             Sender_acc_num = int(
#                 input("For Transction, Enter Sender's(Your) Account no. : ")
#             )
#             Sender_found = 0
#             for Sender_obj in Banks:
#                 if Sender_acc_num == Sender_obj.account_number:
#                     Receiver_acc_num = int(
#                         input("For Transction, Enter Receiver's Account no. : ")
#                     )
#                     Receiver_found = 0
#                     for Receiver_obj in Banks:
#                         if Receiver_acc_num == Receiver_obj.account_number:
#                             Receiver_found += 1
#                             transfer_amount = int(
#                                 input("For Transfer, Enter the amount : ")
#                             )
#                             if transfer_amount <= Sender_obj.current_balence:
#                                 Sender_obj.current_balence -= transfer_amount
#                                 Receiver_obj.current_balence += transfer_amount
#                                 print(
#                                     f"{transfer_amount}Rs. transferd Successfully from {Sender_obj.name}  to {Receiver_obj.name}."
#                                 )
#                             else:
#                                 print("Insuficient bank balance.")

#                     if Receiver_found == 0:
#                         print("Receiver's Account does not exist.")
#                     Sender_found += 1

#             if Sender_found == 0:
#                 print("Sender's Account does not exist.")
